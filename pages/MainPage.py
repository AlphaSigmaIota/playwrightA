from settings import settings


class MainPage:
    """The Main Page for playwright.dev to test on"""

    def __init__(self, page):
        self.page = page

    def navigate(self):
        """Navigation to the page"""
        self.page.goto(settings.URLS.PLAYWRIGHT_DEV)
