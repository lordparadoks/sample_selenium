from tests.page.abstract_page import AbstractPage


class PostForgotPasswordPage(AbstractPage):
    def __init__(self, driver):
        super(PostForgotPasswordPage, self).__init__(driver)