from settings import settings


class MainPage:
    """The Main Page for playwright.dev to test on"""

    def __init__(self, page):
        self.page = page

    def navigate(self):
        """Navigation to the page"""
        self.page.goto(settings.URLS.PLAYWRIGHT_DEV)

    def __getattr__(self, name):
        """
        Method called if attribute is not implemented in this Page Object.
        Return attribute of the standard playwright page
        """
        return object.__getattribute__(self.page, name)
