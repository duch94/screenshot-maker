from aiohttp import web

from screenshot_maker import make_screenshot
from logger import get_logger

logger = get_logger(__name__)


async def get_screenshot(request: web.Request):
    date_start = request.match_info.get("date_start")
    date_end = request.match_info.get("date_end")
    logger.info("Received request: date_start=%s, date_end=%s" % (date_start, date_end))
    url = "https://yandex.ru/search/?text=%s_%s" % (date_start, date_end)
    css_sel = "html"
    logger.info("Started taking screenshot for url %s with selector %s." % (url, css_sel))
    screenshot = make_screenshot(url, css_sel)
    return web.Response(body=screenshot)


async def app_factory():
    app = web.Application()
    app.add_routes([web.get("/get_screenshot/{date_start}_{date_end}.png", get_screenshot)])
    logger.info("Application have been started.")
    return app


if __name__ == "__main__":
    app = app_factory()
    web.run_app(app)
