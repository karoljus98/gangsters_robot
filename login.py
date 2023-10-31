from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from credentials import user_login, user_password
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('--headless=new')

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

def logging_in():
    """
    The function is responsible for logging in the user
    """
    driver.find_element(By.CSS_SELECTOR, '#login > div:nth-child(4) > input').send_keys(user_login)
    driver.find_element(By.CSS_SELECTOR, '#login > div:nth-child(6) > input').send_keys(user_password)
    driver.find_element(By.CSS_SELECTOR, '#login > div:nth-child(7) > input').click()
