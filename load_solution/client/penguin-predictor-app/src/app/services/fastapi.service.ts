import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { TrainParams } from '../models/trainParams';
import { Penguin } from '../models/penguin';

@Injectable({
  providedIn: 'root'
})
export class FastApiService {

  private _http: HttpClient;
  private _baseUrl: string;

  constructor(http: HttpClient) {
    this._http = http;
    this._baseUrl = "http://127.0.0.1:8000"
  }

  public train(trainParams: TrainParams): Observable<any> {
    return this._http.post<TrainParams>(this._baseUrl + '/train', trainParams);
  }

  public getAccuracy(): Observable<number> {
    return this._http.get<number>(this._baseUrl + '/accuracy');
  }

  public predict(data: Penguin): Observable<string> {
    return this._http.post<string>(this._baseUrl + '/predict', data);
  }
}
