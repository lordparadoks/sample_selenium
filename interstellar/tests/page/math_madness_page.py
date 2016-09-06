from tests.page.abstract_page import AbstractPage
from tests.page.post_edit_teacher_profile_page import PostEditTeacherProfilePage

class MathMadnessPage(AbstractPage):
    def __init__(self, driver):
        super(MathMadnessPage, self).__init__(driver)