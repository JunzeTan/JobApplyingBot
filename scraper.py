# scraper.py
from selenium.webdriver.common.by import By
import time


def search_jobs(driver, keyword):
    driver.get(f"{BASE_URL}/jobs")

    # Wait for the elements to load
    time.sleep(3)

    job_search_box = driver.find_element(
        By.CLASS_NAME, 'jobs-search-box__text-input')
    job_search_box.send_keys(keyword)

    search_button = driver.find_element(
        By.CLASS_NAME, 'jobs-search-box__submit-button')
    search_button.click()

    time.sleep(5)  # wait for results to load

    jobs = driver.find_elements(By.CLASS_NAME, 'job-card-container')
    job_list = []
    for job in jobs:
        title = job.find_element(By.CLASS_NAME, 'job-card-list__title').text
        company = job.find_element(
            By.CLASS_NAME, 'job-card-container__company-name').text
        location = job.find_element(
            By.CLASS_NAME, 'job-card-container__metadata-item').text
        job_list.append((title, company, location))

    return job_list
