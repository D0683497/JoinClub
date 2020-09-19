import { AccountService } from '../../services/account/account.service';
import { ChangePassword } from '../../models/account/change-password/change-password.model';
import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { MustMatch } from '../../shared/helpers/must-match.validator';
import { HttpErrorResponse } from '@angular/common/http';
import Swal from 'sweetalert2/dist/sweetalert2.js';
import { Router } from '@angular/router';

@Component({
  selector: 'app-change-password',
  templateUrl: './change-password.component.html',
  styleUrls: ['./change-password.component.scss']
})
export class ChangePasswordComponent implements OnInit {

  changePasswordForm: FormGroup;
  hideCurrentPassword = true;
  hideNewPassword = true;
  hideConfirmNewPassword = true;

  constructor(
    private fb: FormBuilder,
    private accountService: AccountService,
    private router: Router) { }

  ngOnInit(): void {
    this.changePasswordForm = this.fb.group({
      currentPassword: [null, [Validators.required, Validators.minLength(8), Validators.maxLength(64)]],
      newPassword: [null, [Validators.required, Validators.minLength(8), Validators.maxLength(64)]],
      confirmNewPassword: [null, [Validators.required, Validators.minLength(8), Validators.maxLength(64)]]
    }, { validator: MustMatch('newPassword', 'confirmNewPassword') });
  }

  changePasswordFail(err: HttpErrorResponse): void {
    if (err.status === 400) {
      const validationErrors = err.error.errors;
      Object.keys(validationErrors).forEach(prop => {
        const controlName = prop.charAt(0).toLowerCase() + prop.slice(1); // 讓首字母變成小寫

        // 雖然可能有多個錯誤，但後面的會蓋掉前面的
        validationErrors[prop].forEach(element => {
          this.changePasswordForm.controls[controlName].setErrors({server: element});
        });
      });
    }
    Swal.fire({
      icon: 'error',
      title: '修改密碼失敗',
      confirmButtonText: '確認',
      showCloseButton: true
    });
  }

  onSubmit(data: ChangePassword): void {
    this.accountService.changePassword(data).subscribe(
      (res) => {
        this.accountService.logout();
        Swal.fire({
          icon: 'success',
          title: '修改密碼成功',
          text: '請重新登入',
          confirmButtonText: '確認',
          showCloseButton: true
        });
        this.router.navigate(['/account/login']);
      },
      (err: HttpErrorResponse) => {
        this.changePasswordFail(err);
      }
    );
  }

}
