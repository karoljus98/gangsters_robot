from login import driver
from selenium.webdriver.common.by import By


def gym():
    driver.find_element(By.ID, 'leftMenuIconSiłownia').click()

# multiplied is a string value which tells how many points yopu want to add in one training

def atlas(repeat, multiplied: str):
    # A loop that performs the action as many times as specified in the variable (repeat)
    for i in range(repeat):
        driver.find_element(By.XPATH, '//*[@id="s"]/div[2]/div/div[2]/div[1]/form/div[1]/div[3]/input[1]').send_keys(
            multiplied)
        driver.find_element(By.XPATH, '//*[@id="s"]/div[2]/div/div[2]/div[1]/form/div[1]/div[3]/input[2]').click()


def treadmill(repeat, multiplied: str):
    # A loop that performs the action as many times as specified in the variable (repeat)
    for i in range(repeat):
        driver.find_element(By.XPATH, '//*[@id="s"]/div[2]/div/div[2]/div[2]/form/div[1]/div[3]/input[1]').send_keys(
            multiplied)
        driver.find_element(By.XPATH, '//*[@id="s"]/div[2]/div/div[2]/div[2]/form/div[1]/div[3]/input[2]').click()


def rower(repeat, multiplied: str):
    # A loop that performs the action as many times as specified in the variable (repeat)
    for i in range(repeat):
        driver.find_element(By.XPATH, '//*[@id="s"]/div[2]/div/div[2]/div[3]/form/div[1]/div[3]/input[1]').send_keys(
            multiplied)
        driver.find_element(By.XPATH, '//*[@id="s"]/div[2]/div/div[2]/div[3]/form/div[1]/div[3]/input[2]').click()


def bench(repeat, multiplied: str):
    # A loop that performs the action as many times as specified in the variable (repeat)
    for i in range(repeat):
        driver.find_element(By.CSS_SELECTOR,
                            '#s > div.centerBox > div > div:nth-child(3) > div:nth-child(5) > form > div:nth-child(2) '
                            '> div:nth-child(3) > input.text').send_keys(
            multiplied)
        driver.find_element(By.CSS_SELECTOR,
                            '#s > div.centerBox > div > div:nth-child(3) > div:nth-child(5) > form > div:nth-child(2) '
                            '> div:nth-child(3) > input.button').click()


def atlas_max(repeat, multiplied: str):
    # A loop that performs the action as many times as specified in the variable (repeat)
    for i in range(repeat):
        driver.find_element(By.XPATH, '//*[@id="s"]/div[2]/div/div[2]/div[5]/form/div[1]/div[3]/input[1]').send_keys(
            multiplied)
        driver.find_element(By.XPATH, '//*[@id="s"]/div[2]/div/div[2]/div[5]/form/div[1]/div[3]/input[2]').click()
