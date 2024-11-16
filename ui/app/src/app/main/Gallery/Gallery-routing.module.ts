import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { GalleryHomeComponent } from './home/Gallery-home.component';
import { GalleryNewComponent } from './new/Gallery-new.component';
import { GalleryDetailComponent } from './detail/Gallery-detail.component';

const routes: Routes = [
  {path: '', component: GalleryHomeComponent},
  { path: 'new', component: GalleryNewComponent },
  { path: ':id', component: GalleryDetailComponent,
    data: {
      oPermission: {
        permissionId: 'Gallery-detail-permissions'
      }
    }
  },{
    path: ':gallery_id/Event', loadChildren: () => import('../Event/Event.module').then(m => m.EventModule),
    data: {
        oPermission: {
            permissionId: 'Event-detail-permissions'
        }
    }
}
];

export const GALLERY_MODULE_DECLARATIONS = [
    GalleryHomeComponent,
    GalleryNewComponent,
    GalleryDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class GalleryRoutingModule { }