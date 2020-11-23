import { TrainComponent } from '../components/train/train.component';
import { PredictComponent } from '../components/predict/predict.component';
import { Routes } from '@angular/router';

export const routerConfig: Routes = [
    {
        path: 'load',
        component: TrainComponent
    },
    {
        path: 'predict',
        component: PredictComponent
    },
    { path: '**', redirectTo: '/load', pathMatch: 'full' }
];
