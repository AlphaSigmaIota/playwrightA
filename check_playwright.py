from playwright.sync_api import sync_playwright
from settings import settings

if __name__ == "__main__":
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()
        page.goto(settings.URLS.PLAYWRIGHT_DEV)
        print(f"opened website '{page.title()}'")
        browser.close()
