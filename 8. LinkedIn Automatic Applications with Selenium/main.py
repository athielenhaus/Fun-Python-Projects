# SUMMARY: this program uses Selenium to automatically apply to EasyApply LinkedIn job postings (provided they follow a certain pattern)

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time

chrome_driver_path = "C:\Development\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_path)

# set LinkedIn job search URL - including parameters - for Selenium driver
driver.get("https://www.linkedin.com/jobs/search/?f_AL=true&geoId=102426246&keywords=marketing&location=Cologne%2C%20North%20Rhine-Westphalia%2C%20Germany")

# login to LinkedIn
driver.find_element_by_xpath("/html/body/header/nav/div/a[2]").click()

## NOTE- Code below will not work without entering the LinkedIn Email and Password

# login using Email and Username
driver.find_element_by_id("username").send_keys("xxxxxxxxxxxxxx")
driver.find_element_by_id("password").send_keys("xxxxxxxxxxxxxxxxxxxxxxxxxx")

# get element with list of jobs 
driver.find_element_by_xpath('//*[@id="organic-div"]/form/div[3]/button').click()
time.sleep(15)
job_list = driver.find_elements_by_class_name("job-card-container")

# go through jobs in list
for job in job_list:
    job.click()
    time.sleep(10)
    try:
        # Click EasyApply Button
        driver.find_element_by_class_name("jobs-apply-button").click()
    except NoSuchElementException:
        pass
    else:
        try:
            # Hit review button
            driver.find_element_by_css_selector("footer button").click()
            # Submit application
            for i in range(2):
                driver.find_elements_by_tag_name("footer button")[1].click()
        except NoSuchElementException:
            # If no review button, close menu
            driver.find_element_by_tag_name("button").click()
            # Discard application
            driver.find_elements_by_tag_name("footer button")[2].click()
