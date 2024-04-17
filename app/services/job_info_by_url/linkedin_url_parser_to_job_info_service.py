from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from ...schemas import ScrapedJobInfo

def linkedin_url_parser_to_job_info_service(url) -> ScrapedJobInfo:
    ## Open browser
    driver_path = "../chromedriver.exe"
    options = webdriver.ChromeOptions()
    options.add_argument('--disable-cache')
    options.add_argument('--ignore-certificate-errors')
    driver = webdriver.Chrome(options=options)
    driver.delete_all_cookies()

    # Maximizing browser window to avoid hidden elements
    driver.maximize_window()

    ## Opening jobs webpage
    driver.get(url)
    ## waiting load
    driver.delete_all_cookies()
    see_more = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, 'show-more-less-html__button')))
    see_more.click()


    jobs_title = driver.find_element(By.CLASS_NAME, "top-card-layout__title")
    print(jobs_title.text)

    company =  driver.find_elements(By.CSS_SELECTOR, ".topcard__org-name-link")
    comapny_name =''
    for e in company:
        comapny_name += e.text
    locatin = driver.find_elements(By.CSS_SELECTOR, ".topcard__flavor")
    locatio_text = ''
    for e in locatin:
        locatio_text=e.text
    time.sleep(2)
    dec =  driver.find_elements(By.CLASS_NAME, "decorated-job-posting__details")

    job_desc = ''
    for e in dec:
        job_desc += e.text

    job_desc = job_desc.split('Show less')[0]

    #driver.quit()
    return ScrapedJobInfo(title=jobs_title.text, desc=job_desc, comapany=comapny_name, location=locatio_text)




            