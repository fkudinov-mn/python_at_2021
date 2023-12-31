import pytest, os, textwrap, copy
from appium import webdriver

from selenium.webdriver.common.by import By as SeleniumBy

# depends on appium version
try:
    from appium.webdriver.common.appiumby import AppiumBy
except ImportError:
    from appium.webdriver.common.mobileby import MobileBy as AppiumBy


class By(AppiumBy, SeleniumBy):
    ...




EXECUTOR = 'http://127.0.0.1:4723/wd/hub'
ANDROID_BASE_CAPS = {
    'app': os.path.abspath('./tests/android_test/ApiDemos-debug.apk'),
    'platformName': 'Android',
    'automationName': 'UiAutomator2',
    "noSign": "true",
    'platformVersion': os.getenv('ANDROID_PLATFORM_VERSION') or '7.0',
    'deviceName': os.getenv('ANDROID_DEVICE_VERSION') or 'Android',
}


@pytest.fixture(scope='function')
def driver(request):
    calling_request = request._pyfuncitem.name

    caps = copy.copy(ANDROID_BASE_CAPS)
    caps['name'] = calling_request
    # caps['appActivity'] = SEARCH_ACTIVITY  # default activity

    driver = webdriver.Remote(command_executor=EXECUTOR,
                              desired_capabilities=caps)

    driver.implicitly_wait(10)
    yield driver
    driver.quit()


PACKAGE = 'io.appium.android.apis'
SEARCH_ACTIVITY = '.app.SearchInvoke'
ALERT_DIALOG_ACTIVITY = '.app.AlertDialogSamples'


def test_should_send_keys_to_search_box_and_then_check_the_value(driver):
    driver.start_activity(PACKAGE, SEARCH_ACTIVITY)
    search_box_element = driver.find_element(By.ID, 'txt_query_prefill')
    search_box_element.send_keys('Hello world!')

    on_search_requested_button = driver.find_element(By.ID, 'btn_start_search')
    on_search_requested_button.click()

    search_text = driver.find_element(By.ID, 'android:id/search_src_text')
    search_text_value = search_text.text

    assert 'Hello world!' == search_text_value


def test_should_click_a_button_that_opens_an_alert_and_then_dismisses_it(driver):
    driver.start_activity(PACKAGE, ALERT_DIALOG_ACTIVITY)

    open_dialog_button = driver.find_element(By.ID, 'io.appium.android.apis:id/two_buttons')
    open_dialog_button.click()

    alert_element = driver.find_element(By.ID, 'android:id/alertTitle')
    alert_text = alert_element.text

    assert textwrap.dedent('''\
    Lorem ipsum dolor sit aie consectetur adipiscing
    Plloaso mako nuto siwuf cakso dodtos anr koop.''') == alert_text

    close_dialog_button = driver.find_element(By.ID, 'android:id/button1')
    close_dialog_button.click()
