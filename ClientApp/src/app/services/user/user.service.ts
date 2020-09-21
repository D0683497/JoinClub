import { Observable } from 'rxjs';
import { Injectable } from '@angular/core';
import { environment } from '../../../environments/environment';
import { HttpHeaders, HttpClient } from '@angular/common/http';
import { User } from '../../models/user/user.model';

@Injectable({
  providedIn: 'root'
})
export class UserService {

  urlRoot = environment.apiUrl;

  httpOptions = {
    headers: new HttpHeaders({ 'Content-Type': 'application/json' })
  };

  constructor(private http: HttpClient) { }

  // 獲取所有使用者
  getAllUsers(pageIndex: number, pageSize: number): Observable<User[]> {
    const url = `${this.urlRoot}/users?pageNumber=${pageIndex}&pageSize=${pageSize}`;
    return this.http.get<User[]>(url, this.httpOptions);
  }

  // 獲取所有使用者數量
  getAllItemsLength(): Observable<number> {
    const url = `${this.urlRoot}/users/length`;
    return this.http.get<number>(url, this.httpOptions);
  }

  // 修改用戶資料
  updateUser(userId: string, user: User): Observable<object> {
    const url = `${this.urlRoot}/users/${userId}`;
    return this.http.post(url, user, this.httpOptions);
  }

  // 刪除用戶
  deleteUser(userId: string): Observable<object> {
    const url = `${this.urlRoot}/users/${userId}`;
    return this.http.delete(url, this.httpOptions);
  }

  // 使用 Id 獲取使用者
  getUserById(userId: string): Observable<User> {
    const url = `${this.urlRoot}/users/${userId}`;
    return this.http.get<User>(url, this.httpOptions);
  }

  // 使用 Id 獲取使用者角色
  getUserRoleById(userId: string): Observable<string[]> {
    const url = `${this.urlRoot}/users/${userId}/role`;
    return this.http.get<string[]>(url, this.httpOptions);
  }

  // 使用 Id 讓使用者入社
  joinUserById(userId: string): Observable<object> {
    const url = `${this.urlRoot}/users/${userId}/join`;
    return this.http.post(url, this.httpOptions);
  }

  // 使用 nid 獲取 id
  getUserIdByNID(nid: string): Observable<object> {
    const url = `${this.urlRoot}/users/${nid}/nid-to-id`;
    return this.http.get(url, this.httpOptions);
  }

}
