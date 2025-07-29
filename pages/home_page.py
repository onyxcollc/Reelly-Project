from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By


from pages.base_page import BasePage



class HomePage(BasePage):


    OFF_PLAN_TAB = (By.CSS_SELECTOR, "[wized='newOffPlanLink']")
    OFF_PLAN_TAB_MOBILE = (By.CSS_SELECTOR,"[w-el-onclick-0-0*='1XbhaFQ']")


    def off_plan_tab(self):
        sleep(5)
        self.wait_for_element_click(*self.OFF_PLAN_TAB)
        self.driver.save_screenshot("screenshots/03_off_plan_tab.png")


    def off_plan_tab_mobile(self):
        sleep(3)
        elements = self.find_elements(*self.OFF_PLAN_TAB_MOBILE)

        if len(elements) >=2:
            second_element = elements[1]
            second_element.click()
            self.driver.save_screenshot("screenshots_mobile/03_off_plan_tab_mobile.png")

        else:
            raise Exception("Second element  for  OFF_PLAN_TAB_MOBILE not found")