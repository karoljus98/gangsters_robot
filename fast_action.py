

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from login import driver
from selenium.webdriver.common.by import By
from stripe_bar import stripe_bar


def fast_action():
    driver.find_element(By.ID, 'leftMenuIconSzybka akcja').click()


def fast_action_make(repeat, category, which_action, multiplied):
    """
    :param repeat: How many times you want to repeat fast_action?
    :param category: Which level of dificulty you want to choose?
    :param which_action: Which action you want to choose?
    :param multiplied: How many times should the action be performed at once?
    :return:
    """

    driver.find_element(By.CSS_SELECTOR, '#typeForm > select').click()
    driver.find_element(By.CSS_SELECTOR, f'#typeForm > select > option:nth-child({category})').click()
    driver.find_element(By.CSS_SELECTOR, '#saForm > select:nth-child(3)')
    driver.find_element(By.CSS_SELECTOR, f'#saForm > select:nth-child(3) > option:nth-child({which_action})').click()
    driver.find_element(By.CSS_SELECTOR, '#saForm > select:nth-child(6)')
    driver.find_element(By.CSS_SELECTOR, f'#saForm > select:nth-child(6) > option:nth-child({multiplied})').click()

    # A loop that performs the action as many times as specified in the variable (repeat)
    for i in range(repeat):
        driver.find_element(By.CSS_SELECTOR, '#saForm > input.buttonBigRed').click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#attack-stripe-bg')))
        # Calling the stripe_bar function
        stripe_bar()