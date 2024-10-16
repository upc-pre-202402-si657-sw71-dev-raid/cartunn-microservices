from fastapi import FastAPI, HTTPException, Request
import requests
from configs.url_publics import PUBLIC_URLS
from configs.url_services import MICROSERVICE_IAM_URL
from services.Purchasing.Orders.orders_service import orders_router
from services.Purchasing.Notifications.notifications_service import notifications_router
from services.Tunning.tunnning_service import tunning_router

app = FastAPI(
    title="Cartunn API Gateway",
    description="API Gateway for the Cartunn application",
    version="0.1",
)

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


app.include_router(orders_router, tags=["Purchasing Microservice"])
app.include_router(notifications_router, tags=["Purchasing Microservice"])
app.include_router(tunning_router, tags=["Tunning Microservice"])
