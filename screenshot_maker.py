from pyppeteer import launch


async def make_screenshot(url: str, css_selector: str) -> bytes:
    browser = await launch(headless=True)
    page = await browser.newPage()
    await page.goto(url)
    object_to_shot = await page.querySelector(css_selector)
    screenshot = await object_to_shot.screenshot()
    yield screenshot
