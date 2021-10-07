from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://macreconline.ca/Program/GetProducts?classification=98e6c353-76bf-491c-951f-cdaa6d252a00")
link = driver.find_elements_by_class_name("list-group-item")
link[2].click()

try:
    # waits till the page is done loading before finding the element main
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.LINK_TEXT, "Log In"))
    )
    element.click()

    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, ".loginOption.btn-lg"))
    )
    element.click()
    user = driver.find_element_by_name("j_username")
    user.send_keys("enter username")
    password = driver.find_element_by_name("j_password")
    password.send_keys("enter password")

    login = driver.find_element_by_name("_eventId_proceed")
    login.click()

    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.NAME, "_shib_idp_consentIds"))
    )
    element.click()
    submit = driver.find_element_by_name("_eventId_proceed")
    submit.click()
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located(
            (By.CSS_SELECTOR, ".btn-primary"))
    )
    element[-3].click()
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.LINK_TEXT, "CONTINUE"))
    )
    element.click()
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located(
            (By.CSS_SELECTOR, ".btn-primary"))
    )
    element[-3].click()

    element = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located(
            (By.CSS_SELECTOR, ".btn-primary"))
    )
    print("the length is ", len(element))
    element[3].click()
    time.sleep(2)
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located(
            (By.CSS_SELECTOR, ".btn-primary"))
    )
    print("the length is ", len(element))
    element[4].click()
    time.sleep(5)

finally:
    driver.quit()
