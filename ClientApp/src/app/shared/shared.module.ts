import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { LayoutComponent } from './layout/layout.component';
import { ToolbarComponent } from './toolbar/toolbar.component';
import { MenuComponent } from './menu/menu.component';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { RouterModule } from '@angular/router';
import { MaterialSharedModule } from './material-shared/material-shared.module';
import { HomeComponent } from './home/home.component';
import { EmptySetNullDirective } from './helpers/empty-set-null.directive';

@NgModule({
  declarations: [LayoutComponent, ToolbarComponent, MenuComponent, HomeComponent, EmptySetNullDirective],
  imports: [
    CommonModule,
    RouterModule,
    FormsModule,
    ReactiveFormsModule,
    MaterialSharedModule
  ],
  exports: [
    CommonModule,
    RouterModule,
    FormsModule,
    ReactiveFormsModule,
    MaterialSharedModule,
    EmptySetNullDirective
  ]
})
export class SharedModule { }
