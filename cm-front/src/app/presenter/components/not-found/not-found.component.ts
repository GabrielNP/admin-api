import { Component } from '@angular/core';
import { Router } from '@angular/router';

import { TemplateComponent } from '../template/template.component';


@Component({
  standalone: true,
  selector: 'app-not-found',
  templateUrl: './not-found.component.html',
  styleUrls: ['./not-found.component.scss'],
  imports: [TemplateComponent]
})
export class NotFoundComponent {
  constructor(private route: Router) {}

  public restart() {
    this.route.navigate([""]);
  }
}
