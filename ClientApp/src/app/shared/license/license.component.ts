import { Component, OnInit } from '@angular/core';
import { FRONTENDLICENSES, BACKENDLICENSES, IDELICENSES, OTHERLICENSES } from './mock-licenses';

@Component({
  selector: 'app-license',
  templateUrl: './license.component.html',
  styleUrls: ['./license.component.scss']
})
export class LicenseComponent implements OnInit {

  frontendLisenses = FRONTENDLICENSES;
  backendLicenses = BACKENDLICENSES;
  ideLicenses = IDELICENSES;
  otherLicenses = OTHERLICENSES;
  panelOpenState: boolean;

  constructor() { }

  ngOnInit(): void {
    this.panelOpenState = false;
  }

}
