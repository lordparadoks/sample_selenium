from tests.page.abstract_page import AbstractPage
from tests.page.post_forgot_password_page import PostForgotPasswordPage


class ForgotPasswordPage(AbstractPage):
    def __init__(self, driver):
        super(ForgotPasswordPage, self).__init__(driver)

    def type_password(self, email):
        self.driver.find_element_by_xpath('//*[@id="email"]').send_keys(email)
        self.driver.find_element_by_css_selector('.button').click()
        return PostForgotPasswordPage(self.driver)
