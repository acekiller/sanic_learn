from sanic import Blueprint
from sanic.request import Request
from sanic.response import json, text

register_v1 = Blueprint(name="register_v1", url_prefix="/register", version=1)
register = Blueprint.group(register_v1, url_prefix="/user")

@register_v1.get("/")
async def register_welcome(request: Request):
    return text("Welcome")

@register_v1.post("/")
async def register_account(request: Request):
    return json({
        "status": True,
        "user": {
            "id": 1324,
            "name": "fantasy"
        }
    })