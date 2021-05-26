from sanic import Blueprint
from sanic import Request
from sanic.response import json

article_service = Blueprint(name="article", url_prefix="article")

@article_service.route("article_list")
async def article_list(request: Request):
    return json({"title": "article_list"})
