import { Profile } from '../../models/account/profile/profile';
import { ChangeProfile } from '../../models/account/profile/change-profile.model';
import { ChangePassword } from '../../models/account/change-password/change-password.model';
import { Injectable } from '@angular/core';
import { environment } from '../../../environments/environment';
import { HttpHeaders, HttpClient } from '@angular/common/http';
import { JwtHelperService } from '@auth0/angular-jwt';
import { Login } from '../../models/account/login/login.model';
import { Observable, BehaviorSubject, of } from 'rxjs';
import { LoginResponse } from '../../models/account/login/login-response.model';
import { map } from 'rxjs/operators';
import { Register } from '../../models/account/register/register.model';

@Injectable({
  providedIn: 'root'
})
export class AuthService {

  urlRoot = environment.apiUrl;
  loginStatus$ = new BehaviorSubject<boolean>(false);

  httpOptions = {
    headers: new HttpHeaders({ 'Content-Type': 'application/json' })
  };

  constructor(
    private http: HttpClient,
    private jwtHelper: JwtHelperService) { }

  // 登出
  logout(): void {
    localStorage.clear();
    this.loginStatus$.next(false);
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

  // 檢查登入狀態
  checkLoginStatus(): void {
    if (!this.isTokenExpired()) { // token 沒過期
      this.loginStatus$.next(true);
    } else { // token 過期或沒有 token
      this.logout();
    }
  }

  // 獲取登入狀態
  getLoginStatus(): Observable<boolean> {
    this.checkLoginStatus();
    return this.loginStatus$;
  }

  // 登入
  login(loginForm: Login): Observable<void> {
    const url = `${this.urlRoot}/auth/login`;
    return this.http.post(url, loginForm, this.httpOptions).pipe(
      map((data: LoginResponse) => {
        localStorage.setItem('access_token', data.access_token);
        this.loginStatus$.next(true);
        setInterval(() => { // 每 5 分鐘確認一次登入狀態(檢查 token 是否過期)
          this.checkLoginStatus();
        }, 1000 * 60 * 5);
      })
    );
  }

  // 註冊
  register(registerForm: Register): Observable<object> {
    const url = `${this.urlRoot}/account/register`;
    return this.http.post(url, registerForm, this.httpOptions);
  }

  // 獲取個人資訊
  getProfile(): Observable<Profile> {
    const url = `${this.urlRoot}/account/${this.getUserId()}/profile`;
    return this.http.get<Profile>(url, this.httpOptions);
  }

  // 修改個人資訊
  changeProfile(data: ChangeProfile): Observable<object> {
    const url = `${this.urlRoot}/account/${this.getUserId()}/profile`;
    return this.http.post(url, data, this.httpOptions);
  }

  // 更改密碼
  changePassword(data: ChangePassword): Observable<object> {
    const url = `${this.urlRoot}/account/${this.getUserId()}/change-password`;
    return this.http.post(url, data, this.httpOptions);
  }

}
