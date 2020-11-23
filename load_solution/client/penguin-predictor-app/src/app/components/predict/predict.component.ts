import { Component} from '@angular/core';
import { FormBuilder, FormGroup, FormArray, FormControl, ValidatorFn } from '@angular/forms';
import { Penguin } from '../../models/penguin';
import {FastApiService} from '../../services/fastapi.service';

@Component({
  selector: 'predict-component',
  templateUrl: './predict.component.html',
  styleUrls: ['./predict.component.css']
})

export class PredictComponent {
  islands: string[] = ['Torgersen', 'Dream', 'Biscoe'];
  sexes: string[] = ['FEMALE', 'MALE'];
  spicies: string[] = ['Adelie', 'Chinstrap', 'Gentoo'];

  prediction = this.spicies[0];
  penguin = new Penguin(this.islands[0], 0, 0, 0, 0, this.sexes[0], this.spicies[0]);

  constructor(
    private _fastApiService: FastApiService,
  ) {
  }

  public onPredict(): void {
    this._fastApiService.predict(this.penguin).subscribe(
      response => this.prediction = response
    );
  }
}
