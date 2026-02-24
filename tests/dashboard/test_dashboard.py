import pytest
import allure

from config import settings
from pages.dashboard.dashboard_page import DashboardPage
from tools.allure.tags import AllureTag
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
from allure_commons.types import Severity

from tools.routes import AppRoute


@pytest.mark.dashboard
@pytest.mark.regression
@allure.tag(AllureTag.REGRESSION, AllureTag.DASHBOARD)
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.DASHBOARD)
@allure.story(AllureStory.DASHBOARD)
@allure.parent_suite(AllureEpic.LMS)
@allure.suite(AllureFeature.DASHBOARD)
@allure.sub_suite(AllureStory.DASHBOARD)
class TestDashboard:
    @allure.title("Check displaying of dashboard page")
    @allure.severity(Severity.NORMAL)
    def test_dashboard_displaying(self, dashboard_page_with_state: DashboardPage):
        dashboard_page_with_state.visit(AppRoute.DASHBOARD)

        dashboard_page_with_state.sidebar.check_visible()
        #остальные методы проверки сайдбара, я так понял не нужны
        #dashboard_page_with_state.sidebar.click_logout()
        #dashboard_page_with_state.sidebar.click_courses()
        #dashboard_page_with_state.sidebar.click_dashboard()

        dashboard_page_with_state.navbar.check_visible(settings.test_user.username)
        dashboard_page_with_state.check_visible_dashboard_title()
        dashboard_page_with_state.check_visible_scores_chart()
        dashboard_page_with_state.check_visible_courses_chart()
        dashboard_page_with_state.check_visible_students_chart()
        dashboard_page_with_state.check_visible_activities_chart()
        #dashboard_page_with_state.dashboard_toolbar_view.check_visible()
        #dashboard_page_with_state.scores_chart_view.check_visible()
        #dashboard_page_with_state.courses_chart_view.check_visible()
        #dashboard_page_with_state.students_chart_view.check_visible()
        #dashboard_page_with_state.activities_chart_view.check_visible()