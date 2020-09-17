import { UserService } from '../../services/user/user.service';
import { AuthService } from '../../services/auth/auth.service';
import { Profile } from '../../models/profile/profile';
import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { BehaviorSubject } from 'rxjs';
import { User } from 'src/app/models/user/user.model';
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
  userData: User;

  constructor(
    private fb: FormBuilder,
    private authService: AuthService,
    private userService: UserService,
    private snackBar: MatSnackBar) {
      this.userId = this.authService.getUserId();
    }

  ngOnInit(): void {
    this.getData();
    this.profileForm = this.fb.group({
      email: [this.userData.email, [Validators.required, Validators.email]],
      userName: [this.userData.userName, [Validators.required, Validators.pattern(this.pattern)]],
      phoneNumber: this.userData.phoneNumber,
      nid: [this.userData.nid, Validators.required],
      name: [this.userData.name, Validators.required],
      college: [this.userData.college, Validators.required],
      department: [this.userData.department, Validators.required],
      class: [this.userData.class, Validators.required]
    });
    this.isLoading$.next(false);
  }

  getData(): void {
    this.userService.getUserById(this.userId).subscribe(
      (res) => {
        this.userData = res;
        this.isfetchDataError$.next(false);
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
