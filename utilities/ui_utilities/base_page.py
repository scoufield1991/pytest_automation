from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self._driver = driver
        self._wait = WebDriverWait(self._driver, 10)
        self._action_chains = ActionChains(driver)

    def __wait_element_visible(self, locator: tuple):
        return self._wait.until(EC.visibility_of_element_located(locator))

    def move_to_element(self, locator):
        element = self.__wait_element_visible(locator)
        self._action_chains.move_to_element(element).perform()

    def click(self, locator):
        self.__wait_element_visible(locator).click()

    def get_text_element(self, locator):
        element = self.__wait_element_visible(locator)
        text = element.text
        return text

    def scroll(self, locator):
        element = self.__wait_element_visible(locator)
        self._driver.execute_script("arguments[0].scrollIntoView();", element)

    def is_element_displayed(self, locator):
        return self.__wait_element_visible(locator).is_displayed()

    def get_url(self):
        return self._driver.current_url

    def send_keys(self, locator, value):
        element = self.__wait_element_visible(locator)
        element.send_keys(value)

    def clear(self, locator):
        element = self.__wait_element_visible(locator)
        element.clear()

