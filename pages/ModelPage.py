class ModelPage:
    """This is the default page object for the derivatives of other classes"""

    def __init__(self, page):
        self.page = page

    def __getattr__(self, name):
        """
        Method called if attribute is not implemented in this Page Object.
        Return attribute of the standard playwright page
        """
        return object.__getattribute__(self.page, name)
