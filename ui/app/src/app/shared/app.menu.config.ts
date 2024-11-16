import { MenuRootItem } from 'ontimize-web-ngx';

import { BrandCardComponent } from './Brand-card/Brand-card.component';

import { BrandDesignerCardComponent } from './BrandDesigner-card/BrandDesigner-card.component';

import { CollectionCardComponent } from './Collection-card/Collection-card.component';

import { DesignerCardComponent } from './Designer-card/Designer-card.component';

import { EventCardComponent } from './Event-card/Event-card.component';

import { GalleryCardComponent } from './Gallery-card/Gallery-card.component';

import { ItemCardComponent } from './Item-card/Item-card.component';

import { PurchaseOrderCardComponent } from './PurchaseOrder-card/PurchaseOrder-card.component';

import { StoreCardComponent } from './Store-card/Store-card.component';

import { SupplierCardComponent } from './Supplier-card/Supplier-card.component';

import { SupplyOrderCardComponent } from './SupplyOrder-card/SupplyOrder-card.component';

import { WarehouseCardComponent } from './Warehouse-card/Warehouse-card.component';


export const MENU_CONFIG: MenuRootItem[] = [
    { id: 'home', name: 'HOME', icon: 'home', route: '/main/home' },
    
    {
    id: 'data', name: ' data', icon: 'remove_red_eye', opened: true,
    items: [
    
        { id: 'Brand', name: 'BRAND', icon: 'view_list', route: '/main/Brand' }
    
        ,{ id: 'BrandDesigner', name: 'BRANDDESIGNER', icon: 'view_list', route: '/main/BrandDesigner' }
    
        ,{ id: 'Collection', name: 'COLLECTION', icon: 'view_list', route: '/main/Collection' }
    
        ,{ id: 'Designer', name: 'DESIGNER', icon: 'view_list', route: '/main/Designer' }
    
        ,{ id: 'Event', name: 'EVENT', icon: 'view_list', route: '/main/Event' }
    
        ,{ id: 'Gallery', name: 'GALLERY', icon: 'view_list', route: '/main/Gallery' }
    
        ,{ id: 'Item', name: 'ITEM', icon: 'view_list', route: '/main/Item' }
    
        ,{ id: 'PurchaseOrder', name: 'PURCHASEORDER', icon: 'view_list', route: '/main/PurchaseOrder' }
    
        ,{ id: 'Store', name: 'STORE', icon: 'view_list', route: '/main/Store' }
    
        ,{ id: 'Supplier', name: 'SUPPLIER', icon: 'view_list', route: '/main/Supplier' }
    
        ,{ id: 'SupplyOrder', name: 'SUPPLYORDER', icon: 'view_list', route: '/main/SupplyOrder' }
    
        ,{ id: 'Warehouse', name: 'WAREHOUSE', icon: 'view_list', route: '/main/Warehouse' }
    
    ] 
},
    
    { id: 'settings', name: 'Settings', icon: 'settings', route: '/main/settings'}
    ,{ id: 'about', name: 'About', icon: 'info', route: '/main/about'}
    ,{ id: 'logout', name: 'LOGOUT', route: '/login', icon: 'power_settings_new', confirm: 'yes' }
];

export const MENU_COMPONENTS = [

    BrandCardComponent

    ,BrandDesignerCardComponent

    ,CollectionCardComponent

    ,DesignerCardComponent

    ,EventCardComponent

    ,GalleryCardComponent

    ,ItemCardComponent

    ,PurchaseOrderCardComponent

    ,StoreCardComponent

    ,SupplierCardComponent

    ,SupplyOrderCardComponent

    ,WarehouseCardComponent

];