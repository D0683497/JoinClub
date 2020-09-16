import { Injectable } from '@angular/core';
import { environment } from '../../../environments/environment';
import { HttpHeaders, HttpClient } from '@angular/common/http';
import { JwtHelperService } from '@auth0/angular-jwt';
import { Router } from '@angular/router';
import { Login } from '../../models/login/login.model';
import { Observable, BehaviorSubject } from 'rxjs';
import { LoginResponse } from '../../models/login/login-response.model';
import { map } from 'rxjs/operators';
import { Register } from '../../models/register/register.model';
import Swal from 'sweetalert2/dist/sweetalert2.js';

@Injectable({
  providedIn: 'root'
})
export class AuthService {

  urlRoot = environment.apiUrl;
  isLoginSubject$ = new BehaviorSubject<boolean>(this.hasToken());

  httpOptions = {
    headers: new HttpHeaders({ 'Content-Type': 'application/json' })
  };

  constructor(
    private http: HttpClient,
    private jwtHelper: JwtHelperService,
    private router: Router) { }

  // 登入
  login(loginForm: Login): Observable<void> {
    const url = `${this.urlRoot}/auth/login`;
    return this.http.post(url, loginForm, this.httpOptions).pipe(
      map((data: LoginResponse) => {
        localStorage.setItem('access_token', data.access_token);
        this.isLoginSubject$.next(true);
      })
    );
  }

  // 註冊
  register(registerForm: Register): Observable<object> {
    const url = `${this.urlRoot}/account/register`;
    return this.http.post(url, registerForm, this.httpOptions);
  }

  // 登出
  logout(): void {
    localStorage.clear();
    this.isLoginSubject$.next(false);
    Swal.fire({
      icon: 'success',
      title: '成功登出',
      confirmButtonText: '確認',
      showCloseButton: true
    });
    this.router.navigate(['/']);
  }

  // 更改密碼
  changePassword(oldPassword: string, newPassword: string): Observable<object> {
    const url = `${this.urlRoot}/account/change-password`;
    const body = {
      userId: this.getUserId(),
      oldPassword,
      newPassword
    };
    return this.http.post(url, body, this.httpOptions);
  }

  // 獲取角色
  getRole(): string {
    const token = localStorage.getItem('access_token');
    const decodeToken = this.jwtHelper.decodeToken(token);
    return decodeToken.role;
  }

  // 獲取用戶名稱
  getUniqueName(): string {
    const token = localStorage.getItem('access_token');
    const decodeToken = this.jwtHelper.decodeToken(token);
    return decodeToken.unique_name;
  }

  // 獲取用戶 Id
  getUserId(): string {
    const token = localStorage.getItem('access_token');
    const decodeToken = this.jwtHelper.decodeToken(token);
    return decodeToken.nameid;
  }

  // Token 是否過期
  isTokenExpired(): boolean {
    return this.jwtHelper.isTokenExpired(localStorage.getItem('access_token'));
  }

  // 是否有 token
  private hasToken(): boolean {
    return localStorage.getItem('access_token') != null;
  }

  // 是否登入
  isLoggedIn(): Observable<boolean> {
    return this.isLoginSubject$.asObservable();
  }

}
