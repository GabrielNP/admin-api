import { Observable } from "rxjs";

import { LoginRequestModel, LoginResponseModel } from "src/app/infrastructure/models/auth";


export interface Auth {
    login(body: LoginRequestModel): Observable<LoginResponseModel>
}
