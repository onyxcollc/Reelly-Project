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
    PRE_SALE_BTN = (By.XPATH,"//div[text()='Presale (EOI)']")
    BUILDING_CARDS = (By.CSS_SELECTOR,".border.bg-card")
    PRE_SALE_CARDS = (By.CSS_SELECTOR,".border.bg-card.text-card-foreground")
    TAG_SELECTOR = (By.XPATH,"//span[text()='Announced']")
    TAG_SELECTOR_2 =(By.XPATH,"//span[text()='Presale(EOI)']")





    def sale_status_tab(self):
        self.wait_for_element_click(*self.SALE_STATUS_TAB)
        self.driver.save_screenshot("screenshots/05_sale_status_tab.png")


    def announced_btn(self):
        sleep(5)
        self.wait_for_element_click(*self.ANNOUNCED_BTN)
        self.driver.save_screenshot("screenshots/06_announced_btn.png")


    def pre_sale_btn(self):
        sleep(5)
        self.wait_for_element_click(*self.PRE_SALE_BTN)
        self.driver.save_screenshot("screenshots/06_on_sale_btn.png")


    def verify_off_plan_page_opened(self):
        self.verify_text("Off-plan",*self.OFF_PLAN_TXT)
        self.driver.save_screenshot("screenshots/04_off_plan_opened.png")


    def verify_pre_sale_eoi_tag(self):
        self.click_outside()
        sleep(5)
        cards = self.driver.find_elements(*self.PRE_SALE_CARDS)
        assert cards, " No building cards found."

        total = len(cards)
        print(total)

        for index in range(min(total,5)):
            try:
                current_cards = self.driver.find_elements(*self.PRE_SALE_CARDS)
                card = current_cards[index]

                tag_element = card.find_element(*self.TAG_SELECTOR_2)
                tag_text = tag_element.text.strip()
            except Exception as e:
                raise AssertionError(f" Building #{index + 1} is missing a tag element: {e}")

            assert "Presale(EOI)" in tag_text, (
                f" Building #{index + 1} is not tagged as 'Presale(EOI)'. Found: '{tag_text}'"

            )
        print(f"All {total} building are correctly tagged as 'Presale (EOI)'")
        self.driver.save_screenshot("screenshots/07_pre_sale_eoi.png")




    def verify_announced_tag(self):
        self.click_outside()
        sleep(5)
        cards = self.driver.find_elements(*self.BUILDING_CARDS)
        assert cards, " No building cards found."

        total = len(cards)
        print(total)

        for index in range(total):
            try:
                current_cards = self.driver.find_elements(*self.BUILDING_CARDS)
                card = current_cards[index]

                tag_element = card.find_element(*self.TAG_SELECTOR)
                tag_text = tag_element.text.strip()
            except Exception as e:
                raise AssertionError(f" Building #{index + 1} is missing a tag element: {e}")

            assert "Announced" in tag_text, (
                f" Building #{index + 1} is not tagged as 'Announced'. Found: '{tag_text}'"

            )
        print(f"All {total} building are correctly tagged as 'Announced'")
        self.driver.save_screenshot("screenshots/07_verify_announced_tag.png")






