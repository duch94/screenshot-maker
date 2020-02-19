from aiohttp import web
import asyncio
import uuid

from screenshot_maker import make_screenshot
from logger import get_logger
from typing import Union
import os
import json

logger = get_logger(__name__)
path_to_images = os.path.join("screenshots")


async def order_screenshot(request: web.Request) -> web.Response:
    try:
        params: dict = await request.json(loads=json.loads)
    except json.decoder.JSONDecodeError as e:
        logger.error("While decoding request error occured: user's payload was [%s]" % e)
        return web.Response(text="Error occured while parsing json.", status=400)
    actions = params["actions"]
    url = params["url"]
    logger.info("Received request: %s" % str(params))
    logger.info("Started taking screenshot for url %s with actions='%s'." % (url, str(actions)))
    img_id = str(uuid.uuid4())
    asyncio.create_task(make_screenshot(img_id, url, actions))
    return web.Response(text=img_id, status=202)


async def download_order(request: web.Request) -> Union[web.FileResponse, web.Response]:
    img_id = request.match_info.get("img_id")
    img_filename = f"{img_id}.png"
    if os.path.exists(os.path.join(path_to_images, f"{img_filename}.SUCCESS")):
        return web.FileResponse(path=os.path.join(path_to_images, img_filename))
    return web.Response(status=102, text="Screenshot making is in progress")


async def app_factory():
    app = web.Application()
    app.add_routes([web.post("/order_screenshot", order_screenshot),
                    web.get("/download_order?img_id={img_id}", download_order)])
    logger.info("Application have been started.")
    return app


if __name__ == "__main__":
    app_for_debug = app_factory()
    web.run_app(app_for_debug)
