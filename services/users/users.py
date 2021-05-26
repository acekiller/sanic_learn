import sanic
from sanic import Blueprint
from sanic.request import Request
from sanic.response import text
from . import user_v1

user_group = Blueprint.group(user_v1.user_v1)
