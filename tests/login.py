from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import random
import string



options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument("--start-fullscreen") 

# driver = webdriver.Remote(
#     command_executor='http://10.24.7.14:4444/wd/hub',
#     options=options
# )
driver = webdriver.Chrome()
driver.maximize_window()

try:
    # --- AbNormal case ---
    wait = WebDriverWait(driver, 10)
    name_random = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase, k=8))
    password_random = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase, k=8))
    nomor_random = ''.join(random.choices(string.digits, k=11))
    nomor = "08" + nomor_random
    gmail = name_random + "@gmail.com"
    # ---test case 1
    driver.get("https://posaja.posindonesia.co.id/dev/#top")
    time.sleep(5)

    username_input = driver.find_element(By.ID, "l_form1")
    password_input = driver.find_element(By.ID, "l_form2")

    username_input.send_keys(gmail)
    password_input.send_keys(password_random)

    login_button = driver.find_element(By.ID, 'l_btn1')
    login_button.click()
    time.sleep(5)
    driver.save_screenshot("output/EmailorPasswordisWrong.png")
    # driver.save_screenshot("Email or Password is Wrong.png")
    # driver.save_screenshot("output/loginerroremail.png")
    print("Uji AbNormal - Email or Password is Wrong .")
    # tes case 2
    driver.get("https://posaja.posindonesia.co.id/dev/#top")
    time.sleep(5)

    username_input = driver.find_element(By.ID, "l_form1")
    password_input = driver.find_element(By.ID, "l_form2")
    username_input.clear()
    username_input.send_keys("agungprakasa49@gmail.com")
    password_input.clear()
    password_input.send_keys("100721")

    # --- Klik tombol login ---
    login_button = driver.find_element(By.ID, 'l_btn1')
    login_button.click()
    time.sleep(5)
    # driver.save_screenshot("loginberhasil.png")
    driver.save_screenshot("output/loginberhasil.png")
    print("Uji Normal - Berhasil Login .")
    
finally:
    driver.quit()
