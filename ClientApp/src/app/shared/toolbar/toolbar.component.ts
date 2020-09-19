import { AuthService } from '../../services/auth/auth.service';
import { Component } from '@angular/core';
import { Observable } from 'rxjs';
import { Router } from '@angular/router';
import Swal from 'sweetalert2/dist/sweetalert2.js';

@Component({
  selector: 'app-toolbar',
  templateUrl: './toolbar.component.html',
  styleUrls: ['./toolbar.component.scss']
})
export class ToolbarComponent {

  isLoggedIn$: Observable<boolean>;

  constructor(private authService: AuthService, private router: Router) {
    this.isLoggedIn$ = authService.getLoginStatus();
  }

  logout(): void {
    this.authService.logout();
    Swal.fire({
      icon: 'success',
      title: '成功登出',
      confirmButtonText: '確認',
      showCloseButton: true
    });
    this.router.navigate(['/']);
  }

}
