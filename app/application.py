
from pages.base_page import BasePage
from pages.broker_relationship_page import BrokerPage
from pages.log_in_page import LogInPage
from pages.main_page import MainPage
from pages.home_page import HomePage
from pages.market_page import MarketPage
from pages.off_plan_page import OffPlanPage
from pages.price_page import PricePage


class Application:
    def __init__(self, driver):
        self.base_page = BasePage(driver)
        self.log_in_page = LogInPage(driver)
        self.main_page = MainPage(driver)
        self.home_page = HomePage(driver)
        self.off_plan_page = OffPlanPage(driver)
        self.price_page = PricePage(driver)
        self.market_page = MarketPage(driver)
        self.broker_relationship_page = BrokerPage(driver)