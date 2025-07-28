import pytest
from playwright.sync_api import Page, expect


@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(chromium_page_with_state: Page):
    page = chromium_page_with_state
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

    courses_toolbar_title = page.get_by_test_id('courses-list-toolbar-title-text')
    expect(courses_toolbar_title).to_be_visible()
    expect(courses_toolbar_title).to_have_text('Courses')

    folder_icon = page.get_by_test_id('courses-list-empty-view-icon')
    expect(folder_icon).to_be_visible()

    view_title_text = page.get_by_test_id('courses-list-empty-view-title-text')
    expect(view_title_text).to_be_visible()
    expect(view_title_text).to_have_text('There is no results')

    description_rext = page.get_by_test_id('courses-list-empty-view-description-text')
    expect(description_rext).to_be_visible()
    expect(description_rext).to_have_text('Results from the load test pipeline will be displayed here')