from playwright.sync_api import sync_playwright
from playwright_stealth import stealth_sync

def get_page():
    pw = sync_playwright().start()
    browser = pw.chromium.launch(
        headless=False,                # run headful first; flip to True later
        args=["--disable-blink-features=AutomationControlled"],
    )
    ctx = browser.new_context(
        user_agent=("Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                    "AppleWebKit/537.36 (KHTML, like Gecko) "
                    "Chrome/131.0.0.0 Safari/537.36"),
        viewport={"width": 1366, "height": 768},
        locale="en-IN",
    )
    page = ctx.new_page()
    stealth_sync(page)
    return pw, browser, page
