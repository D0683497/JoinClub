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

  constructor(
    private fb: FormBuilder,
    @Inject(MAT_DIALOG_DATA) private data: User,
    private dialogRef: MatDialogRef<ScanResultComponent>,
    private snackBar: MatSnackBar,
    private userService: UserService) { }

  ngOnInit(): void {
    this.checkJoinForm = this.fb.group({
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

  onSubmit(checkJoinForm: User): void {
    this.userService.updateUser(this.data.id, checkJoinForm).subscribe(
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
    this.snackBar.open('修改失敗', '關閉', { duration: 5000 });
  }



}
