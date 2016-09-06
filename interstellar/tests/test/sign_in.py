import unittest

from tests.browser import Browser

from tests.page.index_page import IndexPage

class SignInTest(unittest.TestCase):
    def setUp(self):
        self.browser = Browser()
        self.driver = self.browser.start()
        self.driver.get('http://staging.in-ter-stel-lar.com/')

    def test_logging_teacher_should_succeed(self):
        #given
        user = 'kesha+1@rw.rw'
        password = '123456'

        #when
        var = IndexPage(self.driver).open_sign_in_page
        post_sign_in_page.log_in(user, password)
