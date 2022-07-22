export interface LoginResponseModel {
    user_id: string
    access_token: string
    refresh_token: string
    admin: boolean
    roles: any[]
}

export interface LoginRequestModel {
    email: string
    password: string
}
