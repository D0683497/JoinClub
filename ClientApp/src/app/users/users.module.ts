import { SharedModule } from './../shared/shared.module';
import { NgModule } from '@angular/core';
import { UsersRoutingModule } from './users-routing.module';
import { UsersListComponent } from './users-list/users-list.component';

@NgModule({
  declarations: [UsersListComponent],
  imports: [
    UsersRoutingModule,
    SharedModule
  ]
})
export class UsersModule { }
