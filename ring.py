from login import driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from stripe_bar import stripe_bar

def ring():
    driver.find_element(By.ID, 'leftMenuIconRing').click()


def ring_fight(repeat):
    # A loop that performs the fight as many times as specified in the variable (repeat)
    for i in range(repeat):
        driver.find_element(By.CSS_SELECTOR,
                            '#s > div.centerBox > div:nth-child(4) > div:nth-child(3) > form > input.button').click()
        WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#attack-stripe-bg')))
        # Calling the stripe_bar function
        stripe_bar()
