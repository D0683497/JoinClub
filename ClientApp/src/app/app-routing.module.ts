import { LicenseComponent } from './shared/license/license.component';
import { LayoutComponent } from './shared/layout/layout.component';
import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

const routes: Routes = [
  { path: '', loadChildren: () => import('./dashboard/dashboard.module').then(m => m.DashboardModule) },
  {
    path: 'license',
    component: LayoutComponent,
    children: [
      { path: '', component: LicenseComponent }
    ]
  },
  {
    path: 'account',
    component: LayoutComponent,
    children: [
      { path: '', loadChildren: () => import('./account/account.module').then(m => m.AccountModule) }
    ]
  },
  {
    path: 'users',
    component: LayoutComponent,
    children: [
      { path: '', loadChildren: () => import('./users/users.module').then(m => m.UsersModule) }
    ]
  },
  {
    path: 'staff',
    component: LayoutComponent,
    children: [
      { path: '', loadChildren: () => import('./staff/staff.module').then(m => m.StaffModule) }
    ]
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
