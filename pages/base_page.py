from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains



from support.logger import logger




class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 15)
        self.base_url = 'https://soft.reelly.io'

    def open_url(self, end_url=''):
        url = f'{self.base_url}{end_url}'
        logger.info(f'Opening URL: {url}')
        self.driver.get(url)

    def get(self, url):
        return self.driver.get(url)

    def find_element(self, *locator):
        logger.info(f'Searching for {locator}')
        return self.driver.find_element(*locator)

    def find_elements(self, *locator):
        return self.driver.find_elements(*locator)

    def click(self, *locator):
        logger.info(f'CLicking on {locator}')
        self.driver.find_element(*locator).click()

    def input_text(self, text, *locator):
        logger.info(f'Entering "{text}" in {locator}')
        return self.driver.find_element(*locator).send_keys(text)

    def hover_element(self, *locator):
        element = self.find_element(*locator)
        actions = ActionChains(self.driver)
        actions.move_to_element(element)
        actions.perform()

    def drag_drop(self, source_locator, target_locator):
        source_element = self.driver.find_element(*source_locator)
        target_element = self.driver.find_element(*target_locator)
        actions = ActionChains(self.driver)
        actions.drag_and_drop(source_element, target_element)
        actions.perform()

    def wait_for_element_click(self, *locator):
        logger.info(f'Waiting for element click on {locator}')
        self.wait.until(
            EC.element_to_be_clickable(locator),
            message=f" Element by {locator} not clickable  "
        ).click()


    def wait_for_element_visibility(self, *locator):
        logger.info(f'Waiting for element to be visible {locator}')
        self.wait.until(
            EC.visibility_of_element_located(locator),
            message=f" Element by {locator} not visible "
        ).click()


    def wait_for_element(self, *locator):
        logger.info(f'Waiting for element {locator}')
        self.wait.until(
            EC.visibility_of_element_located(locator),
            message=f" Element by {locator} not visible  ")

    def wait_for_element_disappear(self, *locator):
        self.wait.until(
            EC.invisibility_of_element_located(locator),
            message=f" Element by {locator} still visible")

    def wait_for_url_contains(self, partial_url):
        self.wait.until(EC.url_contains(partial_url)
                        , message=f"Expected '{partial_url}' not in URL")

    def get_current_window_id(self):
        window = self.driver.current_window_handle
        logger.info(f"Original window: {window}")
        return window

    def switch_to_new_window(self):
        self.wait.until(EC.new_window_is_opened)
        all_windows = self.driver.window_handles
        logger.info(f"Switching to a new window: {all_windows[1]}")
        self.driver.switch_to.window(all_windows[1])

    def switch_to_window_by_id(self, window_id):
        logger.info(f"Switching to window: {window_id}")
        self.driver.switch_to.window(window_id)

    def close_window(self):
        self.driver.close()


    def click_outside(self,x_offset=10,y_offset=10):
          ActionChains(self.driver).move_by_offset(x_offset,y_offset).click().perform()
          ActionChains(self.driver).move_by_offset(-x_offset,-y_offset).perform()


    def verify_text(self, expected_text, *locator):
        actual_text = self.driver.find_element(*locator).text
        assert expected_text == actual_text, f"Expected text '{expected_text}' did not match '{actual_text}'"

    def verify_partial_text(self, expected_partial_text, *locator):
        actual_text = self.driver.find_element(*locator).text
        assert expected_partial_text in actual_text, \
            f"Expected text '{expected_partial_text}' not in  '{actual_text}'"

    def verify_url(self, expected_url):
        actual_url = self.driver.current_url
        logger.info('Current URL', actual_url)
        assert expected_url == actual_url, \
            f"Expected URL '{expected_url}' did not match actual URL '{actual_url}'"

    def verify_partial_url(self, expected_partial_url):
        actual_url = self.driver.current_url
        logger.info('Current URL', actual_url)
        assert expected_partial_url in actual_url, \
            f"Expected URL '{expected_partial_url}' in actual URL '{actual_url}'"

