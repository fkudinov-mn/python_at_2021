from typing import Tuple, List
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webdriver import WebElement
from python_at_2021.tests.akaiafiuk.constants import HOST


class BasePage:
    url = ''

    def __init__(self, session: WebDriver):
        self.host = HOST
        self.session = session

    def open(self):
        self.session.get(self.host + self.url)
        return self

    def find_element(self, by: Tuple[By, str]) -> WebElement:
        return self.session.find_element(*by)

    def find_elements(self, by: Tuple[By, str]) -> List[WebElement]:
        return self.session.find_elements(*by)

    def refresh_page(self):
        self.session.refresh()

    def get_header(self):
        # todo: return Header
        ...
