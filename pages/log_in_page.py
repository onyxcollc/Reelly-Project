from time import sleep

from selenium.webdriver.common.by import By


from pages.base_page import BasePage



class LogInPage(BasePage):


    EMAIL_VALUE = (By.CSS_SELECTOR, "[placeholder='Email']")
    PASSWORD_VALUE = (By.CSS_SELECTOR, "[placeholder='Password']")
    CONTINUE_BTN = (By.CSS_SELECTOR, "[wized='loginButton']")
    CONTINUE_BTN_MOBILE = (By.CSS_SELECTOR,".login-button")

    def email_address(self,address):
        sleep(3)
        self.input_text(address,*self.EMAIL_VALUE)


    def enter_password(self,password):
        sleep(3)
        self.input_text(password,*self.PASSWORD_VALUE)


    def continue_button(self):
        sleep(3)
        self.click(*self.CONTINUE_BTN)
        self.driver.save_screenshot('screenshots/02_continue_button.png')

    def continue_button_mobile(self):
        sleep(3)
        self.click_outside()
        self.wait_for_element_visibility(*self.CONTINUE_BTN_MOBILE)