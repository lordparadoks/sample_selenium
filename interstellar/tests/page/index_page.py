from tests.page.abstract_page import AbstractPage
from tests.page.sign_in_page import SignInPage
from tests.page.sign_up_page import SignUpPage
from tests.page.forgot_password_page import ForgotPasswordPage

class IndexPage(AbstractPage):

    def __init__(self, driver):
        super(IndexPage, self).__init__(driver)

    def open_sign_in_page(self):
        self.driver.find_element_by_xpath('//*[@id="head_links"]/li[3]/a').click()
        return SignInPage(self.driver)

    def open_sign_up_page(self):
        self.driver.find_element_by_css_selector('a.home-button.js-popup-link').click()
        return SignUpPage(self.driver)

    def open_forgot_password_page(self):
        self.driver.find_element_by_xpath('//*[@id="head_links"]/li[3]/a').click()
        self.driver.find_element_by_css_selector('a.forgot-pass').click()
        return ForgotPasswordPage(self.driver)

