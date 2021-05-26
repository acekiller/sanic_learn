# coding: utf-8
"""
"""
from operator import mul
import server_config
import multiprocessing
import os
from re import template
from sanic import Sanic, request, response, text
import sanic
from sanic.log import logger
from sanic import Request
from sanic import html
from jinja2 import Environment, PackageLoader

app = Sanic(server_config.app_name)
app.config["APP_NAME"] = server_config.app_name
app.config.update_config({"DB_NAME":server_config.db_name})
app.config.update({"DB_USER":"db_user"})

from services.users import user_group
from services import article

env = Environment(
    loader=PackageLoader(server_config.templates_name, package_path=os.path.join(os.getcwd(), server_config.templates_name)),
     enable_async=True)

@app.route("/")
async def index(request: Request):
    print(app.config["APP_NAME"] + " " + app.config["DB_NAME"] + " " + app.config["DB_USER"])
    # request.cookies['test'] = 'It worked!'
    # request.cookies['test']['domain'] = '.gotta-go-fast.com'
    # request.cookies['test']['httponly'] = True
    return response.json({
        "parsed": True,
        "url": request.url,
        "query_string": request.query_string,
        "args": request.args,
        "query_args": request.query_args,
        # "cookies_value": "{}".format(request.cookies.get("test"))
    })

app.blueprint(user_group)
app.blueprint(article.article_service)

if __name__ == "__main__":
    app.run(port=8080)