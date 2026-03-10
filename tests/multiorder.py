from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from datetime import datetime
import pytz
import time
import random
import string




options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument("--start-fullscreen") 
driver = webdriver.Remote(
    command_executor='http://10.24.7.14:4444/wd/hub',
    options=options
)
# driver = webdriver.Chrome()
# driver.maximize_window()

try:
    wait = WebDriverWait(driver, 10)
    name_random = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase, k=8))
    password_random = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase, k=8))
    nomor_random = ''.join(random.choices(string.digits, k=11))
    nomor = "08" + nomor_random
    gmail = name_random + "@gmail.com"
    driver.get("https://posaja.posindonesia.co.id/dev/#top")
    time.sleep(10)

    username_input = driver.find_element(By.ID, "l_form1")
    password_input = driver.find_element(By.ID, "l_form2")
    username_input.clear()
    username_input.send_keys("email@gmail.com")
    password_input.clear()
    password_input.send_keys("100721")

    # --- Klik tombol login ---
    login_button = driver.find_element(By.ID, 'l_btn1')
    login_button.click()
    time.sleep(5)
    # driver.save_screenshot("output/loginberhasil.png")
    print("Uji Normal - Berhasil Login .")
    time.sleep(10)

    # test case order noncod
    
    multiorder_link = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//a[contains(@onclick, 'getData017')]")
    ))
    # Klik link "Order"
    multiorder_link.click()
    time.sleep(5)
    select_element = Select(driver.find_element(By.ID, 'f_form2'))
    select_element.select_by_visible_text('Pos Reguler')

    file_input = driver.find_element(By.ID, 'upload_file')
    # Kirimkan path file lokal ke input file
    # file_path = r"D:/Tools/selenium/PosajaWebDev/automationtestingposajaweb/tests/order.xls" 
    file_path = r"tests/order.xls"
     # Gunakan path absolut
    file_input.send_keys(file_path)
    time.sleep(5)

    upload = driver.find_element(By.ID, 'f_btn_upload')
    upload.click()
    time.sleep(5)
    # driver.save_screenshot("Berhasiluploadmultiorder.png")
    driver.save_screenshot("output/Berhasiluploadmultiorder.png")
    print("Normal Case - Multi Order Berhasil Dibuat")

    

    daftarorder = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//a[contains(@onclick, 'getData011')]")
    ))
    # Klik link "Order"
    daftarorder.click()
    time.sleep(5)

    label_tanggal = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//label[contains(., 'Tanggal')]"))
    )
    label_tanggal.click()

    # (Opsional) Tunggu setelah klik
    driver.implicitly_wait(2)

    tz = pytz.timezone('Asia/Jakarta')
    today = datetime.now(tz).strftime('%d-%m-%Y')
    print(today)
    tanggalawal = driver.find_element(By.ID, "tanggalawal")
    tanggalawal.clear()
    tanggalawal.send_keys(today)

    tanggalakhir = driver.find_element(By.ID, "tanggalawal2")
    tanggalakhir.clear()
    tanggalakhir.send_keys(today)

    cari = driver.find_element(By.ID, 'f_btn1')
    cari.click()
    time.sleep(5)
    
    print("Daftar order multiorder")
    # driver.save_screenshot("daftarordermultiorder.png")
    driver.save_screenshot("output/daftarordermultiorder.png")
    
finally:
    driver.quit()

