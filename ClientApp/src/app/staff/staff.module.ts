import { SharedModule } from '../shared/shared.module';
import { NgModule } from '@angular/core';
import { StaffRoutingModule } from './staff-routing.module';
import { CheckJoinComponent } from './check-join/check-join.component';
import { ZXingScannerModule } from '@zxing/ngx-scanner';
import { ScanResultComponent } from './scan-result/scan-result.component';

@NgModule({
  declarations: [CheckJoinComponent, ScanResultComponent],
  imports: [
    StaffRoutingModule,
    SharedModule,
    ZXingScannerModule
  ],
  entryComponents: [
    ScanResultComponent
  ]
})
export class StaffModule { }
