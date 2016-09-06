from tests.page.abstract_page import AbstractPage
from tests.page.index_page import IndexPage
from tests.page.post_edit_teacher_profile_page import PostEditTeacherProfilePage
from selenium.webdriver.common.action_chains import ActionChains

class EditTeacherProfilePage(AbstractPage):
    def __init__(self, driver):
        super(EditTeacherProfilePage, self).__init__(driver)

    def edit_form(self, first_name, last_name, phone, bio):
        self.driver.find_element_by_xpath('//*[@id="user_first_name"]').clear()
        self.driver.find_element_by_xpath('//*[@id="user_last_name"]').clear()
        self.driver.find_element_by_xpath('//*[@id="user_phone"]').clear()
        self.driver.find_element_by_xpath('//*[@id="user_bio"]').clear()
        self.driver.find_element_by_xpath('//*[@id="user_first_name"]').send_keys(first_name)
        self.driver.find_element_by_xpath('//*[@id="user_last_name"]').send_keys(last_name)
        self.driver.find_element_by_xpath('//*[@id="user_phone"]').send_keys(phone)
        self.driver.find_element_by_xpath('//*[@id="user_bio"]').send_keys(bio)
        self.driver.find_element_by_xpath('//*[@id="edit_user"]/div[3]/div[5]/div/input').click()
        return PostEditTeacherProfilePage

    def change_password(self, password, confirmation_pass):
        self.driver.find_element_by_xpath('//*[@id="user_password"]').send_keys(password)
        self.driver.find_element_by_xpath('//*[@id="user_password_confirmation"]').send_keys(confirmation_pass)
        self.driver.find_element_by_xpath('//*[@id="edit_user"]/div[5]/div/input').click()
        return PostEditTeacherProfilePage

    def edit_school(self, school, city):
        self.driver.find_element_by_xpath('//*[@id="user_school_attributes_name"]').clear()
        self.driver.find_element_by_xpath('//*[@id="user_school_attributes_city"]').clear()
        self.driver.find_element_by_xpath('//*[@id="user_school_attributes_name"]').send_keys(school)
        self.driver.find_element_by_xpath('//*[@id="user_school_attributes_city"]').send_keys(city)
        self.driver.find_element_by_xpath('//*[@id="edit_user"]/div[7]/input').click()
        return PostEditTeacherProfilePage

    def upload_avatar(self, avatar_path):
        avatar = self.driver.find_element_by_xpath('//*[@id="user_avatar_image_attributes_image"]')
        avatar.send_keys('/Users/spookyact/desktop/avatars/', avatar_path)
        self.driver.find_element_by_xpath('//*[@id="edit_user"]/div[3]/div[5]/div/input').click()
        return PostEditTeacherProfilePage

    def log_out(self):
        dropdown_hover = self.driver.find_element_by_css_selector('.profile-dropdown > a.current')
        hover = ActionChains(self.driver).move_to_element(dropdown_hover)
        hover.perform()
        self.driver.find_element_by_css_selector('.profile-dropdown li:nth-child(4) > a.hint').click()
        self.driver.find_element_by_css_selector('div.logo > a').click()
        return IndexPage
