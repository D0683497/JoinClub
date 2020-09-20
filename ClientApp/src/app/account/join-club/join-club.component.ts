import { AuthService } from 'src/app/services/auth/auth.service';
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-join-club',
  templateUrl: './join-club.component.html',
  styleUrls: ['./join-club.component.scss']
})
export class JoinClubComponent implements OnInit {

  userId: string;

  constructor(private authService: AuthService) { }

  ngOnInit(): void {
    this.userId = this.authService.getUserId();
  }

}
