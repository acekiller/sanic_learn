import sanic
from sanic import Blueprint
from sanic.request import Request
from sanic.response import text
from . import user_service, user_register

user_group = Blueprint.group(user_service.user, user_register.register)
