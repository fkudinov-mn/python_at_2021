from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC


class BaseElement:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def get_element(self, locator, wait_time: int = 0):
        return WebDriverWait(self.driver, wait_time).until(EC.presence_of_element_located(locator))

    def get_elements(self, locator, wait_time: int = 0):
        try:
            WebDriverWait(self.driver, wait_time).until(EC.presence_of_element_located(locator))
        except:
            pass
        return self.driver.find_elements(*locator)
