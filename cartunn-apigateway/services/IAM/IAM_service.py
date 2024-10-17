from fastapi import APIRouter, Request
import requests
from configs.url_services import MICROSERVICE_IAM_URL
from services.IAM.models.SignInRequest import SignInRequest
from services.IAM.models.SignUpRequest import SignUpRequest


iam_router =  APIRouter(
)

@iam_router.post("/sign-in")
async def sign_in(request: Request, signInRequest: SignInRequest):
    url = f"{MICROSERVICE_IAM_URL}/sign-in"
    response = requests.post(url, headers=request.headers, json=signInRequest.model_dump())
    return response.json()

@iam_router.post("/sign-up")
async def sign_in(request: Request, signInRequest: SignUpRequest):
    url = f"{MICROSERVICE_IAM_URL}/sign-up"
    response = requests.post(url, headers=request.headers, json=signInRequest.model_dump())
    return response.json()