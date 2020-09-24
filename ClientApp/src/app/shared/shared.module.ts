import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { LayoutComponent } from './layout/layout.component';
import { ToolbarComponent } from './toolbar/toolbar.component';
import { MenuComponent } from './menu/menu.component';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { RouterModule } from '@angular/router';
import { MaterialSharedModule } from './material-shared/material-shared.module';
import { EmptySetNullDirective } from './helpers/empty-set-null/empty-set-null.directive';
import { FirstLetterUpperDirective } from './helpers/first-letter-upper/first-letter-upper.directive';
import { LicenseComponent } from './license/license.component';
import { LoadingPageComponent } from './loading-page/loading-page.component';

@NgModule({
  declarations: [
    LayoutComponent,
    ToolbarComponent,
    MenuComponent,
    EmptySetNullDirective,
    FirstLetterUpperDirective,
    LicenseComponent,
    LoadingPageComponent
  ],
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
    EmptySetNullDirective,
    FirstLetterUpperDirective
  ],
  entryComponents: [
    LoadingPageComponent
  ]
})
export class SharedModule { }
