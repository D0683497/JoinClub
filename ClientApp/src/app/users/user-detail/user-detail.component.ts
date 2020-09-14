import { HttpErrorResponse } from '@angular/common/http';
import { UserService } from '../../services/user/user.service';
import { User } from '../../models/user/user.model';
import { Component, Inject, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { MatDialogRef, MAT_DIALOG_DATA } from '@angular/material/dialog';
import { MatSnackBar } from '@angular/material/snack-bar';

@Component({
  selector: 'app-user-detail',
  templateUrl: './user-detail.component.html',
  styleUrls: ['./user-detail.component.scss']
})
export class UserDetailComponent implements OnInit {

  pattern = new RegExp(/[\w\-\.\@\+\#\$\%\\\/\(\)\[\]\*\&\:\>\<\^\!\{\}\=]+/gm);
  loading = false;
  userDetailForm: FormGroup;

  constructor(
    private fb: FormBuilder,
    @Inject(MAT_DIALOG_DATA) private data: User,
    private dialogRef: MatDialogRef<UserDetailComponent>,
    private snackBar: MatSnackBar,
    private userService: UserService) { }

  ngOnInit(): void {
    this.userDetailForm = this.fb.group({
      id: [{value: this.data.id, disabled: true}],
      email: [this.data.email, [Validators.required, Validators.email]],
      userName: [this.data.userName, [Validators.required, Validators.pattern(this.pattern)]],
      phoneNumber: this.data.phoneNumber,
      nid: [this.data.nid, Validators.required],
      name: [this.data.name, Validators.required],
      college: [this.data.college, Validators.required],
      department: [this.data.department, Validators.required],
      class: [this.data.class, Validators.required],
    });
  }

  onSubmit(userDetailForm: User): void {
    this.loading = true;
    console.log(userDetailForm);
    this.userService.updateUser(this.data.id, userDetailForm).subscribe(
      data => {
        this.snackBar.open('修改成功', '關閉', { duration: 5000 });
        this.dialogRef.close();
      },
      (e: HttpErrorResponse) => {
        if (e.status === 400) {
          if (e.error.Email) {
            for (const field of e.error.Email) {
              this.userDetailForm.controls.email.setErrors({ server: field });
            }
          }
          if (e.error.NID) {
            for (const field of e.error.NID) {
              this.userDetailForm.controls.nid.setErrors({ server: field });
            }
          }
          if (e.error.UserName) {
            for (const field of e.error.UserName) {
              this.userDetailForm.controls.userName.setErrors({ server: field });
            }
          }
          if (e.error.PhoneNumber) {
            for (const field of e.error.PhoneNumber) {
              this.userDetailForm.controls.phoneNumber.setErrors({ server: field });
            }
          }
        }
        this.snackBar.open('修改失敗', '關閉', { duration: 5000 });
        this.loading = false;
      }
    );
  }

}
