import { NgModule } from "@angular/core";
import { RouterModule, Routes } from "@angular/router";

import { NotFoundComponent } from "./app/presenter/components/not-found/not-found.component";
import { TemplateComponent } from "./app/presenter/components/template/template.component";


const routes: Routes = [
  { path: "login", loadChildren: () => import("./app/presenter/views/login/login.module").then(m => m.LoginModule), canActivate: [] },
  {
    path: "", component: TemplateComponent, children: [
      { path: "", redirectTo: "/home", pathMatch: "full" },
      { path: "home", loadChildren: () => import("./app/presenter/views/home/home.module").then(m => m.HomeModule), canActivate: []},
      { path: "users", loadChildren: () => import("./app/presenter/views/user/user.module").then(m => m.UserModule), canActivate: []},
    ]
  },
  { path: '**', component: NotFoundComponent }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { };
