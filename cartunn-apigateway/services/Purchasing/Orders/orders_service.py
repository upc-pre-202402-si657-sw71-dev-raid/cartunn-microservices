from fastapi import APIRouter, Request
import requests
from configs.url_services import MICROSERVICE_PURCHASING_URL
from models.Order import Order

orders_router =  APIRouter(
)

# Get all
@orders_router.get("/orders/")
async def route_to_service_purchasing(request: Request):
    url = f"{MICROSERVICE_PURCHASING_URL}/orders"
    response = requests.get(url, headers=request.headers)
    return response.json()

# Get by OrderID
@orders_router.get("/orders/{order_id}")
async def route_to_service_purchasing(request: Request, order_id: int):
    url = f"{MICROSERVICE_PURCHASING_URL}/orders/{order_id}"
    response = requests.get(url, headers=request.headers)
    return response.json()

# Put by orderID
@orders_router.put("/orders/{order_id}")
async def put_order_by_order_id(request: Request, order_id: int):
    url = f"{MICROSERVICE_PURCHASING_URL}/orders/{order_id}"
    response = requests.put(url, headers=request.headers)
    return response.json()

# Delete by Order ID
@orders_router.delete("/orders/{order_id}")
async def delete_order_by_order_id(request: Request, order_id: int):
    url = f"{MICROSERVICE_PURCHASING_URL}/orders/{order_id}"
    response = requests.delete(url, headers=request.headers)
    return response.json()

@orders_router.post("/orders/")
async def route_to_service_purchasing(request: Request, order: Order):
    url = f"{MICROSERVICE_PURCHASING_URL}/orders"
    response = requests.post(url, headers=request.headers, json=order.model_dump())
    return response.json()