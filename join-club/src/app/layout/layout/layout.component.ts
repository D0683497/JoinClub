import { Component, OnInit, ViewChild } from '@angular/core';
import { Observable } from "rxjs";
import { BreakpointObserver, Breakpoints } from "@angular/cdk/layout";
import { map, shareReplay } from "rxjs/operators";
import { MatSidenav } from "@angular/material/sidenav";

@Component({
  selector: 'app-layout',
  templateUrl: './layout.component.html',
  styleUrls: ['./layout.component.scss']
})
export class LayoutComponent implements OnInit {

  @ViewChild('drawer') drawer!: MatSidenav;
  isHandset$: Observable<boolean> = this.breakpointObserver.observe(Breakpoints.Handset)
    .pipe(
      map(result => result.matches),
      shareReplay()
    );
  date = Date.now();
  sides = [
    {
      title: 'Dashboard',
      links: [
        {
          name: '首頁',
          url: '/',
          icon: 'home'
        }
      ]
    }
  ]

  constructor(private breakpointObserver: BreakpointObserver) { }

  ngOnInit(): void {
  }

  clickLink(): void {
    this.isHandset$.subscribe((data: boolean) => {
      if (data) {
        void this.drawer.toggle();
      }
    });
  }

}
