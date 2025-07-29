from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By


from pages.base_page import BasePage



class HomePage(BasePage):


    OFF_PLAN_TAB = (By.CSS_SELECTOR, "[wized='newOffPlanLink']")
    OFF_PLAN_TAB_MOBILE = (By.CSS_SELECTOR,"div[wized*='mobileMenu'] a[wized='newOffPlanLink']")


    def off_plan_tab(self):
        sleep(5)
        self.wait_for_element_click(*self.OFF_PLAN_TAB)
        self.driver.save_screenshot("screenshots/03_off_plan_tab.png")


    def off_plan_tab_mobile(self):
        sleep(3)
        self.wait_for_element_click(*self.OFF_PLAN_TAB_MOBILE)
        self.driver.save_screenshot("screenshots_mobile/03_off_plan_tab_mobile.png")

