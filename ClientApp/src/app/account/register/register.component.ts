import { Component, OnInit } from '@angular/core';
import { FormGroup, FormBuilder, Validators } from '@angular/forms';
import { AuthService } from '../../services/auth/auth.service';
import { Register } from '../../models/register/register.model';
import Swal from 'sweetalert2/dist/sweetalert2.js';
import { Router } from '@angular/router';
import { HttpErrorResponse } from '@angular/common/http';
import { BehaviorSubject } from 'rxjs';
import { MustMatch } from '../../shared/helpers/must-match.validator';

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.scss']
})
export class RegisterComponent implements OnInit {

  pattern = new RegExp(/[\w\-\.\@\+\#\$\%\\\/\(\)\[\]\*\&\:\>\<\^\!\{\}\=]+/gm);
  isLoading$: BehaviorSubject<boolean> = new BehaviorSubject(false);
  registerForm: FormGroup;
  hidePassword = true;
  hideConfirmPassword = true;

  constructor(
    private fb: FormBuilder,
    private authService: AuthService,
    private router: Router) { }

  ngOnInit(): void {
    this.registerForm = this.fb.group({
      email: [null, [Validators.required, Validators.email]],
      userName: [null, [Validators.required, Validators.pattern(this.pattern)]],
      password: [null, [Validators.required, Validators.minLength(8), Validators.maxLength(64)]],
      passwordConfirm: [null, [Validators.required, Validators.minLength(8), Validators.maxLength(64)]],
      phoneNumber: null,
      nid: [null, Validators.required],
      name: [null, Validators.required],
      college: [null, Validators.required],
      department: [null, Validators.required],
      class: [null, Validators.required]
    }, { validator: MustMatch('password', 'confirmPassword') });
  }

  registerSuccess(): void {
    Swal.fire({
      icon: 'success',
      title: '註冊成功',
      toast: true,
      position: 'bottom',
      showConfirmButton: false,
      timer: 5000,
      timerProgressBar: true,
    });
    this.router.navigate(['/account/login']);
  }

  registerFail(err: HttpErrorResponse): void {
    if (err.status === 400) {
      const validationErrors = err.error.errors;
      Object.keys(validationErrors).forEach(prop => {
        const controlName = prop.charAt(0).toLowerCase() + prop.slice(1); // 讓首字母變成小寫

        // 雖然可能有多個錯誤，但後面的會蓋掉前面的
        validationErrors[prop].forEach(element => {
          this.registerForm.controls[controlName].setErrors({server: element});
        });
      });
    }
    Swal.fire({
      icon: 'error',
      title: '註冊失敗',
      confirmButtonText: '確認',
      showCloseButton: true
    });
  }

  onSubmit(registerForm: Register): void {
    this.isLoading$.next(true);
    this.authService.register(registerForm).subscribe(
      (res) => { this.registerSuccess(); },
      (err: HttpErrorResponse) => {
        this.registerFail(err);
        this.isLoading$.next(false);
      }
    );
  }

}
