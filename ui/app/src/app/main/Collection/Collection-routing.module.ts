import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { CollectionHomeComponent } from './home/Collection-home.component';
import { CollectionNewComponent } from './new/Collection-new.component';
import { CollectionDetailComponent } from './detail/Collection-detail.component';

const routes: Routes = [
  {path: '', component: CollectionHomeComponent},
  { path: 'new', component: CollectionNewComponent },
  { path: ':id', component: CollectionDetailComponent,
    data: {
      oPermission: {
        permissionId: 'Collection-detail-permissions'
      }
    }
  },{
    path: ':collection_id/Item', loadChildren: () => import('../Item/Item.module').then(m => m.ItemModule),
    data: {
        oPermission: {
            permissionId: 'Item-detail-permissions'
        }
    }
},{
    path: ':collection_id/PurchaseOrder', loadChildren: () => import('../PurchaseOrder/PurchaseOrder.module').then(m => m.PurchaseOrderModule),
    data: {
        oPermission: {
            permissionId: 'PurchaseOrder-detail-permissions'
        }
    }
}
];

export const COLLECTION_MODULE_DECLARATIONS = [
    CollectionHomeComponent,
    CollectionNewComponent,
    CollectionDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class CollectionRoutingModule { }