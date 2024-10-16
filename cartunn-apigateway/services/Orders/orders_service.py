from fastapi import APIRouter, Request
import requests
from configs.url_services import MICROSERVICE_PURCHASING_URL
from models.Order import Order

orders_router =  APIRouter()

@orders_router.get("/orders/")
async def route_to_service_purchasing(request: Request):
    url = f"{MICROSERVICE_PURCHASING_URL}"
    response = requests.get(url, headers=request.headers)
    return response.json()

@orders_router.post("/orders/")
async def route_to_service_purchasing(request: Request, order: Order):
    url = f"{MICROSERVICE_PURCHASING_URL}"
    response = requests.post(url, headers=request.headers, json=order.dict())
    return response.json()