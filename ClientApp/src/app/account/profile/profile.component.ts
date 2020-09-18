import { Profile } from '../../models/profile/profile';
import { UserService } from '../../services/user/user.service';
import { AuthService } from '../../services/auth/auth.service';
import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { BehaviorSubject } from 'rxjs';
import { MatSnackBar } from '@angular/material/snack-bar';

@Component({
  selector: 'app-profile',
  templateUrl: './profile.component.html',
  styleUrls: ['./profile.component.scss']
})
export class ProfileComponent implements OnInit {

  pattern = new RegExp(/[\w\-\.\@\+\#\$\%\\\/\(\)\[\]\*\&\:\>\<\^\!\{\}\=]+/gm);
  isLoading$: BehaviorSubject<boolean> = new BehaviorSubject(true);
  isfetchDataError$: BehaviorSubject<boolean> = new BehaviorSubject(false);
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
          this.profileForm.controls[prop].setValue(res[prop]);
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

  onSubmit(data: Profile): void {

  }

}
