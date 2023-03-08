import { Component } from '@angular/core';
import { Router } from '@angular/router';

import { TemplateModule } from '../template/template.module';


@Component({
  standalone: true,
  selector: 'app-not-found',
  templateUrl: './not-found.component.html',
  styleUrls: ['./not-found.component.scss'],
  imports: [TemplateModule]
})
export class NotFoundComponent {
  constructor(private route: Router) {}

  public restart() {
    this.route.navigate([""]);
  }
}
