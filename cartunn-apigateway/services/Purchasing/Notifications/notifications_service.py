from fastapi import APIRouter, Request
import requests
from configs.url_services import MICROSERVICE_PURCHASING_URL
from models.NotificationResource import NotificationResource

notifications_router =  APIRouter()

# get by notification id
@notifications_router.get("/notifications/{notification_id}")
async def get_notification_by_id(requests: Request, notification_id: int):
    url = f"{MICROSERVICE_PURCHASING_URL}/{notification_id}"
    response = requests.get(url, headers=requests.request.headers)
    return response.json()

@notifications_router.put("/notifications/{notification_id}")
async def put_notification_by_id(requests: Request, notification_id: int):
    url = f"{MICROSERVICE_PURCHASING_URL}/{notification_id}"
    response = requests.put(url, headers=requests.request.headers)
    return response.json()


@notifications_router.delete("/notifications/{notification_id}")
async def delete_notification_by_id(requests: Request, notification_id: int):
    url = f"{MICROSERVICE_PURCHASING_URL}/{notification_id}"
    response = requests.delete(url, headers=requests.request.headers)
    return response.json()


@notifications_router.get("/notifications")
async def get_all_notifications(requests: Request):
    url = f"{MICROSERVICE_PURCHASING_URL}"
    response = requests.get(url, headers=requests.request.headers)
    return response.json()

@notifications_router.post("/notifications")
async def post_a_notifications(requests: Request, notification: NotificationResource ):
    url = f"{MICROSERVICE_PURCHASING_URL}"
    response = requests.post(url, headers=requests.request.headers, json=notification.model_dump())
    return response.json()

@notifications_router.post("/orders/{order_id}/notifications")
async def post_a_notifications(requests: Request, order_id: int):
    url = f"{MICROSERVICE_PURCHASING_URL}/orders/{order_id}/notifications"
    response = requests.post(url, headers=requests.request.headers)
    return response.json()
