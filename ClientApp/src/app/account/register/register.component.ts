import { Component, OnInit } from '@angular/core';
import { FormGroup, FormBuilder, Validators, FormGroupDirective } from '@angular/forms';
import { AuthService } from 'src/app/services/auth/auth.service';
import { Register } from 'src/app/models/register/register.model';
import Swal from 'sweetalert2/dist/sweetalert2.js';
import { Router } from '@angular/router';
import { HttpResponse, HttpErrorResponse } from '@angular/common/http';

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.scss']
})
export class RegisterComponent implements OnInit {

  pattern = new RegExp(/[\w\-\.\@\+\#\$\%\\\/\(\)\[\]\*\&\:\>\<\^\!\{\}\=]+/gm);
  loading = false;
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
    });
  }

  onSubmit(registerForm: Register, formDirective: FormGroupDirective): void {
    this.loading = true;
    this.authService.register(registerForm).subscribe(
      data => {
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
        this.loading = false;
      },
      (e: HttpErrorResponse) => {
        if (e.status === 400) {
          if (e.error.errors.NID) {
            for (const field of e.error.errors.NID) {
              this.registerForm.controls.nid.setErrors({ server: field });
            }
          }
          if (e.error.errors.Email) {
            for (const field of e.error.errors.Email) {
              this.registerForm.controls.email.setErrors({ server: field });
            }
          }
          if (e.error.errors.UserName) {
            for (const field of e.error.errors.UserName) {
              this.registerForm.controls.userName.setErrors({ server: field });
            }
          }
        }
        Swal.fire({
          icon: 'error',
          title: '註冊失敗',
          confirmButtonText: '確認',
          showCloseButton: true
        });
        this.loading = false;
      }
    );
  }

}
