# main.py
from login import login_to_linkedin
from scraper import search_jobs


def main():
    username = input("Enter your LinkedIn username: ")
    password = input("Enter your LinkedIn password: ")

    driver = login_to_linkedin(username, password)
    jobs = search_jobs(driver, 'Data Analyst')  # Example job search
    for job in jobs:
        print(f"Job Title: {job[0]}, Company: {job[1]}, Location: {job[2]}")

    driver.quit()


if __name__ == "__main__":
    main()
