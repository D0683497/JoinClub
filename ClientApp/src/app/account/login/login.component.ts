import { Component, OnInit } from '@angular/core';
import { FormGroup, FormBuilder, Validators, FormGroupDirective } from '@angular/forms';
import { AuthService } from 'src/app/services/auth/auth.service';
import { Router } from '@angular/router';
import { Login } from 'src/app/models/login/login.model';
import Swal from 'sweetalert2/dist/sweetalert2.js';
import { HttpErrorResponse } from '@angular/common/http';
import { BehaviorSubject } from 'rxjs';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss']
})
export class LoginComponent implements OnInit {

  pattern = new RegExp(/[\w\-\.\@\+\#\$\%\\\/\(\)\[\]\*\&\:\>\<\^\!\{\}\=]+/gm);
  isLoading$: BehaviorSubject<boolean> = new BehaviorSubject(false);
  loginForm: FormGroup;
  hide = true;

  constructor(
    private fb: FormBuilder,
    private authService: AuthService,
    private router: Router) { }

  ngOnInit(): void {
    this.loginForm = this.fb.group({
      userName: [null, [Validators.required, Validators.pattern(this.pattern)]],
      password: [null, [Validators.required, Validators.minLength(8), Validators.maxLength(64)]]
    });
  }

  onSubmit(loginForm: Login, formDirective: FormGroupDirective): void {
    this.isLoading$.next(true);
    this.authService.login(loginForm).subscribe(
      data => {
        Swal.fire({
          icon: 'success',
          title: '登入成功',
          toast: true,
          position: 'bottom',
          showConfirmButton: false,
          timer: 5000,
          timerProgressBar: true,
        });
        this.router.navigate(['/']);
        this.isLoading$.next(false);
      },
      (error: HttpErrorResponse) => {
        if (error.error === '帳號被鎖定') {
          Swal.fire({
            icon: 'error',
            title: '帳號被鎖定',
            confirmButtonText: '確認',
            showCloseButton: true
          });
          this.isLoading$.next(false);
        } else if (error.error === '尚未入社') {
          Swal.fire({
            icon: 'error',
            title: '尚未入社',
            confirmButtonText: '確認',
            showCloseButton: true
          });
          this.isLoading$.next(false);
        } else {
          Swal.fire({
            icon: 'error',
            title: '登入失敗',
            confirmButtonText: '確認',
            showCloseButton: true
          });
          this.isLoading$.next(false);
        }
      }
    );
  }

}
