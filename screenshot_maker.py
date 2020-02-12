import asyncio
import os

from pyppeteer import launch
from pyppeteer.page import Page

from logger import get_logger

logger = get_logger(__name__)
path_to_images = os.path.join("/var", "tmp", "screenshots")


async def make_screenshot(img_id: str, url: str, actions: list):
    args = {
        "headless": True,
    }
    browser = await launch(args)
    page = await browser.newPage()
    logger.info("Browser have been loaded with args %s." % str(args))
    await page.goto(url)
    logger.info("Page %s have been loaded." % url)
    screenshot_path = os.path.join(path_to_images, f"{img_id}.png")
    asyncio.create_task(do_actions(actions=actions, page=page, img_path=screenshot_path))


async def do_actions(actions: list, page: Page, img_path: str):
    for a in actions:
        # === configuring page ===
        if a["action"] == "set_resolution":
            await page.setViewport({
                "width": a["width"],
                "height": a["height"]
            })
        # === actions ===
        if "selector" in a.keys():
            element = await page.querySelector(a["selector"])
            logger.warning("Action have no CSS selector, it contains %s. Skipping..." % str(a))
        else:
            continue
        if a["action"] == "click":
            await element.click()
            logger.info("Element at selector=%s have been clicked." % a["selector"])
        if a["action"] == "write":
            await element.type(a["text"])
            logger.info("Text [%s] have been written at selector=%s" % (a["text"], a["selector"]))
        if a["action"] == "screenshot_element":
            await element.screenshot(path=img_path)
            with open(f"{img_path}.SUCCESS", "w") as file_signal:
                file_signal.write("")
            logger.info("Screenshot at selector=%s have been made." % a["selector"])
