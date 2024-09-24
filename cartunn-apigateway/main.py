from fastapi import FastAPI, Request
import requests
from pydantic import BaseModel 
app = FastAPI()

# Microservicios URLs
MICROSERVICE_TUNNING_URL = "http://localhost:8080/api/v1/tunning-task"

@app.get("/service-tunning/{path:path}")
async def route_to_service_tunning(path: str, request: Request):
    url = f"{MICROSERVICE_TUNNING_URL}"
    # Enviar la solicitud al microservicio A
    response = requests.get(url, headers=request.headers)
    return response.json()

class TunningTask(BaseModel):
    modifiedPart: str
    date: str
    status: str

@app.post("/service-tunning/{path:path}")
async def route_to_service_tunning(path: str, request: Request, tunning_task: TunningTask):
    url = f"{MICROSERVICE_TUNNING_URL}"
    # Enviar la solicitud al microservicio A
    response = requests.post(url, headers=request.headers, json=tunning_task.dict())
    return response.json()
