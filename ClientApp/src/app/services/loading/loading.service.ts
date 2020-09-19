import { LoadingPageComponent } from './../../shared/loading-page/loading-page.component';
import { Injectable } from '@angular/core';
import { MatDialog } from '@angular/material/dialog';
import { Subject } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class LoadingService {

  // tslint:disable-next-line: variable-name
  private _loading = false;
  loadingStatus: Subject<boolean> = new Subject();
  dialogId: string;

  constructor(private dialog: MatDialog) { }

  get loading(): boolean {
    return this._loading;
  }

  set loading(value: boolean) {
    this._loading = value;
    this.loadingStatus.next(value);
  }

  startLoading(): void {
    this.loading = true;
    const dialogRef = this.dialog.open(LoadingPageComponent, {
      disableClose: true
    });
    this.dialogId = dialogRef.id;
  }

  stopLoading(): void {
    this.loading = false;
    this.dialog.getDialogById(this.dialogId).close();
  }

}
