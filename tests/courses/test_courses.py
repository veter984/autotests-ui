import pytest
import allure
from pages.courses.courses_list_page import CoursesListPage
from pages.courses.create_course_page import CreateCoursePage
from tools.allure.tags import AllureTag
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
from allure_commons.types import Severity


@pytest.mark.courses
@pytest.mark.regression
@allure.tag(AllureTag.REGRESSION, AllureTag.COURSES)
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.COURSES)
@allure.story(AllureStory.COURSES)
@allure.parent_suite(AllureEpic.LMS)
@allure.suite(AllureFeature.COURSES)
@allure.sub_suite(AllureStory.COURSES)
class TestCourses:
    @allure.title("Check displaying of empty courses list")
    @allure.severity(Severity.NORMAL)
    def test_empty_courses_list(self, courses_list_page: CoursesListPage):
        courses_list_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")
        courses_list_page.toolbar_courses.check_visible()
        courses_list_page.check_visible_empty_view()
        #courses_list_page.check_visible_create_course_button()

        courses_list_page.sidebar.check_visible()
        #остальные методы проверки сайдбара, я так понял не нужны
        #courses_list_page.sidebar.click_logout()
        #courses_list_page.sidebar.click_courses()
        #courses_list_page.sidebar.click_dashboard()
        courses_list_page.navbar.check_visible("username")

    @allure.title("Create course")
    @allure.severity(Severity.CRITICAL)
    def test_create_course(self, courses_list_page: CoursesListPage, create_course_page: CreateCoursePage):
        create_course_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create")
        create_course_page.create_course_toolbar_view.check_visible()
        create_course_page.preview_empty_view.check_visible(title="No image selected",
                                                        description="Preview of selected image will be displayed here"
                                                        )
        create_course_page.image_upload_widget.check_visible(is_image_uploaded=False)
        create_course_page.create_course_form.check_visible(title="", estimated_time="", description="",
                                                        max_score="0", min_score="0"
                                                        )
        create_course_page.create_course_exercise_toolbar_view.check_visible()
        ##create_course_page.check_visible_create_exercise_button()
        create_course_page.exercises_empty_view.check_visible(title="There is no exercises",
                                                          description='Click on "Create exercise" button to create new '
                                                           'exercise'
                                                          )
        create_course_page.image_upload_widget.upload_preview_image(file="./testdata/files/image.png")
        create_course_page.image_upload_widget.check_visible(is_image_uploaded=True)
        create_course_page.create_course_form.fill(title="Playwright", estimated_time="2 weeks",
                                               description="Playwright", max_score="100", min_score="10"
                                               )
        create_course_page.create_course_toolbar_view.click_create_course_button()
        courses_list_page.toolbar_courses.check_visible()
        #courses_list_page.check_visible_create_course_button()
        courses_list_page.course_view.check_visible(index=0, title="Playwright", max_score="100", min_score="10",
                                                estimated_time="2 weeks"
                                                )

    @allure.title("Edit course")
    @allure.severity(Severity.CRITICAL)
    def test_edit_course(self, courses_list_page: CoursesListPage, create_course_page: CreateCoursePage):
        create_course_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create')

        create_course_page.image_upload_widget.upload_preview_image('./testdata/files/image.png')
        create_course_page.create_course_form.fill(title="test", estimated_time="4 weeks",
                                                   description="QA", max_score="500", min_score="100"
                                                   )
        create_course_page.create_course_form.check_visible(title="test", estimated_time="4 weeks",
                                                            description="QA", max_score="500", min_score="100"
                                                           )

        create_course_page.create_course_toolbar_view.click_create_course_button()
        courses_list_page.course_view.check_visible(index=0, title="test", max_score="500", min_score="100",
                                                    estimated_time="4 weeks"
                                                    )
        courses_list_page.course_view.menu.click_edit(index=0)

        create_course_page.create_course_form.fill(title="testo", estimated_time="3 weeks",
                                                   description="QAtest", max_score="50", min_score="10"
                                                   )
        create_course_page.create_course_form.check_visible(title="testo", estimated_time="3 weeks",
                                                            description="QAtest", max_score="50", min_score="10"
                                                           )

        create_course_page.create_course_toolbar_view.click_create_course_button()
        courses_list_page.course_view.check_visible(index=0, title="testo", max_score="50", min_score="10",
                                                    estimated_time="3 weeks"
                                                    )










# не обращайте внимания, оставил на будущее для повторения, после отпуска
#def test_empty_courses_list(chromium_page_with_state: Page):

    #chromium_page_with_state.goto(' https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')

    #courses_toolbar = chromium_page_with_state.get_by_test_id('courses-list-toolbar-title-text')
    #expect(courses_toolbar).to_be_visible()
    #expect(courses_toolbar).to_have_text('Courses')

    #empty_view = chromium_page_with_state.get_by_test_id('courses-list-empty-view-title-text')
    ##expect(empty_view).to_have_text('There is no results')

    #empty_icon = chromium_page_with_state.get_by_test_id('courses-list-empty-view-icon')
    #expect(empty_icon).to_be_visible()

    #description_text = chromium_page_with_state.get_by_test_id('courses-list-empty-view-description-text')
    #expect(description_text).to_be_visible()
    #expect(description_text).to_have_text('Results from the load test pipeline will be displayed here')

        # Задержка для наглядности выполнения теста
    #chromium_page_with_state.wait_for_timeout(3000)
