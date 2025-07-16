
from pages.base_page import BasePage
from pages.log_in_page import LogInPage
from pages.main_page import MainPage
from pages.home_page import HomePage
from pages.off_plan_page import OffPlanPage


class Application:
    def __init__(self, driver):
        self.base_page = BasePage(driver)
        self.log_in_page = LogInPage(driver)
        self.main_page = MainPage(driver)
        self.home_page = HomePage(driver)
        self.off_plan_page = OffPlanPage(driver)