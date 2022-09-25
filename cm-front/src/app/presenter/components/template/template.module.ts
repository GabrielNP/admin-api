import { NgModule } from "@angular/core";
import { RouterModule } from "@angular/router";
import { MaterialModule } from "../modules/material.module";

import { TemplateComponent } from "./template.component";


@NgModule({
    declarations: [
        TemplateComponent
    ],
    imports: [
        RouterModule,
        MaterialModule
    ],
})
export class TemplateModule {};
