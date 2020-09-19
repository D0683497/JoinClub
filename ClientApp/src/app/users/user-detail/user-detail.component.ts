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

  deleteUser(userId: string): void {
    this.userService.deleteUser(userId).subscribe(
      (res) => {
        this.dialogRef.close();
        this.snackBar.open('刪除成功', '關閉', { duration: 5000 });
      },
      (err) => {
        this.snackBar.open('刪除失敗', '關閉', { duration: 5000 });
      }
    );
  }

  updateFail(err: HttpErrorResponse): void {
    if (err.status === 400) {
      const validationErrors = err.error.errors;
      Object.keys(validationErrors).forEach(prop => {
        const controlName = prop.charAt(0).toLowerCase() + prop.slice(1); // 讓首字母變成小寫
        validationErrors[prop].forEach(element => {
          this.userDetailForm.controls[controlName].setErrors({server: element});
        });
      });
    }
    this.snackBar.open('修改失敗', '關閉', { duration: 5000 });
  }

  onSubmit(userDetailForm: User): void {
    this.userService.updateUser(this.data.id, userDetailForm).subscribe(
      (res) => {
        this.snackBar.open('修改成功', '關閉', { duration: 5000 });
        this.dialogRef.close();
      },
      (err: HttpErrorResponse) => {
        this.updateFail(err);
      }
    );
  }

}
