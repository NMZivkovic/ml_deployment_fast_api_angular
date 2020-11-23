import { Component} from '@angular/core';
import { TrainParams } from '../../models/trainParams';
import {FastApiService} from '../../services/fastapi.service';

@Component({
  selector: 'train-component',
  templateUrl: './train.component.html',
  styleUrls: ['./train.component.css']
})
export class TrainComponent {
  models: string[] = ['SVM', 'Decision Tree', 'Random Forest', 'Logistic Regression'];
  modelLoaded = false;
  trainParams = new TrainParams(this.models[0], './data/penguins_size.csv', 0.2);

  constructor(
    private _fastApiService: FastApiService,
  ) {
  }

  public onTrainClick(): void {
    console.log(this.trainParams);
    this._fastApiService.train(this.trainParams).subscribe(
      _ => this.modelLoaded = true
    );
  }
}
