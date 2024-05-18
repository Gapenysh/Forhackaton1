import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { Landmark } from './landmark.interface';

@Injectable({
  providedIn: 'root'
})
export class LandmarkService {
  [x: string]: any;
  private apiUrl = 'http://192.168.1.238:5000';

  constructor(private http: HttpClient) { }

  getVideoUrl(landmarkId: number): Observable<string> {
    const url = `${this.apiUrl}/${landmarkId}/video`;
    return this.http.get<string>(url);
  }
}