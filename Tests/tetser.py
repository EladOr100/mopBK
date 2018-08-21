
import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Tests import helper as report_logger





def func(x):
    return x + 1


@allure.severity(allure.severity_level.MINOR)
@allure.epic('BK Test')
@allure.feature('Feature1')
@allure.story('Story 0')
def test_fail():
    with allure.step('step failed'):
        report_logger.decorate_as_description("fjhsjdkfhskdjf")
        assert func(3) == 5


@allure.severity(allure.severity_level.CRITICAL)
@allure.epic('BK Test')
@allure.feature('Feature1')
@allure.story('Story 1 ')
def test_past():
    assert func(4) == 5


@allure.severity(allure.severity_level.CRITICAL)
@allure.epic('BK Test')
@allure.feature('Feature2')
@allure.story('Story 3')
def test_past222():
    assert func(34) == 5


@allure.severity(allure.severity_level.CRITICAL)
@allure.epic('BK Test')
@allure.feature('Feature3')
@allure.story('Story 77')
def test_pas222t():
    with allure.step("Verify Titlefkjdlgklfdjgkldfjgkldfjgkldfjgkldfgjdlkfjgldkfjgdlkfjgldkfjgldkjgslkfjgslkdgjsdlkgjsldkjgldskjgldskgjlskdjglsdkgjsldkjgf loaded"):
        assert func(43) == 5


@allure.severity(allure.severity_level.CRITICAL)
@allure.epic('Selenium Test')
@allure.feature('Feature google')
@allure.story('Story 77')
def test_site_loads():
    with allure.step("Launch site"):
        driver = webdriver.Chrome()
        driver.get("http://google.com/")
        assert ("Gookkkkkkkkkkkkkgle" == driver.title)
    with allure.step("Verify Title loaded"):
        wait = WebDriverWait(driver, 5)
        wait.until(EC.visibility_of_element_located((By.ID, "lst-ib")))
    with allure.step("Verify Title name is : " + driver.title):
        assert ("Googlgfdfge" == driver.title)
        allure.attach('screenshot', driver.get_screenshot_as_png(), attachment_type=AttachmentType.PNG)
