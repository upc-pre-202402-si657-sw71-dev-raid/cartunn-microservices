from fastapi import FastAPI, Request
import requests
from pydantic import BaseModel 
app = FastAPI()

# Microservicios URLs
MICROSERVICE_IAM_URL = "http://localhost:8080/api/v1/authentication"
MICROSERVICE_TUNNING_URL = "http://localhost:8080/api/v1/tunning-task"
MICROSERVICE_PURCHASING_URL = "http://localhost:8080/api/v1/orders"

@app.get("/service-tunning/")
async def route_to_service_tunning(request: Request):
    url = f"{MICROSERVICE_TUNNING_URL}"
    response = requests.get(url, headers=request.headers)
    return response.json()

class TunningTask(BaseModel):
    modifiedPart: str
    date: str
    status: str

@app.post("/service-tunning/")
async def route_to_service_tunning(request: Request, tunning_task: TunningTask):
    url = f"{MICROSERVICE_TUNNING_URL}"
    response = requests.post(url, headers=request.headers, json=tunning_task.dict())
    return response.json()

@app.get("/orders/")
async def route_to_service_purchasing(request: Request):
    url = f"{MICROSERVICE_PURCHASING_URL}"
    response = requests.get(url, headers=request.headers)
    return response.json()

class Order(BaseModel):
    name: str
    description: str
    code: int
    entryDate: str
    exitDate: str
    status: str

@app.post("/orders/")
async def route_to_service_purchasing(request: Request, order: Order):
    url = f"{MICROSERVICE_PURCHASING_URL}"
    response = requests.post(url, headers=request.headers, json=order.dict())
    return response.json()
