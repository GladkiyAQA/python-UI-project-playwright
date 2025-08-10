import allure
import pytest
from allure_commons.types import Severity

from pages.courses.create_course_page import CreateCoursePage
from pages.courses.courses_page import CoursesPage
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
from tools.allure.tags import AllureTag


@pytest.mark.courses
@pytest.mark.regression
@allure.tag(AllureTag.REGRESSION, AllureTag.COURSES)
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.COURSES)
@allure.story(AllureStory.COURSES)
class TestCourses:
    @allure.title("Create course")
    @allure.severity(Severity.CRITICAL)
    def test_create_course(self, create_course_page: CreateCoursePage, courses_page: CoursesPage):
        create_course_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create")

        create_course_page.toolbar.check_visible()

        create_course_page.image_upload_widget.check_visible(is_image_uploaded=False)

        create_course_page.form.check_visible(
            title='',
            estimated_time='',
            description='',
            max_score='0',
            min_score='0',
        )

        create_course_page.exercises_toolbar.check_visible()
        create_course_page.check_visible_exercises_empty_view()

        create_course_page.image_upload_widget.upload_preview_image('./test-data/files/image.png')
        create_course_page.image_upload_widget.check_visible(is_image_uploaded=True)

        create_course_page.form.fill(
            title='Playwright',
            estimated_time='2 weeks',
            description='Playwright',
            max_score='100',
            min_score='10',
        )

        create_course_page.toolbar.click_create_course_button()

        courses_page.toolbar_view.check_visible()
        courses_page.course_view.check_visible(
            index=0,
            title='Playwright',
            max_score='100',
            min_score='10',
            estimated_time='2 weeks',
        )

    @allure.title("Check displaying of empty courses list")
    @allure.severity(Severity.NORMAL)
    def test_empty_courses_list(self, courses_page: CoursesPage):
        courses_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

        courses_page.sidebar.check_visible()
        courses_page.navbar.check_visible("username")

        courses_page.toolbar_view.check_visible()
        courses_page.empty_view.check_visible(
            title='There is no results',
            description='Results from the load test pipeline will be displayed here'
        )

    @allure.title("Edit course")
    @allure.severity(Severity.CRITICAL)
    def test_edit_course(self, create_course_page: CreateCoursePage, courses_page: CoursesPage):
        create_course_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create")

        create_course_page.toolbar.check_visible()
        create_course_page.image_upload_widget.check_visible(is_image_uploaded=False)

        create_course_page.image_upload_widget.upload_preview_image("./test-data/files/image.png")
        create_course_page.image_upload_widget.check_visible(is_image_uploaded=True)

        create_course_page.form.fill(
            title="Playwright",
            estimated_time="2 weeks",
            description="Playwright",
            max_score="100",
            min_score="10",
        )
        create_course_page.toolbar.click_create_course_button()

        courses_page.toolbar_view.check_visible()
        courses_page.course_view.check_visible(
            index=0,
            title="Playwright",
            max_score="100",
            min_score="10",
            estimated_time="2 weeks",
        )

        courses_page.course_view.menu.click_edit(index=0)

        create_course_page.form.fill(
            title="Playwright PRO",
            estimated_time="3 weeks",
            description="Playwright advanced",
            max_score="120",
            min_score="20",
        )
        create_course_page.toolbar.click_create_course_button()

        courses_page.toolbar_view.check_visible()
        courses_page.course_view.check_visible(
            index=0,
            title="Playwright PRO",
            max_score="120",
            min_score="20",
            estimated_time="3 weeks",
        )

