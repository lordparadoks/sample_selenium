from tests.page.edit_teacher_profile_page import EditTeacherProfilePage
from tests.page.math_madness_page import MathMadnessPage
from tests.page.index_page import IndexPage
from tests.page.manage_team_page import ManageTeamPage
from selenium.webdriver.common.action_chains import ActionChains
from tests.page.abstract_page import AbstractPage

class TeacherIndexPage(AbstractPage):

    def __init__(self, driver):
        super(TeacherIndexPage, self).__init__(driver)

    def open_teacher_profile_page(self):
        dropdown_hover = self.driver.find_element_by_css_selector('.profile-dropdown > a.current')
        hover = ActionChains(self.driver).move_to_element(dropdown_hover)
        hover.perform()
        self.driver.find_element_by_css_selector('.profile-dropdown li:nth-child(1) a.hint').click()
        return EditTeacherProfilePage(self.driver)

    def open_math_madness_page(self):
        dropdown_hover = self.driver.find_element_by_css_selector('.profile-dropdown > a.current')
        hover = ActionChains(self.driver).move_to_element(dropdown_hover)
        hover.perform()
        self.driver.find_element_by_css_selector('.profile-dropdown li:nth-child(2) a.hint').click()
        return MathMadnessPage(self.driver)

    def log_out(self):
        dropdown_hover = self.driver.find_element_by_css_selector('.profile-dropdown > a.current')
        hover = ActionChains(self.driver).move_to_element(dropdown_hover)
        hover.perform()
        self.driver.find_element_by_css_selector('.profile-dropdown li:nth-child(4) a.hint').click()
        self.driver.find_element_by_css_selector('div.logo > a').click()
        return IndexPage(self.driver)

    def open_manage_team_page(self):
        self.driver.find_element_by_xpath('//*[@id="head_links"]/li[1]/a').click()
        return ManageTeamPage(self.driver)


    #
    # def open_schedule_page (self):
    #
    # def open_results_page(self):
    #
    # def open_create_match_page(self):
    #
    # def open_manage_team_page(self):