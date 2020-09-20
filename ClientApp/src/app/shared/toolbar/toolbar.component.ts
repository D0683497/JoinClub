import { AccountService } from '../../services/account/account.service';
import { AuthService } from '../../services/auth/auth.service';
import { Component, OnInit } from '@angular/core';
import { Observable } from 'rxjs';
import { Router } from '@angular/router';
import Swal from 'sweetalert2/dist/sweetalert2.js';

@Component({
  selector: 'app-toolbar',
  templateUrl: './toolbar.component.html',
  styleUrls: ['./toolbar.component.scss']
})
export class ToolbarComponent implements OnInit {

  isLoggedIn$: Observable<boolean>;

  constructor(
    private authService: AuthService,
    private router: Router,
    private accountService: AccountService) {
  }

  ngOnInit(): void {
    this.isLoggedIn$ = this.authService.getLoginStatus();
  }

  getUserName(): string {
    return this.authService.getUniqueName();
  }

  logout(): void {
    this.accountService.logout();
    Swal.fire({
      icon: 'success',
      title: '成功登出',
      confirmButtonText: '確認',
      showCloseButton: true
    });
    this.router.navigate(['/']);
  }

}
