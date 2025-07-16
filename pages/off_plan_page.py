from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from time import sleep

from pages.base_page import BasePage




class OffPlanPage(BasePage):

    OFF_PLAN_TXT = (By.XPATH,"//button[text()='Off-plan']")
    SALE_STATUS_TAB = (By.XPATH,"//button[text()='Sale Status']")
    ANNOUNCED_BTN = (By.XPATH,"//div[text()='Announced']" )
    ANNOUNCED_TAG = (By.XPATH,"//span[text()='Announced']")





    def sale_status_tab(self):
        self.wait_for_element_click(*self.SALE_STATUS_TAB)
        self.driver.save_screenshot("screenshots/05_sale_status_tab.png")


    def announced_btn(self):
        self.wait_for_element_click(*self.ANNOUNCED_BTN)
        self.driver.save_screenshot("screenshots/06_announced_btn.png")


    def verify_announced_tag(self):

        self.click_outside()
        self.verify_text("Announced",*self.ANNOUNCED_TAG)
        self.driver.save_screenshot("screenshots/07_verify_announced_tag.png")



    def verify_off_plan_page_opened(self):
        self.verify_text("Off-plan",*self.OFF_PLAN_TXT)
        self.driver.save_screenshot("screenshots/04_off_plan_opened.png")



