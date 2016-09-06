from tests.page.abstract_page import AbstractPage
from tests.page.post_sign_in_page import PostSignInPage


class SignInPage(AbstractPage):
    def __init__(self, driver):
        super(SignInPage, self).__init__(driver)

    def log_in(self, user, password):
        self.driver.find_element_by_id('user_session_email').send_keys(user)
        self.driver.find_element_by_id('user_session_password').send_keys(password)
        self.driver.find_element_by_css_selector('.button').click()
        return PostSignInPage(self.driver)
