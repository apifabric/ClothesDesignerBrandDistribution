import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { BrandHomeComponent } from './home/Brand-home.component';
import { BrandNewComponent } from './new/Brand-new.component';
import { BrandDetailComponent } from './detail/Brand-detail.component';

const routes: Routes = [
  {path: '', component: BrandHomeComponent},
  { path: 'new', component: BrandNewComponent },
  { path: ':id', component: BrandDetailComponent,
    data: {
      oPermission: {
        permissionId: 'Brand-detail-permissions'
      }
    }
  },{
    path: ':brand_id/BrandDesigner', loadChildren: () => import('../BrandDesigner/BrandDesigner.module').then(m => m.BrandDesignerModule),
    data: {
        oPermission: {
            permissionId: 'BrandDesigner-detail-permissions'
        }
    }
},{
    path: ':brand_id/Collection', loadChildren: () => import('../Collection/Collection.module').then(m => m.CollectionModule),
    data: {
        oPermission: {
            permissionId: 'Collection-detail-permissions'
        }
    }
},{
    path: ':brand_id/SupplyOrder', loadChildren: () => import('../SupplyOrder/SupplyOrder.module').then(m => m.SupplyOrderModule),
    data: {
        oPermission: {
            permissionId: 'SupplyOrder-detail-permissions'
        }
    }
}
];

export const BRAND_MODULE_DECLARATIONS = [
    BrandHomeComponent,
    BrandNewComponent,
    BrandDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class BrandRoutingModule { }