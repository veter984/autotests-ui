from playwright.sync_api import Page, expect
from pages.base_page import BasePage
from components.navigation.navbar_component import NavbarComponent
from components.navigation.sidebar_component import SidebarComponent
from components.dashboard.dashboard_toolbar_view_component import DashboardToolbarViewComponent
from components.charts.chart_view_component import ChartViewComponent

class DashboardPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.sidebar = SidebarComponent(page)
        self.navbar = NavbarComponent(page)
        self.dashboard_toolbar_view = DashboardToolbarViewComponent(page)
        self.scores_chart_view = ChartViewComponent(page, "scores", "scatter")
        self.courses_chart_view = ChartViewComponent(page, "courses", "pie")
        self.students_chart_view = ChartViewComponent(page, "students", "bar")
        self.activities_chart_view = ChartViewComponent(page, "activities", "line")

        self.dashboard_title = page.get_by_test_id('dashboard-toolbar-title-text')


    def check_visible_dashboard_title(self):
       expect(self.dashboard_title).to_be_visible()
       expect(self.dashboard_title).to_have_text("Dashboard")

    def check_visible_students_chart(self):
        self.students_chart_view.check_visible('Students')
        #expect(self.students_title).to_be_visible()
        #expect(self.students_title).to_have_text('Students')
        #expect(self.students_chart).to_be_visible()

    def check_visible_courses_chart(self):
        self.courses_chart_view.check_visible('Courses')
        #expect(self.courses_title).to_be_visible()
        #expect(self.courses_title).to_have_text('Courses')
        #expect(self.courses_chart).to_be_visible()

    def check_visible_activities_chart(self):
        self.activities_chart_view.check_visible('Activities')
        #expect(self.activities_title).to_be_visible()
        #expect(self.activities_title).to_have_text('Activities')
        #expect(self.activities_chart).to_be_visible()

    def check_visible_scores_chart(self):
        self.scores_chart_view.check_visible('Scores')
        #expect(self.scores_title).to_be_visible()
        #expect(self.scores_title).to_have_text('Scores')
        #expect(self.scores_chart).to_be_visible()

