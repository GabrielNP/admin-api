import { Injectable } from "@angular/core";
import { LoginRequestModel } from "src/app/infrastructure/models/auth";

import { AuthImpl } from "src/app/infrastructure/services/auth.service";


@Injectable({ providedIn: "root" })
export class Login {
    constructor(private authImpl: AuthImpl) {}

    public async login(body: LoginRequestModel) {
        return await this.authImpl.login(body).subscribe()
    }
}
