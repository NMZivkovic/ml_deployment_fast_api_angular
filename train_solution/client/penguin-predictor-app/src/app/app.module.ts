import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppComponent } from './app.component';
import { FormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';
import { RouterModule } from '@angular/router';
import { routerConfig } from './config/router-config';
import { PredictComponent } from './components/predict/predict.component';
import { TrainComponent } from './components/train/train.component';
import { ReactiveFormsModule} from '@angular/forms'

@NgModule({
  declarations: [
    AppComponent,
    PredictComponent,
    TrainComponent
  ],
  imports: [
    BrowserModule,
    FormsModule,
    HttpClientModule,
    ReactiveFormsModule,
    RouterModule.forRoot(routerConfig)
  ],
  providers: [],
  bootstrap: [
    AppComponent
  ]
})
export class AppModule { }
