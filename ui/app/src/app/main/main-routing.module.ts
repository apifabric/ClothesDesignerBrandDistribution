import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { MainComponent } from './main.component';

export const routes: Routes = [
  {
    path: '', component: MainComponent,
    children: [
        { path: '', redirectTo: 'home', pathMatch: 'full' },
        { path: 'about', loadChildren: () => import('./about/about.module').then(m => m.AboutModule) },
        { path: 'home', loadChildren: () => import('./home/home.module').then(m => m.HomeModule) },
        { path: 'settings', loadChildren: () => import('./settings/settings.module').then(m => m.SettingsModule) },
      
    
        { path: 'Brand', loadChildren: () => import('./Brand/Brand.module').then(m => m.BrandModule) },
    
        { path: 'BrandDesigner', loadChildren: () => import('./BrandDesigner/BrandDesigner.module').then(m => m.BrandDesignerModule) },
    
        { path: 'Collection', loadChildren: () => import('./Collection/Collection.module').then(m => m.CollectionModule) },
    
        { path: 'Designer', loadChildren: () => import('./Designer/Designer.module').then(m => m.DesignerModule) },
    
        { path: 'Event', loadChildren: () => import('./Event/Event.module').then(m => m.EventModule) },
    
        { path: 'Gallery', loadChildren: () => import('./Gallery/Gallery.module').then(m => m.GalleryModule) },
    
        { path: 'Item', loadChildren: () => import('./Item/Item.module').then(m => m.ItemModule) },
    
        { path: 'PurchaseOrder', loadChildren: () => import('./PurchaseOrder/PurchaseOrder.module').then(m => m.PurchaseOrderModule) },
    
        { path: 'Store', loadChildren: () => import('./Store/Store.module').then(m => m.StoreModule) },
    
        { path: 'Supplier', loadChildren: () => import('./Supplier/Supplier.module').then(m => m.SupplierModule) },
    
        { path: 'SupplyOrder', loadChildren: () => import('./SupplyOrder/SupplyOrder.module').then(m => m.SupplyOrderModule) },
    
        { path: 'Warehouse', loadChildren: () => import('./Warehouse/Warehouse.module').then(m => m.WarehouseModule) },
    
    ]
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class MainRoutingModule { }