import { HttpErrorResponse } from '@angular/common/http';
import { Component, Inject, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { MatDialogRef, MAT_DIALOG_DATA } from '@angular/material/dialog';
import { MatSnackBar } from '@angular/material/snack-bar';
import { UserService } from 'src/app/services/user/user.service';
import { User } from '../../models/user/user.model';

@Component({
  selector: 'app-scan-result',
  templateUrl: './scan-result.component.html',
  styleUrls: ['./scan-result.component.scss']
})
export class ScanResultComponent implements OnInit {

  pattern = new RegExp(/[\w\-\.\@\+\#\$\%\\\/\(\)\[\]\*\&\:\>\<\^\!\{\}\=]+/gm);
  checkJoinForm: FormGroup;
  role: string;

  constructor(
    private fb: FormBuilder,
    @Inject(MAT_DIALOG_DATA) private data: any,
    private dialogRef: MatDialogRef<ScanResultComponent>,
    private snackBar: MatSnackBar,
    private userService: UserService) { }

  ngOnInit(): void {
    this.role = this.data.role;
    this.checkJoinForm = this.fb.group({
      id: [{value: this.data.user.id, disabled: true}],
      email: [this.data.user.email, [Validators.required, Validators.email]],
      userName: [this.data.user.userName, [Validators.required, Validators.pattern(this.pattern)]],
      phoneNumber: this.data.user.phoneNumber,
      nid: [this.data.user.nid, Validators.required],
      name: [this.data.user.name, Validators.required],
      college: [this.data.user.college, Validators.required],
      department: [this.data.user.department, Validators.required],
      class: [this.data.user.class, Validators.required],
    });
  }

  onSubmit(checkJoinForm: User): void {
    this.userService.updateUser(this.data.user.id, checkJoinForm).subscribe(
      (res) => {
        this.snackBar.open('修改成功', '關閉', { duration: 3000 });
        this.dialogRef.close();
      },
      (err: HttpErrorResponse) => {
        this.updateFail(err);
      }
    );
  }

  updateFail(err: HttpErrorResponse): void {
    if (err.status === 400) {
      const validationErrors = err.error.errors;
      Object.keys(validationErrors).forEach(prop => {
        const controlName = prop.charAt(0).toLowerCase() + prop.slice(1); // 讓首字母變成小寫
        validationErrors[prop].forEach(element => {
          this.checkJoinForm.controls[controlName].setErrors({server: element});
        });
      });
    }
    this.snackBar.open('修改失敗', '關閉', { duration: 3000 });
  }

  join(): void {
    this.userService.joinUserById(this.data.user.id).subscribe(
      (res) => {
        this.snackBar.open('申請成功', '關閉', { duration: 3000 });
        this.dialogRef.close();
      },
      (err) => {
        this.snackBar.open('申請失敗', '關閉', { duration: 3000 });
      }
    );
  }

}
