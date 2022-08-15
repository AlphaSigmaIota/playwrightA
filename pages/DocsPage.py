from .MainPage import MainPage
from .ModelPage import ModelPage


class DocsPage(ModelPage):
    """The Docs Page for playwright.dev to test on"""

    def __init__(self, page):
        self.page = page

        self.label_title = page.locator("h1", has_text="Installation")

    def navigate(self):
        """Alternative navigation method to just calling of the URL"""
        main_page = MainPage(self.page)
        main_page.navigate()
        main_page.check_am_i_there()
        main_page.button_get_started.click()

    def check_am_i_there(self):
        """Method for checking if the Page is opened."""
        assert self.label_title.is_visible(), "DocsPage is not visible"
