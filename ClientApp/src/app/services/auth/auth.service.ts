import { Injectable } from '@angular/core';
import { JwtHelperService } from '@auth0/angular-jwt';
import { Observable, BehaviorSubject } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class AuthService {

  loginStatus$ = new BehaviorSubject<boolean>(false);

  constructor(private jwtHelper: JwtHelperService) { }

  // 獲取登入狀態
  getLoginStatus(): Observable<boolean> {
    this.checkLoginStatus();
    return this.loginStatus$;
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

  // 設置 token
  setToken(token: string): void {
    localStorage.setItem('access_token', token);
  }

  // 設置登入狀態
  setLoginStatus(status: boolean): void {
    this.loginStatus$.next(status);
  }

  // 設置自動檢查登入狀態
  setAutoCheckLoginStatus(): void {
    setInterval(() => { // 每 5 分鐘確認一次登入狀態(檢查 token 是否過期)
      this.checkLoginStatus();
    }, 1000 * 60 * 5);
  }

  // 移除登入狀態 (登出)
  removeLoginStatus(): void {
    localStorage.clear();
    this.loginStatus$.next(false);
  }

  // Token 是否過期
  private isTokenExpired(): boolean {
    return this.jwtHelper.isTokenExpired(localStorage.getItem('access_token'));
  }

  // 檢查登入狀態
  private checkLoginStatus(): void {
    if (!this.isTokenExpired()) { // token 沒過期
      this.loginStatus$.next(true);
    } else { // token 過期或沒有 token
      this.removeLoginStatus();
    }
  }

}
