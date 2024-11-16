import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { SupplyOrderHomeComponent } from './home/SupplyOrder-home.component';
import { SupplyOrderNewComponent } from './new/SupplyOrder-new.component';
import { SupplyOrderDetailComponent } from './detail/SupplyOrder-detail.component';

const routes: Routes = [
  {path: '', component: SupplyOrderHomeComponent},
  { path: 'new', component: SupplyOrderNewComponent },
  { path: ':id', component: SupplyOrderDetailComponent,
    data: {
      oPermission: {
        permissionId: 'SupplyOrder-detail-permissions'
      }
    }
  }
];

export const SUPPLYORDER_MODULE_DECLARATIONS = [
    SupplyOrderHomeComponent,
    SupplyOrderNewComponent,
    SupplyOrderDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class SupplyOrderRoutingModule { }