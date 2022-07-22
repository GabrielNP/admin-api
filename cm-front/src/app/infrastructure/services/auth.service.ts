import { HttpClient } from "@angular/common/http"
import { Injectable } from "@angular/core";
import { Observable } from "rxjs";

import { Auth } from "src/app/domain/auth/auth.interface";
import { environment } from "src/environments/environment";
import { LoginRequestModel, LoginResponseModel } from "../models/auth";


@Injectable({ providedIn: "root" })
export class AuthImpl implements Auth {
    private url: string;

    constructor(private httpClient: HttpClient) {
        this.url = environment.apiHost + "/auth";
    }

    public login(body: LoginRequestModel): Observable<LoginResponseModel> {
        return this.httpClient.post<LoginResponseModel>(this.url, body);
    }
}
