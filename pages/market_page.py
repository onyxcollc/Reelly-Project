from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from time import sleep



class MarketPage(BasePage):

    OFFERS_FOR_YOU_TXT = (By.XPATH,"//div[text()='Offers for you']")
    LEARN_MORE_BTN = (By.XPATH,"//div[text()='Learn more']")
    CLICK_CONNECT_AGENT = (By.XPATH,"//*[text()='Connect to the network of 42K agents']")

    def click_learn_more_button(self):
        sleep(3)
        self.wait_for_element_click(*self.CLICK_CONNECT_AGENT)
        sleep(5)


    def verify_market_page_open(self):
        sleep(3)
        self.verify_text('Offers for you', *self.OFFERS_FOR_YOU_TXT)


    def verify_learn_more_button(self):
        self.find_element(*self.LEARN_MORE_BTN)