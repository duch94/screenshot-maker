from typing import AsyncGenerator

from pyppeteer import launch

from logger import get_logger

logger = get_logger(__name__)


async def make_screenshot(url: str, css_selector: str) -> AsyncGenerator[bytes, None]:
    args = {
        "headless": True,
    }
    browser = await launch(args)
    page = await browser.newPage()
    logger.info("Browser have been loaded with args %s." % str(args))
    await page.goto(url)
    logger.info("Page %s have been loaded." % url)
    object_to_shot = await page.querySelector(css_selector)
    logger.info("Element with css_selector='%s' have been selected." % css_selector)
    screenshot = await object_to_shot.screenshot()
    logger.info("Screenshot have been made.")
    yield screenshot
