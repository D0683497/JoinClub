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
  userId: string;

  constructor(
    private fb: FormBuilder,
    private authService: AuthService,
    private userService: UserService,
    private snackBar: MatSnackBar) {
      this.userId = this.authService.getUserId();
      this.profileForm = this.fb.group({
        email: [null, [Validators.required, Validators.email]],
        userName: [null, [Validators.required, Validators.pattern(this.pattern)]],
        phoneNumber: null,
        nid: [null, Validators.required],
        name: [null, Validators.required],
        college: [null, Validators.required],
        department: [null, Validators.required],
        class: [null, Validators.required]
      });
    }

  ngOnInit(): void {
    this.getData();
  }

  getData(): void {
    this.userService.getUserById(this.userId).subscribe(
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

  onSubmit(data: User): void {
    this.isUpdateLoading$.next(true);
    this.userService.updateUser(this.userId, data).subscribe(
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
