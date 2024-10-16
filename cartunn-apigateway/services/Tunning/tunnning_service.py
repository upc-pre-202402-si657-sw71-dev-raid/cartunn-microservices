from fastapi import APIRouter, Request
import requests
from configs.url_services import MICROSERVICE_TUNNING_URL
from models.TunningTask import TunningTask

tunning_router =  APIRouter()

@tunning_router.get("/service-tunning/")
async def route_to_service_tunning(request: Request):
    url = f"{MICROSERVICE_TUNNING_URL}"
    response = requests.get(url, headers=request.headers)
    return response.json()


@tunning_router.post("/service-tunning/")
async def route_to_service_tunning(request: Request, tunning_task: TunningTask):
    url = f"{MICROSERVICE_TUNNING_URL}"
    response = requests.post(url, headers=request.headers, json=tunning_task.dict())
    return response.json()