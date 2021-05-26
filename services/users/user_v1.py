from sanic import Sanic
from sanic.blueprints import Blueprint
from sanic.request import Request
from sanic.response import json

user_v1 = Blueprint(name="user", url_prefix="/user", version=1)

@user_v1.route("tops")
async def top_users(request: Request):
    return json(
        [{
        "id": 123,
        "name": "fantasy",
        "gender": "M",
    },
    {
        "id": 123,
        "name": "fantasy",
        "gender": "M",
    }]
    )

# @user_v1.get("userinfo/<user:string>")
# async def user_info(request: Request, user: str):
    # return json({
    #     "id": 123,
    #     "name": "fantasy",
    #     "gender": "M",
    # })