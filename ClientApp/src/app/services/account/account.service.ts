import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { map } from 'rxjs/operators';
import { ChangePassword } from '../../models/account/change-password/change-password.model';
import { LoginResponse } from '../../models/account/login/login-response.model';
import { Login } from '../../models/account/login/login.model';
import { ChangeProfile } from '../../models/account/profile/change-profile.model';
import { Profile } from '../../models/account/profile/profile';
import { Register } from '../../models/account/register/register.model';
import { environment } from '../../../environments/environment';
import { AuthService } from '../auth/auth.service';

@Injectable({
  providedIn: 'root'
})
export class AccountService {

  urlRoot = environment.apiUrl;

  httpOptions = {
    headers: new HttpHeaders({ 'Content-Type': 'application/json' })
  };

  constructor(
    private http: HttpClient,
    private authService: AuthService) { }

  // 登入
  login(loginForm: Login): Observable<void> {
    const url = `${this.urlRoot}/auth/login`;
    return this.http.post(url, loginForm, this.httpOptions).pipe(
      map((data: LoginResponse) => {
        this.authService.setToken(data.access_token);
        this.authService.setLoginStatus(true);
        this.authService.setAutoCheckLoginStatus();
      })
    );
  }

  // 登出
  logout(): void {
    this.authService.removeLoginStatus();
  }

  // 註冊
  register(registerForm: Register): Observable<object> {
    const url = `${this.urlRoot}/account/register`;
    return this.http.post(url, registerForm, this.httpOptions);
  }

  // 獲取個人資訊
  getProfile(): Observable<Profile> {
    const userId = this.authService.getUserId();
    const url = `${this.urlRoot}/account/${userId}/profile`;
    return this.http.get<Profile>(url, this.httpOptions);
  }

  // 修改個人資訊
  changeProfile(data: ChangeProfile): Observable<object> {
    const userId = this.authService.getUserId();
    const url = `${this.urlRoot}/account/${userId}/profile`;
    return this.http.post(url, data, this.httpOptions);
  }

  // 更改密碼
  changePassword(data: ChangePassword): Observable<object> {
    const userId = this.authService.getUserId();
    const url = `${this.urlRoot}/account/${userId}/change-password`;
    return this.http.post(url, data, this.httpOptions);
  }

}
