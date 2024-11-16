import { Component, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'transactions-card',
  templateUrl: './Gallery-card.component.html',
  styleUrls: ['./Gallery-card.component.scss'],
  encapsulation: ViewEncapsulation.None,
  host: {
    '[class.Gallery-card]': 'true'
  }
})

export class GalleryCardComponent {


}