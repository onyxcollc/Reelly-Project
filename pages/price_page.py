from selenium.webdriver.common.by import By
from time import sleep


from pages.base_page import BasePage






class PricePage(BasePage):

    MIN_PRICE =(By.CSS_SELECTOR,"[placeholder='From']")
    MAX_PRICE =(By.CSS_SELECTOR,"[placeholder='To']")
    APPLY_BTN =(By.XPATH,"//button[text()='Apply filter']")

    def min_max_price(self,min_val,max_val):
        self.input_text(min_val,*self.MIN_PRICE)
        self.input_text(max_val,*self.MAX_PRICE)
        self.click(*self.APPLY_BTN)


