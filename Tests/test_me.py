import allure
import pytest
import unittest
from backEnd import devFunctions as beck_end_func
from FrontEnd import seleniumFunctions as front_end_func
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from Functions import yaml_parser as y_parser
from allure_commons.types import AttachmentType

login_repo = "D:\python\FinalReport\configFiles\login_repo"
login_repo_data = "D:\python\FinalReport\configFiles\login_repo_data"
driver = webdriver.Chrome()
add_one = 5
add_two = 5
add_expected_pass = 10
add_expected_fail = 20
sub_expected_pass = 0
sub_expected_fail = 20
website_url = y_parser.yaml_data_parser(login_repo_data, "url")


# website_url = "http://10.32.5.73/ui/"

@pytest.fixture
def setup():
    driver.get("google")


@allure.severity(allure.severity_level.CRITICAL)
@allure.epic('Front-End Test')
@allure.feature('login')
@allure.story('check google search window')
def test_search_in_python_org():
    with allure.step("open the website"):
        front_end_func.open_site(website_url, driver)
        front_end_func.send_keys_by_xpath(driver, y_parser.yaml_data_parser(login_repo, "username"),
                                          y_parser.yaml_data_parser(login_repo_data, "username"))

        elem = driver.find_element_by_name("q")
        elem.send_keys("Elad Or")
        elem.send_keys(Keys.RETURN)
        front_end_func.take_screen_shot(driver, "Elad Or")
        assert "No results found." not in driver.page_source


@allure.severity(allure.severity_level.CRITICAL)
@allure.epic('Front-End Test')
@allure.feature('Feature google')
@allure.story('check google title')
def test_site_loads():
    with allure.step("Launch site"):
        driver.get("http://google.com/")
        front_end_func.take_screen_shot(driver, "title")
        allure.step("check google title and take screenshots")

        assert ("Google" == driver.title)


@allure.severity(allure.severity_level.NORMAL)
@allure.epic('Back-End Test')
@allure.feature('ADD')
@allure.story('check the add function')
def test_add():
    with allure.step("check 2 parameters :" + str(add_two) + " and :" + str(
            add_one) + " the expected rez is: " + str(add_expected_pass)):
        actual = beck_end_func.add(add_one, add_two)
        assert actual == add_expected_pass, "the expected data is : " + str(add_expected_pass) + " and we got :" + str(
            actual)

    with allure.step("check 2 parameters :" + str(add_two) + " and :" + str(
            add_one) + " the expected rez is: " + str(add_expected_pass)):
        actual = beck_end_func.add(add_one, add_two)
        assert actual == add_expected_pass, "the expected data is : " + str(add_expected_pass) + " and we got :" + str(
            actual)

    with allure.step("check 2 parameters :" + str(add_two) + " and :" + str(
            add_one) + " the expected rez is: " + str(add_expected_fail)):
        actual = beck_end_func.add(add_one, add_two)
        assert actual == add_expected_fail, "the expected data is : " + str(add_expected_fail) + " and we got :" + str(
            actual)


@allure.severity(allure.severity_level.CRITICAL)
@allure.epic('Back-End Test')
@allure.feature('SUB')
@allure.story('check the sub function')
def test_sub():
    with allure.step("check 2 parameters from user:" + str(add_two) + " and :" + str(
            add_one) + " the expected rez is: " + str(sub_expected_pass)):
        actual = beck_end_func.sub(add_one, add_two)
        assert actual == sub_expected_pass, "the expected data is : " + str(sub_expected_pass) + " and we got :" + str(
            actual)

    with allure.step("check 2 parameters :" + str(add_two) + " and :" + str(
            add_one) + " the expected rez is: " + str(sub_expected_pass)):
        actual = beck_end_func.sub(add_one, add_two)
        assert actual == sub_expected_pass, "the expected data is : " + str(sub_expected_pass) + " and we got :" + str(
            actual)

    with allure.step("check 2 parameters :" + str(add_two) + " and :" + str(
            add_one) + " the expected rez is: " + str(add_expected_fail)):
        actual = beck_end_func.sub(add_one, add_two)
        assert actual == add_expected_fail, "the expected data is : " + str(add_expected_fail) + " and we got :" + str(
            actual)



if __name__ == '__main__':
    unittest.main()