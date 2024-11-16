import {CUSTOM_ELEMENTS_SCHEMA, NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { OntimizeWebModule } from 'ontimize-web-ngx';
import { SharedModule } from '../../shared/shared.module';
import  {GALLERY_MODULE_DECLARATIONS, GalleryRoutingModule} from  './Gallery-routing.module';

@NgModule({

  imports: [
    SharedModule,
    CommonModule,
    OntimizeWebModule,
    GalleryRoutingModule
  ],
  declarations: GALLERY_MODULE_DECLARATIONS,
  exports: GALLERY_MODULE_DECLARATIONS,
  schemas: [CUSTOM_ELEMENTS_SCHEMA]
})
export class GalleryModule { }