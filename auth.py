from fastapi import APIRouter

model_auth = APIRouter(prefix="/auth")


@model_auth.get("/")
async def auth():
    return {
        "massage": "Auth page"
    }


@model_auth.get('/register')
async def register():
    return {
        "massage": "This is register page"
    }


@model_auth.get("/login")
async def login():
    return {
        "massage": "This is login page"
    }


@model_auth.get("/log_out")
async def lot_out():
    return {
        "massage": "This is log out page"
    }
