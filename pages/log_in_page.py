from selenium.webdriver.common.by import By


from pages.base_page import BasePage



class LogInPage(BasePage):


    EMAIL_VALUE = (By.CSS_SELECTOR, "[placeholder='Email']")
    PASSWORD_VALUE = (By.CSS_SELECTOR, "[placeholder='Password']")
    CONTINUE_BTN = (By.CSS_SELECTOR, "[wized='loginButton']")


    def email_address(self,address):
        self.input_text(address,*self.EMAIL_VALUE)


    def enter_password(self,password):
        self.input_text(password,*self.PASSWORD_VALUE)


    def continue_button(self):
        self.click(*self.CONTINUE_BTN)
        self.driver.save_screenshot('screenshots/02_continue_button.png')
