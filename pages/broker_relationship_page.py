from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from time import sleep



class BrokerPage(BasePage):


    YOUR_NAME = (By.CSS_SELECTOR,"[placeholder='Your name']")
    COMPANY_NAME = (By.CSS_SELECTOR,"[placeholder='Company name']")
    ROLE_NAME = (By.CSS_SELECTOR,"[placeholder='Role in the company']")
    COMPANY_AGE = (By.CSS_SELECTOR,"[placeholder='Age of the company?']")
    COUNTRY_PROJECT_LOCATION = (By.CSS_SELECTOR,"[placeholder='Country for placing the project']")
    PROJECT_NAME = (By.CSS_SELECTOR,"[placeholder='Name of the project to hos']")
    PHONE_NUMBER = (By.CSS_SELECTOR,"[placeholder='Phone']")
    EMAIL_ADDRESS = (By.CSS_SELECTOR,"[placeholder='Email']")
    SEND_APP_BTN = (By.CSS_SELECTOR,"[value='Send an application']")

    def broker_form(self):
        sleep(2)
        self.input_text('John Doe', *self.YOUR_NAME)
        self.input_text('PJ Mask', *self.COMPANY_NAME)
        self.input_text('CEO', *self.ROLE_NAME)
        self.input_text('5', *self.COMPANY_AGE)
        self.input_text('Dubi', *self.COUNTRY_PROJECT_LOCATION)
        self.input_text(' Lux Apartments', *self.PROJECT_NAME)
        self.input_text('5468837363', *self.PHONE_NUMBER)
        self.input_text('test@test.com', *self.EMAIL_ADDRESS)
        sleep(2)
