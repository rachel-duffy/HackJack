import { Component, signal } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import {MatToolbarModule} from '@angular/material/toolbar';
import {Header} from './utils/header/header';

@Component({
  selector: 'app-root',
  imports: [RouterOutlet, MatToolbarModule, Header],
  templateUrl: './app.html',
  styleUrl: './app.scss'
})
export class App {
  protected readonly title = signal('HackJack');
}
