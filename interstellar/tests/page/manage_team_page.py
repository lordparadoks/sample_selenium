from tests.page.abstract_page import AbstractPage
from tests.page.post_manage_team_page import PostManageTeamPage


class ManageTeamPage(AbstractPage):
    def __init__(self, driver):
        super(ManageTeamPage, self).__init__(driver)

    def student_no_email(self, stud_name, stud_last_name):
        self.driver.find_element_by_css_selector('div.size9of10.add-student-link > a').click()
        self.driver.find_element_by_css_selector('#student_first_name').send_keys(stud_name)
        self.dirver.find_element_by_css_selector('#student_last_name').send_keys(stud_last_name)
        self.driver.find_element_by_css_selector('#no_email').click()
        self.driver.find_element_by_css_selector('div.clearfix.mvm > input.button').click()
        return PostManageTeamPage(self.driver)
