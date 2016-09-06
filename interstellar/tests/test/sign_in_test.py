import unittest

from hamcrest import assert_that, contains_string
from random import randint

from tests.browser import Browser
from tests.page.index_page import IndexPage

class SignInTest(unittest.TestCase):
    def setUp(self):
        self.browser = Browser()
        self.driver = self.browser.start()
        self.driver.get('http://staging.in-ter-stel-lar.com/')

    def test_logging_teacher_should_succeed(self):
        #given
        user = 'kesha+3@rw.rw'
        password = '123456'

        #when
        sign_in_page = IndexPage(self.driver).open_sign_in_page()
        post_sign_in_page = sign_in_page.log_in(user, password)

        #then
        assert_that(post_sign_in_page.get_page_source(), contains_string('Login successful!'))

    def test_with_invalid_credentials(self):
        #given
        user = 'kesha+2@rw.rw'
        password = 1234567
        incorrect_password = 'You have entered an invalid email or password.'

        #when
        sign_in_page = IndexPage(self.driver).open_sign_in_page()
        post_sign_in_page = sign_in_page.log_in(user, password)

        #then
        assert_that(post_sign_in_page.get_page_source(), contains_string(incorrect_password))

    def test_with_fake_data(self):
        #given
        user = 'kaszubski'
        password = 'jenkins'
        
        #when
        sign_in_page = IndexPage(self.driver).open_sign_in_page()
        post_sign_in_page = sign_in_page.log_in(user, password)
        
        #then
        #then
        assert_that(post_sign_in_page.get_page_source(), contains_string("Invalid username"))

    def test_forgot_password(self):
        #given
        email = 'kesha+2@rw.rw'
        alert = 'Instructions to reset your password have been emailed to you.'

        #when
        forgot_password_page = IndexPage(self.driver).open_forgot_password_page()
        post_forgot_password_page = forgot_password_page.type_password(email)

        #then
        assert_that(post_forgot_password_page.get_page_source(), contains_string(alert))






