from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import BasePage


class MainPage(BasePage):

    def open_main_page(self):
        self.open_url()
        self.driver.save_screenshot('screenshots/01_main_page.png')
        sleep(3)