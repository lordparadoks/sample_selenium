import unittest
from random import randint
from hamcrest import assert_that, contains_string
from tests.page.teacher_index_page import TeacherIndexPage
from tests.browser import Browser
from tests.page.index_page import IndexPage
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.support.ui import Select

class SignUpTest(unittest.TestCase):
    def setUp(self):
        print('test')
        self.browser = Browser()
        self.driver = self.browser.start()
        self.driver.get('http://staging.in-ter-stel-lar.com/')

    def test_registration_should_succeed(self):
        for x in range (1, 100):
            first_name = "Tony", + randint(1, 10000)
            last_name = "Montana", + randint(1, 999)
            email = "tony.montana", + randint(1, 1000), "@netguru.pl"
            req_password = '123456'
            req_password2 = '123456'
            school_name = 'hogwarts'
            school_city = 'tol bared'
            sign_up_page = IndexPage(self.driver).open_sign_up_page()
            post_sign_up_page = sign_up_page.sign_up(first_name, last_name, email, req_password, req_password2, school_name, school_city)
            TeacherIndexPage(self.driver).log_out()

    def test_user_does_not_type_any_password(self):
        #given
        first_name ="Jimmy", + randint(1, 100)
        last_name = "Bond"
        email = "jimmy.bond@netguru.pl"
        req_password =''
        req_password2 = ''
        school_name = 'Beauxbautons'
        school_city = 'Paris'

        # when
        sign_up_page = IndexPage(self.driver).open_sign_up_page()
        post_sign_up_page = sign_up_page.sign_up(first_name, last_name, email, req_password, req_password2,  school_name, school_city)
        # then
        assert_that(sign_up_page.get_page_source(), contains_string('Password must have a minimum of 6 characters.'))
        assert_that(sign_up_page.get_page_source(), contains_string('Password confirmation must have a minimum of 6 characters.'))

    def test_user_types_one_password(self):
        first_name ="Jimmy", + randint(1, 100)
        last_name = "Bond"
        email = "jimmy.bond@netguru.pl"
        req_password =''
        school_name = 'Beauxbautons'
        school_city = 'Paris'

        # when
        sign_up_page = IndexPage(self.driver).open_sign_up_page()
        post_sign_up_page = sign_up_page.sign_up(first_name, last_name, email, req_password, req_password2, school_name, school_city)


    def test_user_does_not_type_school_name(self):
        #given
        first_name ="Jimmy", + randint(1, 100)
        last_name = "Bond"
        email = "jimmy.bond@netguru.pl"
        req_password = 'powermetal', +  randint(1, 100)
        req_password2 = 'powermetal', + randint(1, 100)
        school_name = ''
        school_city = 'Paris'
        #when
        sign_up_page = IndexPage(self.driver).open_sign_up_page()
        post_sign_up_page = sign_up_page.sign_up(first_name, last_name, email, req_password, req_password2, school_name, school_city)
        #then
        assert_that(sign_up_page.get_page_source(), contains_string('Name can\'t be blank.'))

      # def test_user_does_not_type_city_name(self):
      #   #given
      #   first_name ="Jimmy", + randint(1, 100)
      #   last_name = "Bond"
      #   email = "jimmy.bond@netguru.pl"
      #   req_password = 'powermetal', +  randint(1, 100)
      #   req_password2 = 'powermetal', + randint(1, 100)
      #   school_name = 'Beauxbatons'
      #   school_city = ''
      #   #when
      #   sign_up_page = IndexPage(self.driver).open_sign_up_page()
      #   post_sign_up_page = sign_up_page.sign_up(first_name, last_name, email, req_password, req_password2, school_name, school_city)
      #   #then
      #   assert_that(sign_up_page.get_page_source(), contains_string('Name can\'t be blank.'))
