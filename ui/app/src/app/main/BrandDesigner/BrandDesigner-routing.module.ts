import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { BrandDesignerHomeComponent } from './home/BrandDesigner-home.component';
import { BrandDesignerNewComponent } from './new/BrandDesigner-new.component';
import { BrandDesignerDetailComponent } from './detail/BrandDesigner-detail.component';

const routes: Routes = [
  {path: '', component: BrandDesignerHomeComponent},
  { path: 'new', component: BrandDesignerNewComponent },
  { path: ':id', component: BrandDesignerDetailComponent,
    data: {
      oPermission: {
        permissionId: 'BrandDesigner-detail-permissions'
      }
    }
  }
];

export const BRANDDESIGNER_MODULE_DECLARATIONS = [
    BrandDesignerHomeComponent,
    BrandDesignerNewComponent,
    BrandDesignerDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class BrandDesignerRoutingModule { }