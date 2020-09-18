import { ChangeProfile } from './../../models/account/profile/change-profile.model';
import { UserService } from '../../services/user/user.service';
import { AuthService } from '../../services/auth/auth.service';
import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { BehaviorSubject } from 'rxjs';
import { MatSnackBar } from '@angular/material/snack-bar';
import { User } from 'src/app/models/user/user.model';
import { HttpErrorResponse } from '@angular/common/http';

@Component({
  selector: 'app-profile',
  templateUrl: './profile.component.html',
  styleUrls: ['./profile.component.scss']
})
export class ProfileComponent implements OnInit {

  pattern = new RegExp(/[\w\-\.\@\+\#\$\%\\\/\(\)\[\]\*\&\:\>\<\^\!\{\}\=]+/gm);
  isLoading$: BehaviorSubject<boolean> = new BehaviorSubject(true);
  isfetchDataError$: BehaviorSubject<boolean> = new BehaviorSubject(false);
  isUpdateLoading$: BehaviorSubject<boolean> = new BehaviorSubject(false);
  profileForm: FormGroup;

  constructor(
    private fb: FormBuilder,
    private authService: AuthService,
    private snackBar: MatSnackBar) {
  }

  ngOnInit(): void {
    this.profileForm = this.fb.group({
      email: [{value: null, disabled: true}, [Validators.required, Validators.email]],
      userName: [{value: null, disabled: true}, [Validators.required, Validators.pattern(this.pattern)]],
      phoneNumber: {value: null, disabled: true},
      nid: [{value: null, disabled: true}, Validators.required],
      name: [null, Validators.required],
      college: [{value: null, disabled: true}, Validators.required],
      department: [{value: null, disabled: true}, Validators.required],
      class: [{value: null, disabled: true}, Validators.required]
    });
    this.getData();
  }

  getData(): void {
    this.authService.getProfile().subscribe(
      (res) => {
        Object.keys(res).forEach(prop => {
          const controlName = prop.charAt(0).toLowerCase() + prop.slice(1); // 讓首字母變成小寫
          this.profileForm.controls[controlName].setValue(res[prop]);
        });
        this.isfetchDataError$.next(false);
        this.isLoading$.next(false);
      },
      (err) => {
        this.snackBar.open('獲取資料失敗', '關閉', { duration: 5000 });
        this.isfetchDataError$.next(true);
        this.isLoading$.next(false);
      }
    );
  }

  reload(): void {
    this.isfetchDataError$.next(false);
    this.isLoading$.next(true);
    this.ngOnInit();
  }

  updateFail(err: HttpErrorResponse): void {
    if (err.status === 400) {
      const validationErrors = err.error.errors;
      Object.keys(validationErrors).forEach(prop => {
        const controlName = prop.charAt(0).toLowerCase() + prop.slice(1); // 讓首字母變成小寫
        validationErrors[prop].forEach(element => {
          this.profileForm.controls[controlName].setErrors({server: element});
        });
      });
    }
    this.snackBar.open('修改失敗', '關閉', { duration: 5000 });
  }

  onSubmit(data: ChangeProfile): void {
    this.isUpdateLoading$.next(true);
    this.authService.changeProfile(data).subscribe(
      (res) => {
        this.snackBar.open('修改成功', '關閉', { duration: 5000 });
        this.isUpdateLoading$.next(false);
      },
      (err: HttpErrorResponse) => {
        this.updateFail(err);
        this.isUpdateLoading$.next(false);
      }
    );
  }

}
