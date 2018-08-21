import allure
import pytest

from backEnd import devFunctions as beck_end_func
from FrontEnd import seleniumFunctions as front_end_func
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from Functions import yaml_parser as y_parser
from allure_commons.types import AttachmentType

login_repo = "configFiles/login_repo"
login_repo_data = "configFiles/login_repo_data"
dashboard_repo_data = "configFiles/dashboard_repo"
driver = webdriver.Chrome()
website_url = y_parser.yaml_data_parser(login_repo_data, "url")


@classmethod
def teardown_class(cls):
    driver.close()


@allure.description("This test is going to check the login function ")
@allure.severity(allure.severity_level.CRITICAL)
@allure.epic('Front-End Test')
@allure.feature('login')
@allure.story('check login window')
def test_login_to_site():
    with allure.step("open the website"):
        front_end_func.open_site(website_url, driver)
        front_end_func.send_keys_by_xpath(driver, y_parser.yaml_data_parser(login_repo, "username"),
                                          y_parser.yaml_data_parser(login_repo_data, "username"))

        front_end_func.send_keys_by_xpath(driver, y_parser.yaml_data_parser(login_repo, "password"),
                                          y_parser.yaml_data_parser(login_repo_data, "password"))

        front_end_func.take_screen_shot(driver, "Login")

        front_end_func.click_element_by_xpath(driver, y_parser.yaml_data_parser(login_repo, "submit_button"))

        allure.attach('here you`ll see the actual title :' + driver.title, 'title assert', allure.attachment_type.TEXT)
        front_end_func.check_site_title(driver, y_parser.yaml_data_parser(login_repo_data, "title"))


@allure.description("This test is going to check the login function ")
@allure.severity(allure.severity_level.CRITICAL)
@allure.epic('Front-End Test')
@allure.feature('login')
@allure.story('check login  window')
def test_login_to_site_fail():
    with allure.step("open the website"):
        front_end_func.open_site(website_url, driver)
        front_end_func.send_keys_by_xpath(driver, y_parser.yaml_data_parser(login_repo, "username"),
                                          y_parser.yaml_data_parser(login_repo_data, "username"))

        front_end_func.send_keys_by_xpath(driver, y_parser.yaml_data_parser(login_repo, "password"),
                                          y_parser.yaml_data_parser(login_repo_data, "password"))

        front_end_func.take_screen_shot(driver, "Login")

        front_end_func.click_element_by_xpath(driver, y_parser.yaml_data_parser(login_repo, "submit_button"))

        allure.attach('here you`ll see the actual title :' + driver.title, 'title assert', allure.attachment_type.TEXT)
        front_end_func.check_site_title(driver, y_parser.yaml_data_parser(login_repo_data, "title_failure"))


@allure.description("This test is going to check the login function ")
@allure.severity(allure.severity_level.CRITICAL)
@allure.epic('Front-End Test')
@allure.feature('login')
@allure.story('check login window')
def test_login_to_site_fail_username():
    with allure.step("open the website"):
        front_end_func.open_site(website_url, driver)
        front_end_func.send_keys_by_xpath(driver, y_parser.yaml_data_parser(login_repo, "username"),
                                          y_parser.yaml_data_parser(login_repo_data, "username_fails"))

        front_end_func.send_keys_by_xpath(driver, y_parser.yaml_data_parser(login_repo, "password"),
                                          y_parser.yaml_data_parser(login_repo_data, "password_fails"))

        front_end_func.take_screen_shot(driver, "Login")

        front_end_func.click_element_by_xpath(driver, y_parser.yaml_data_parser(login_repo, "submit_button"))

        allure.attach('here you`ll see the actual title :' + driver.title, 'title assert', allure.attachment_type.TEXT)
        front_end_func.check_site_title(driver, y_parser.yaml_data_parser(login_repo_data, "title"))

        front_end_func.wait_for_element_by_xpath(driver,
                                                 y_parser.yaml_data_parser(dashboard_repo_data, "add_entities_button"))
