from selenium.webdriver.common.keys import Keys

url = 'https://demoqa.com/automation-practice-form'

# locators
css_fname = '#firstName'
css_lname = '#lastName'
css_email = '#userEmail'
css_phone = '#userNumber'
css_date_of_birth = '#dateOfBirthInput'
css_subjects = '#subjectsInput'
css_current_address = '#currentAddress'
css_state = "#react-select-3-input"
css_city = "#react-select-4-input"
css_gender = '.custom-control.custom-radio.custom-control-inline'
css_checkbox_hobbies = '.custom-control.custom-checkbox.custom-control-inline'
css_submit_button = '#submit'

# data
fname = 'name'
lname = 'lname'
email = 'test@test.com'
phone = '1234567890'
subjects = 'English'
current_address = 'test address'
state = 'NCR'
city = 'Delhi'
gender = 'Male'
hobbies = 'Sports'


def test_form(driver_init):
    driver_init.get(url)

    filled_locators = {css_fname: fname, css_lname: lname, css_email: email,
                       css_phone: phone, css_current_address: current_address}

    for k, v in filled_locators.items():
        locator = driver_init.find_element_by_css_selector(k)
        locator.clear()
        locator.send_keys(v)

    gender_locator = driver_init.find_element_by_css_selector(css_gender).click()
    hobbies_locator = driver_init.find_element_by_css_selector(css_checkbox_hobbies).click()

    subjects_locator = driver_init.find_element_by_css_selector(css_subjects)
    subjects_locator.send_keys(subjects)
    subjects_locator.send_keys(Keys.RETURN)

    state_locator = driver_init.find_element_by_css_selector(css_state)
    state_locator.send_keys(state)
    state_locator.send_keys(Keys.RETURN)

    city_locator = driver_init.find_element_by_css_selector(css_city)
    city_locator.send_keys(city)
    city_locator.send_keys(Keys.RETURN)

    # scroll
    driver_init.execute_script("window.scrollTo(0,document.body.scrollHeight)")

    submit = driver_init.find_element_by_css_selector(css_submit_button).click()

    table = driver_init.find_elements_by_css_selector('.table-responsive tr td')
    actual_result = [i.text for i in table]

    expected = {fname + ' ' + lname, email, gender, phone, subjects, hobbies, current_address, state + ' ' + city}

    assert expected.issubset(actual_result)
