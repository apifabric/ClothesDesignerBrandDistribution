import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { DesignerHomeComponent } from './home/Designer-home.component';
import { DesignerNewComponent } from './new/Designer-new.component';
import { DesignerDetailComponent } from './detail/Designer-detail.component';

const routes: Routes = [
  {path: '', component: DesignerHomeComponent},
  { path: 'new', component: DesignerNewComponent },
  { path: ':id', component: DesignerDetailComponent,
    data: {
      oPermission: {
        permissionId: 'Designer-detail-permissions'
      }
    }
  },{
    path: ':designer_id/BrandDesigner', loadChildren: () => import('../BrandDesigner/BrandDesigner.module').then(m => m.BrandDesignerModule),
    data: {
        oPermission: {
            permissionId: 'BrandDesigner-detail-permissions'
        }
    }
}
];

export const DESIGNER_MODULE_DECLARATIONS = [
    DesignerHomeComponent,
    DesignerNewComponent,
    DesignerDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class DesignerRoutingModule { }