import unittest

from tests.browser import Browser
from selenium import webdriver
from tests.page.teacher_index_page import TeacherIndexPage
from tests.page.index_page import IndexPage
from random import randint
from hamcrest import assert_that, contains_string

class EditProfileTest(unittest.TestCase):

    def setUp(self):
        self.browser = Browser()
        self.driver = self.browser.start()
        self.driver.get('http://staging.in-ter-stel-lar.com/')

    def login(self):
        user = 'kesha+3@rw.rw'
        password = '123456'
        #when
        sign_in_page = IndexPage(self.driver).open_sign_in_page()
        post_sign_in_page = sign_in_page.log_in(user, password)

    def test_edit_profile(self):
        first_name = "Tom", + randint(1, 100)
        last_name = "Cox", + randint(1, 10)
        phone = "500123456"
        bio = "SAasldhasjdjasldkalksdjhasdj,dasasdsadsadas"
        #when
        self.login()
        #then
        teacher_index_page = TeacherIndexPage(self.driver).open_teacher_profile_page()
        post_edit_teacher_profile_page = teacher_index_page.edit_form(first_name, last_name, phone, bio)
        assert_that(post_edit_teacher_profile_page.get_page_source(), contains_string('Your account has been updated.'))

    def test_change_password(self):
        password = '123456'
        confirmation_pass = '123456'
        self.login()
        #then
        teacher_index_page = TeacherIndexPage(self.driver).open_teacher_profile_page()
        post_teacher_index_page = teacher_index_page.change_password(password, confirmation_pass)

    def test_edit_school(self):
        school = "Hogwarts", + randint(1, 1000)
        city = "alaska", + randint(1, 1000)
        self.login()
        #then
        teacher_index_page = TeacherIndexPage(self.driver).open_teacher_profile_page()
        post_teacher_index_page = teacher_index_page.edit_school(school, city)

    def test_upload_avatar(self):
        avatar_path = "logo", randint(1, 5), ".jpg"
        self.login()
        teacher_index_page = TeacherIndexPage(self.driver).open_teacher_profile_page()
        post_edit_teacher_profile_page = teacher_index_page.upload_avatar(avatar_path)
        assert_that(post_edit_teacher_profile_page.get_page_source(), contains_string('Your account has been updated'))

    # def test change_timezone(self):

    #
    # def test_change_countries(self):