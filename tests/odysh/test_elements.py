import pytest
from selenium.webdriver.common.by import By
from .constants import HOST


ELEMENTS_PAGE = "elements"


@pytest.mark.text_box
def test_positive_registration_form(driver):
    driver.get(HOST + ELEMENTS_PAGE)
    driver.find_element(By.CLASS_NAME, "text").click()
    driver.find_element(By.ID, "userName").send_keys('Human')
    driver.find_element(By.ID, "userEmail").send_keys('some@email.com')
    driver.find_element(By.CSS_SELECTOR, "#currentAddress").send_keys('Milky Way')
    driver.find_element(By.ID, "permanentAddress").send_keys('Earth')
    driver.find_element(By.CSS_SELECTOR, "#submit").click()
    assert driver.find_element(By.XPATH, "//p[@id='name']").text[5:] == 'Human'
    assert driver.find_element(By.XPATH, "//p[@id='email']").text[6:] == 'some@email.com'
    assert driver.find_element(By.XPATH, "//p[@id='currentAddress']").text[-9:] == 'Milky Way'
    assert driver.find_element(By.XPATH, "//p[@id='permanentAddress']").text[-5:] == 'Earth'
