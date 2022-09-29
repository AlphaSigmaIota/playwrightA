from settings import settings

from .ModelPage import ModelPage


class MainPage(ModelPage):
    """The Main Page for playwright.dev to test on"""

    def __init__(self, page):
        self.page = page

        self.button_get_started = page.locator("a.getStarted_Sjon")

    def navigate(self):
        """Navigation to the page"""
        self.page.goto(settings.URLS.PLAYWRIGHT_DEV)

    def check_present(self):
        """Method for checking if the Page is opened."""
        assert self.button_get_started.is_visible(), "MainPage is not visible"
