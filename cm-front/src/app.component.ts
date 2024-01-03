import { Component } from "@angular/core";

import { TemplateComponent } from "app/presenter/components/template/template.component";

@Component({
  selector: "app-root",
  standalone: true,
  imports: [TemplateComponent],
  templateUrl: "./app.component.html",
  styleUrls: ["./app.component.scss"]
})
export class AppComponent {
  title = "Canto de Maria Admin";
}
