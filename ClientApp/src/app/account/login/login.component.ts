import { Component, OnInit } from '@angular/core';
import { FormGroup, FormBuilder, Validators } from '@angular/forms';
import { AuthService } from 'src/app/services/auth/auth.service';
import { Router } from '@angular/router';
import { Login } from '../../models/account/login/login.model';
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

  loginSuccess(): void {
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
  }

  loginFail(err: HttpErrorResponse): void {
    switch (err.error) {
      case '帳號被鎖定': {
        Swal.fire({
          icon: 'question',
          title: '帳號被鎖定',
          confirmButtonText: '確認',
          showCloseButton: true
        });
        break;
      }
      // case '尚未入社': {
      //   Swal.fire({
      //     icon: 'warning',
      //     title: '尚未入社',
      //     confirmButtonText: '確認',
      //     showCloseButton: true
      //   });
      //   break;
      // }
      default: {
        Swal.fire({
          icon: 'error',
          title: '登入失敗',
          confirmButtonText: '確認',
          showCloseButton: true
        });
        break;
      }
    }
  }

  onSubmit(loginForm: Login): void {
    this.authService.login(loginForm).subscribe(
      (res) => { this.loginSuccess(); },
      (err: HttpErrorResponse) => {
        this.loginFail(err);
      }
    );
  }

}
