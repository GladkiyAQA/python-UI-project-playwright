import allure
from playwright.sync_api import Page
from components.base_component import BaseComponent
from elements.text import Text
from elements.button import Button

class CreateCourseExercisesToolbarViewComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)
        self.title = Text(
            page, "create-course-exercises-box-toolbar-title-text", "Exercises toolbar title"
        )
        self.create_exercise_button = Button(
            page, "create-course-exercises-box-toolbar-create-exercise-button", "Create exercise button"
        )

    @allure.step('Check visible "Exercises" toolbar')
    def check_visible(self):
        self.title.check_visible()
        self.title.check_have_text("Exercises")
        self.create_exercise_button.check_visible()

    @allure.step('Click "Create exercise"')
    def click_create_exercise_button(self):
        self.create_exercise_button.click()
