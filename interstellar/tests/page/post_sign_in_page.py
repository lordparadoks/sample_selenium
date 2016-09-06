from tests.page.abstract_page import AbstractPage


class PostSignInPage(AbstractPage):
    def __init__(self, driver):
        super(PostSignInPage, self).__init__(driver)