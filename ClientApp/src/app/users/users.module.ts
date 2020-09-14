import { SharedModule } from './../shared/shared.module';
import { NgModule } from '@angular/core';
import { UsersRoutingModule } from './users-routing.module';
import { UsersListComponent } from './users-list/users-list.component';
import { UserDetailComponent } from './user-detail/user-detail.component';

@NgModule({
  declarations: [UsersListComponent, UserDetailComponent],
  imports: [
    UsersRoutingModule,
    SharedModule
  ],
  entryComponents: [UserDetailComponent]
})
export class UsersModule { }
