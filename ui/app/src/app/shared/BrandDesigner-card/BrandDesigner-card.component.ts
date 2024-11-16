import { Component, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'transactions-card',
  templateUrl: './BrandDesigner-card.component.html',
  styleUrls: ['./BrandDesigner-card.component.scss'],
  encapsulation: ViewEncapsulation.None,
  host: {
    '[class.BrandDesigner-card]': 'true'
  }
})

export class BrandDesignerCardComponent {


}