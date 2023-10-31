from login import driver
from selenium.webdriver.common.by import By
from selenium.common import exceptions


def stripe_bar():
    """
    The feature provides support for the attack bar
    """
    attack_stripe_bg = driver.find_element(By.CSS_SELECTOR, '#attack-stripe-bg')
    changing_element = driver.find_element(By.CSS_SELECTOR, '#attack-stripe-bar')

    flag = True

    while flag:
        for i in range(10):
            try:
                # A loop that is getting value from element attribute name 'style'
                for value in changing_element.get_attribute('style').split(';'):
                    if 'top' in value:
                        top_value = float(value.split(':')[-1].strip().replace('px', ''))
                        if top_value == 0:
                            attack_stripe_bg.click()
                            flag = False
            except exceptions.StaleElementReferenceException:
                pass
