from time import sleep

from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class HomePage(BasePage):


    OFF_PLAN_TAB = (By.CSS_SELECTOR, "[wized='newOffPlanLink']")



    def off_plan_tab(self):
        self.wait_for_element_click(*self.OFF_PLAN_TAB)
        sleep(3)
        self.driver.save_screenshot("screenshots/03_off_plan_tab.png")