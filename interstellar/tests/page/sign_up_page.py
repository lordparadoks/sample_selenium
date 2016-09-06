from tests.page.abstract_page import AbstractPage
from tests.page.post_sign_up_page import PostSignUpPage

from selenium import webdriver
from selenium.webdriver.support.ui import Select

class SignUpPage(AbstractPage):
    def __init__(self, driver):
        super(SignUpPage, self).__init__(driver)

    def sign_up(self, first_name, last_name, email, req_password, req_password2, school_name, city_name):
        self.driver.find_element_by_id('moderator_first_name').send_keys(first_name)
        self.driver.find_element_by_id('moderator_last_name').send_keys(last_name)
        self.driver.find_element_by_id('moderator_email').send_keys(email)
        self.driver.find_element_by_id('moderator_password').send_keys(req_password)
        self.driver.find_element_by_id('moderator_password_confirmation').send_keys(req_password2)
        self.driver.find_element_by_id('moderator_school_attributes_name').send_keys(school_name)
        self.driver.find_element_by_id('moderator_school_attributes_city').send_keys(city_name)
        self.driver.find_element_by_xpath('//*[@id="s2id_moderator_school_attributes_state"]/a').click()
        self.driver.find_element_by_xpath('//*[@id="select2-results-1"]').click()
        self.driver.find_element_by_xpath('//*[@id="s2id_moderator_school_attributes_country"]/a').click()
        self.driver.find_element_by_xpath('//*[@id="select2-results-2"]').click()
        self.driver.find_element_by_xpath('//*[@id="new_moderator"]/div[8]/input').click()
        return PostSignUpPage(self.driver)


    # def select_state (self):
    #     state = Select(self.driver.find_element_by_id('moderator_school_attributes_state')
    #     state.find_element_by_text('Alabama')

        # select = Select(self.driver.find_element_by_id('moderator_school_attributes_state')

    # def state_click(self):
    #     StateList = self.driver.find_element_by_xpath('//*[@id="moderator_school_attributes_state"]').click()

