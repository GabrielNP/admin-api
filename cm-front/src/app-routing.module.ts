import { NgModule } from "@angular/core";
import { RouterModule, Routes } from "@angular/router";
import { TemplateComponent } from "./app/presenter/components/template/template.component";

const routes: Routes = [
  { path: "login", loadChildren: () => import("./app/presenter/views/login/login.module").then(m => m.LoginModule), canActivate: [] },
  {
    path: "", component: TemplateComponent, children: [
      { path: "", redirectTo: "/home", pathMatch: "full" },
      { path: "home", loadChildren: () => import("./app/presenter/views/home/home.module").then(m => m.HomeModule), canActivate: []},
    ]
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { };
