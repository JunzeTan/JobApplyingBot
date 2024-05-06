# login.py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from config import BASE_URL


def login_to_linkedin(username, password):
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get(f"{BASE_URL}/login")

    username_field = driver.find_element(By.ID, 'session_key')
    username_field.send_keys(username)

    password_field = driver.find_element(By.ID, 'session_password')
    password_field.send_keys(password)

    login_button = driver.find_element(
        By.CLASS_NAME, 'sign-in-form__submit-button')
    login_button.click()

    return driver
