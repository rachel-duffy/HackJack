import { Routes } from '@angular/router';
import {Homepage} from './homepage/homepage';
import {Play} from './play/play';

export const routes: Routes = [
  { path: '', component: Homepage },
  { path: 'play', component: Play}
];
