import pytest
from pages.courses_page import CoursesPage

@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(courses_page: CoursesPage):
    courses_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

    courses_page.sidebar.check_visible()
    courses_page.navbar.check_visible("username")

    courses_page.check_visible_courses_title()
    courses_page.check_visible_create_course_button()
    courses_page.check_visible_empty_view()
