from fastapi import APIRouter, Request
from configs.url_services import MICROSERVICE_PURCHASING_URL
from models.Order import Order

notifications_router =  APIRouter()