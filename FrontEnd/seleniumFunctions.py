import allure
from allure_commons.types import AttachmentType
import selenium.webdriver.support.ui as ui


def open_site(url, driver):
    driver.get(url)
    driver.maximize_window()


def check_site_title(driver, site_name):
    assert driver.title == site_name, "the expected data is : " + driver.title + " and we got :" + site_name


def take_screen_shot(driver, image_name):
    allure.attach(driver.get_screenshot_as_png(), name=image_name, attachment_type=AttachmentType.PNG)


def click_element_by_class_name(driver, class_name):
    w_element = driver.find_element_by_class_name(class_name)
    highlight(driver, w_element)
    w_element.click()


def click_element_by_xpath(driver, xpath):
    w_element = driver.find_element_by_xpath(xpath)
    highlight(driver, w_element)
    w_element.click()


def send_keys_by_xpath(driver, xpath, data):
    w_element = driver.find_element_by_xpath(xpath)
    highlight(driver, w_element)
    w_element.send_keys(data)


def highlight(driver, element):
    driver.execute_script("arguments[0].style.border='3px solid red'",
                          element)


def wait_for_element_by_xpath(driver, xpath):
    wait = ui.WebDriverWait(driver, 10)
    try:
        wait.until(driver.find_element_by_xpath(xpath))
    except ValueError:
        allure.attach("wait for the element but he did not  came :(", 'cant find element error', allure.attachment_type.TEXT)
