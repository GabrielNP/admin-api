import { Component, OnInit } from "@angular/core";

@Component({
  selector: "app-template",
  templateUrl: "./template.component.html",
  styleUrls: ["./template.component.scss"]
})
export class TemplateComponent implements OnInit {
  public menuBar: boolean = false;

  constructor() { }

  ngOnInit(): void {
  }

  public toggleMenu() {
    this.menuBar = !this.menuBar
    console.log(this.menuBar);
  }
}
