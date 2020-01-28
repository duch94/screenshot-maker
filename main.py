from aiohttp import web

from screenshot_maker import make_screenshot


async def get_screenshot(request: web.Request):
    # params = await request.post()
    # ds = params["date_start"]
    # de = params["date_end"]
    date_start = request.match_info.get("date_start")
    date_end = request.match_info.get("date_end")
    url = "https://yandex.ru/search/?text=%s_%s" % (date_start, date_end)
    css_sel = "html"
    screenshot = make_screenshot(url, css_sel)
    return web.Response(body=screenshot)


async def app_factory():
    app = web.Application()
    app.add_routes([web.get("/get_screenshot/{date_start}_{date_end}.png", get_screenshot)])
    return app

if __name__ == "__main__":
    app = app_factory()
    web.run_app(app)