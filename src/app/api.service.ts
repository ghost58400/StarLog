import {Injectable} from '@angular/core';

import {Observable, of, throwError} from 'rxjs';
import {HttpClient, HttpHeaders, HttpErrorResponse} from '@angular/common/http';
import {catchError, tap, map} from 'rxjs/operators';

const httpOptions = {
  headers: new HttpHeaders({'Content-Type': 'application/json'})
};
const backendUrl = 'http://localhost:5000'; // service REST

@Injectable({
  providedIn: 'root'
})
export class ApiService {
  token = '';

  constructor(private http: HttpClient) {
  }

  private handleError<T>(operation = 'operation', result?: T) {
    return (error: any): Observable<T> => {
// TODO: send the error to remote logging infrastructure
      console.error(error); // log to console instead
// Let the app keep running by returning an empty result.
      return of(result as T);
    };
  }

  signUp(params): Observable<any> {
    return this.http.post(backendUrl+'/signup', params, httpOptions).pipe(
      tap((result:any) =>
        this.token = result.token
      ),
      catchError(this.handleError('signup'))
    );
  }

}

