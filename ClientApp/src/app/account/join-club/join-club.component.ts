import { AuthService } from 'src/app/services/auth/auth.service';
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-join-club',
  templateUrl: './join-club.component.html',
  styleUrls: ['./join-club.component.scss']
})
export class JoinClubComponent implements OnInit {

  joinCode: string;

  constructor(private authService: AuthService) { }

  ngOnInit(): void {
    const userId = this.authService.getUserId();
    this.joinCode = `HackerSir-join-code-${userId}`;
  }

}
