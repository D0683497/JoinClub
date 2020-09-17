import { SharedModule } from './../shared/shared.module';
import { NgModule } from '@angular/core';

import { AccountRoutingModule } from './account-routing.module';
import { LoginComponent } from './login/login.component';
import { RegisterComponent } from './register/register.component';
import { ChangePasswordComponent } from './change-password/change-password.component';
import { ProfileComponent } from './profile/profile.component';


@NgModule({
  declarations: [LoginComponent, RegisterComponent, ChangePasswordComponent, ProfileComponent],
  imports: [
    AccountRoutingModule,
    SharedModule
  ]
})
export class AccountModule { }
