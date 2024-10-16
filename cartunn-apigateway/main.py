from fastapi import FastAPI, HTTPException, Request
import requests
from pydantic import BaseModel 
app = FastAPI()

PUBLIC_URLS = ["/docs", "/authentication", "/openapi.json"]

# Microservicios URLs
MICROSERVICE_IAM_URL = "http://localhost:8080/api/v1/authentication"
MICROSERVICE_TUNNING_URL = "http://localhost:8081/api/v1/tunning-task"
MICROSERVICE_PURCHASING_URL = "http://localhost:8080/api/v1/orders"


async def is_token_valid(token: str) -> bool:
    """
    Validates a given token by sending a request to the IAM microservice.

    Args:
        token (str): The token to be validated.

    Returns:
        bool: True if the token is valid, False otherwise.
    """
    response = requests.post(f"{MICROSERVICE_IAM_URL}/validate-token", json={"token": token})
    print(response.json())
    if response.status_code == 200:
        if response.json().get("valid") == True:
            return True
    return False



@app.middleware("http")
async def check_token(request: Request, call_next):
    """
    Middleware to check the validity of the token in the HTTP request.
    This middleware intercepts incoming HTTP requests and checks if the request URL is in the list of public URLs.
    If the URL is public, the request is passed through without further checks.
    For non-public URLs, it checks for the presence of an Authorization header with a Bearer token.
    If the token is present, it validates the token using the `is_token_valid` function.
    If the token is missing or invalid, an HTTP 401 Unauthorized exception is raised.
    Args:
        request (Request): The incoming HTTP request.
        call_next (function): The next middleware or route handler to be called.
    Returns:
        Response: The HTTP response after processing the middleware and route handler.
    Raises:
        HTTPException: If the token is missing or invalid, an HTTP 401 Unauthorized exception is raised.
    """
    if request.url.path in PUBLIC_URLS:
        response = await call_next(request)
        return response

    token = request.headers.get("Authorization")
    if token and token.startswith("Bearer "):
        token = token.split("Bearer ")[1]
        if not await is_token_valid(token):
            raise HTTPException(status_code=401, detail="Invalid token")
    else:
        raise HTTPException(status_code=401, detail="Token is missing or invalid")
    
    response = await call_next(request)
    return response

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
