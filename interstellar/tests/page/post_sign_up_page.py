from tests.page.abstract_page import AbstractPage


class PostSignUpPage(AbstractPage):
    def __init__(self, driver):
        super(PostSignUpPage, self).__init__(driver)