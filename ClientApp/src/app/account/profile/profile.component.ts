import { JoinClubComponent } from './../join-club/join-club.component';
import { ChangeProfile } from '../../models/account/profile/change-profile.model';
import { AuthService } from '../../services/auth/auth.service';
import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { BehaviorSubject } from 'rxjs';
import { MatSnackBar } from '@angular/material/snack-bar';
import { HttpErrorResponse } from '@angular/common/http';
import { AccountService } from '../../services/account/account.service';
import { MatDialog } from '@angular/material/dialog';

@Component({
  selector: 'app-profile',
  templateUrl: './profile.component.html',
  styleUrls: ['./profile.component.scss']
})
export class ProfileComponent implements OnInit {

  pattern = new RegExp(/[\w\-\.\@\+\#\$\%\\\/\(\)\[\]\*\&\:\>\<\^\!\{\}\=]+/gm);
  isfetchDataError$: BehaviorSubject<boolean> = new BehaviorSubject(false);
  profileForm: FormGroup;
  role: string;

  constructor(
    private fb: FormBuilder,
    private authService: AuthService,
    private snackBar: MatSnackBar,
    private accountService: AccountService,
    private dialog: MatDialog) { }

  ngOnInit(): void {
    this.role = this.authService.getRole();
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
    this.accountService.getProfile().subscribe(
      (res) => {
        Object.keys(res).forEach(prop => {
          const controlName = prop.charAt(0).toLowerCase() + prop.slice(1); // 讓首字母變成小寫
          this.profileForm.controls[controlName].setValue(res[prop]);
        });
        this.isfetchDataError$.next(false);
      },
      (err) => {
        this.snackBar.open('獲取資料失敗', '關閉', { duration: 5000 });
        this.isfetchDataError$.next(true);
      }
    );
  }

  reload(): void {
    this.isfetchDataError$.next(false);
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
    this.accountService.changeProfile(data).subscribe(
      (res) => {
        this.snackBar.open('修改成功', '關閉', { duration: 5000 });
      },
      (err: HttpErrorResponse) => {
        this.updateFail(err);
      }
    );
  }

  joinClub(): void {
    const dialogRef = this.dialog.open(JoinClubComponent);
    dialogRef.afterClosed().subscribe(() => {
      this.ngOnInit();
    });
  }

}
