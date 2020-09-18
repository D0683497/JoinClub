import { LoadingService } from '../../services/loading/loading.service';
import { Component, OnDestroy, OnInit } from '@angular/core';
import { Subscription } from 'rxjs';

@Component({
  selector: 'app-loading-page',
  templateUrl: './loading-page.component.html',
  styleUrls: ['./loading-page.component.scss']
})
export class LoadingPageComponent implements OnInit, OnDestroy {

  loading = false;
  loadingSubscription: Subscription;

  constructor(private loadingService: LoadingService) { }

  ngOnInit(): void {
    console.log(true);
    this.loadingSubscription = this.loadingService.loadingStatus.subscribe(
      (value) => { this.loading = value; }
    );
  }

  ngOnDestroy(): void {
    this.loadingSubscription.unsubscribe();
  }

}
