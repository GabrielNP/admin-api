import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { MatIconModule } from '@angular/material/icon';
import { MatToolbarModule } from '@angular/material/toolbar';
import { MatSidenavModule } from '@angular/material/sidenav';
import { MatListModule } from '@angular/material/list';

const materialModules = [
  MatIconModule,
  MatToolbarModule,
  MatSidenavModule,
  MatListModule
];
  
  @NgModule({
    declarations: [],
    imports: [
      CommonModule,
      ...materialModules
    ],
    exports: [
      ...materialModules
    ]
  })
  export class MaterialModule { }
