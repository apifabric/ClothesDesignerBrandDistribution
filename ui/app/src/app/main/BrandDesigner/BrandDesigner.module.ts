import {CUSTOM_ELEMENTS_SCHEMA, NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { OntimizeWebModule } from 'ontimize-web-ngx';
import { SharedModule } from '../../shared/shared.module';
import  {BRANDDESIGNER_MODULE_DECLARATIONS, BrandDesignerRoutingModule} from  './BrandDesigner-routing.module';

@NgModule({

  imports: [
    SharedModule,
    CommonModule,
    OntimizeWebModule,
    BrandDesignerRoutingModule
  ],
  declarations: BRANDDESIGNER_MODULE_DECLARATIONS,
  exports: BRANDDESIGNER_MODULE_DECLARATIONS,
  schemas: [CUSTOM_ELEMENTS_SCHEMA]
})
export class BrandDesignerModule { }