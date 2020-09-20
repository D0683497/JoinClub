import { UserService } from '../../services/user/user.service';
import { ScanResultComponent } from '../scan-result/scan-result.component';
import { Component, OnInit } from '@angular/core';
import { MatDialog } from '@angular/material/dialog';
import { MatSnackBar } from '@angular/material/snack-bar';
import { BehaviorSubject, forkJoin } from 'rxjs';

@Component({
  selector: 'app-check-join',
  templateUrl: './check-join.component.html',
  styleUrls: ['./check-join.component.scss']
})
export class CheckJoinComponent implements OnInit {

  openScanner = false;

  availableDevices: MediaDeviceInfo[];
  currentDevice: MediaDeviceInfo = null;
  hasDevices: boolean;
  hasPermission: boolean;
  torchAvailable$ = new BehaviorSubject<boolean>(false);
  canScan = true;

  constructor(
    private snackBar: MatSnackBar,
    private dialog: MatDialog,
    private userService: UserService) { }

  ngOnInit(): void { }

  onCodeResult(resultString: string): void {
    if (this.canScan) {
      this.canScan = false;
      if (resultString.slice(0, 20) === 'HackerSir-join-code-') { // 格式正確
        const userId = resultString.slice(20);
        this.showResultDialog(userId);
      } else {
        this.canScan = true;
        this.snackBar.open('掃描失敗', '關閉', { duration: 3000 });
      }
    }
  }

  showResultDialog(userId: string): void {
    const userDataOberserval = this.userService.getUserById(userId);
    const roleDataOberserval = this.userService.getUserRoleById(userId);

    forkJoin([userDataOberserval, roleDataOberserval]).subscribe(
      results => {
        const dialogRef = this.dialog.open(ScanResultComponent, {
          data: { user: results[0], role: results[1][0] }
        });
        dialogRef.afterClosed().subscribe(() => {
          this.canScan = true;
        });
      },
      error => {
        this.canScan = true;
        this.snackBar.open('發生錯誤', '關閉', { duration: 3000 });
      }
    );
  }

  onCamerasFound(devices: MediaDeviceInfo[]): void {
    this.availableDevices = devices;
    this.hasDevices = Boolean(devices && devices.length);
  }

  // 更換裝置(鏡頭)
  onDeviceSelectChange(selected: string): void {
    const device = this.availableDevices.find(x => x.deviceId === selected);
    this.currentDevice = device || null;
  }

  onHasPermission(has: boolean): void {
    this.hasPermission = has;
  }

  onTorchCompatible(isCompatible: boolean): void {
    this.torchAvailable$.next(isCompatible || false);
  }

}
