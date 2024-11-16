import { Component, Injector, ViewChild } from '@angular/core';
import { NavigationService, OFormComponent } from 'ontimize-web-ngx';

@Component({
  selector: 'Gallery-new',
  templateUrl: './Gallery-new.component.html',
  styleUrls: ['./Gallery-new.component.scss']
})
export class GalleryNewComponent {
  @ViewChild("GalleryForm") form: OFormComponent;
  onInsertMode() {
    const default_values = {}
    this.form.setFieldValues(default_values);
  }
  constructor(protected injector: Injector) {
    this.injector.get(NavigationService).initialize();
  }
}