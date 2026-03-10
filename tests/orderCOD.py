from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
import random
import string
import time
import os
import datetime
import traceback
import requests



# options = Options()
# options.add_argument('--headless')
# options.add_argument('--no-sandbox')
# options.add_argument('--disable-dev-shm-usage')
# options.add_argument("--start-fullscreen") 
# driver = webdriver.Remote(
#     command_executor='http://10.24.7.14:4444/wd/hub',
#     options=options
# )
driver = webdriver.Chrome()
driver.maximize_window()

# === KONFIG TELEGRAM ===
BOT_TOKEN = 'token'   # Ganti token kamu
CHAT_ID = '-4800804566'               # Ganti chat ID kamu

# === FOLDER ===
os.makedirs("logs", exist_ok=True)
os.makedirs("screenshots", exist_ok=True)

def kirim_file_ke_telegram(filepath, caption):
    url = f'https://api.telegram.org/bot{BOT_TOKEN}/sendDocument'
    with open(filepath, 'rb') as f:
        files = {'document': f}
        data = {'chat_id': CHAT_ID, 'caption': caption}
        requests.post(url, files=files, data=data)
    print(f"✅ File dikirim ke Telegram: {filepath}")

def handle_error(driver, err):
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

    # === Screenshot ===
    screenshot_path = f"screenshots/error_{timestamp}.png"
    driver.save_screenshot(screenshot_path)
    print(f"[!] Screenshot disimpan: {screenshot_path}")

    # === Simpan Log Error ===
    log_path = f"logs/error_{timestamp}.txt"
    with open(log_path, "w", encoding="utf-8") as log_file:
        log_file.write("Traceback:\n")
        log_file.write(traceback.format_exc())
        log_file.write("\n\nURL saat error:\n")
        try:
            log_file.write(driver.current_url)
        except:
            log_file.write("Gagal mengambil URL")

    print(f"[!] Log disimpan: {log_path}")

    # === Kirim ke Telegram ===
    kirim_file_ke_telegram(screenshot_path, "📸 Screenshot error Selenium")
    kirim_file_ke_telegram(log_path, "📝 Log error Selenium")

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
    username_input.send_keys("agungprakasa49@gmail.com")
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
    
    order_link = wait.until(EC.element_to_be_clickable(
    (By.XPATH, "//a[contains(@onclick, 'getDataOrder001')]")
    ))
    # Klik link "Order"
    order_link.click()
    time.sleep(5)
    
    select_element = Select(driver.find_element(By.ID, 'form33Cod'))
    select_element.select_by_visible_text('COD')
    NilaiCOD = driver.find_element(By.ID, "form34NCod")
    NilaiCOD.clear()
    NilaiCOD.send_keys("1000000")

    
    Nama = driver.find_element(By.ID, "form15")
    alamat = driver.find_element(By.ID, "form16")
    Nama.clear()
    Nama.send_keys("Agung Prakasa")
    alamat.clear()
    alamat.send_keys("Gang reuma kidul 2 no 75b")

    input_box = wait.until(EC.presence_of_element_located((By.ID, 'form1')))
    # Input '40115'
    input_box.clear()
    input_box.send_keys('Kel. CITARUM Kec. BANDUNG WETAN, KOTA BANDUNG - 40115')

    # Tunggu sampai hasil autocomplete muncul
    # autocomplete_option = wait.until(EC.visibility_of_element_located(
    #     (By.XPATH, "//li[contains(text(), 'Kel. CITARUM Kec. BANDUNG WETAN, KOTA BANDUNG - 40115')]")
    # ))
    # time.sleep(5)
    telepon_pengirim = driver.find_element(By.ID, "form17")
    email_pengirim = driver.find_element(By.ID, "form22email")
    telepon_pengirim.clear()
    telepon_pengirim.send_keys("088218320463")
    email_pengirim.clear()
    email_pengirim.send_keys("agungprakasa49@gmail.com")
# ------------------------------------------------------------
    Nama_penerima = driver.find_element(By.ID, "form18")
    alamat_penerima = driver.find_element(By.ID, "form19")
    Nama_penerima.clear()
    Nama_penerima.send_keys("Martindes")
    alamat_penerima.clear()
    alamat_penerima.send_keys("Rumah bunda maria")

    input_box = wait.until(EC.presence_of_element_located((By.ID, 'form2')))
    # Input '40115'
    input_box.clear()
    input_box.send_keys('Kel. BRAGA Kec. SUMUR BANDUNG, KOTA BANDUNG - 40111')

    # Tunggu sampai hasil autocomplete muncul
    # autocomplete_option = wait.until(EC.visibility_of_element_located(
    #     (By.XPATH, "//li[contains(text(), 'Kel. CITARUM Kec. BANDUNG WETAN, KOTA BANDUNG - 40115')]")
    # ))
    # time.sleep(5)
    telepon_penerima = driver.find_element(By.ID, "form20")
    email_penerima = driver.find_element(By.ID, "form21email")
    telepon_penerima.clear()
    telepon_penerima.send_keys("088218320463")
    email_penerima.clear()
    email_penerima.send_keys("martindes@gmail.com")

    
    berat = driver.find_element(By.ID, "form3")
    berat.clear()
    berat.send_keys("1000")
    select_element = Select(driver.find_element(By.ID, 'form22'))
    select_element.select_by_visible_text('PAKET')
    p = driver.find_element(By.ID, "form4")
    p.clear()
    p.send_keys("5")
    l = driver.find_element(By.ID, "form5")
    l.clear()
    l.send_keys("5")
    t = driver.find_element(By.ID, "form6")
    t.clear()
    t.send_keys("5")
    nilai_barang = driver.find_element(By.ID, "form7")
    nilai_barang.clear()
    nilai_barang.send_keys("1000000")
    ket_kiriman = driver.find_element(By.ID, "form12")
    ket_kiriman.clear()
    ket_kiriman.send_keys("COD MOHON DIKIRIM")
    
    checkbox = wait.until(EC.element_to_be_clickable((By.ID, 'chk2')))

    # Klik checkbox
    checkbox.click()
    cek_tarif = driver.find_element(By.ID, 'btn1')
    cek_tarif.click()
    time.sleep(10)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    driver.save_screenshot("output/Cek_tarif.png")

    checkbox = driver.find_element(By.ID, "chkval")
    checkbox.click()

    button_ids = ['l_btn-1', 'l_btn-2', 'l_btn-3', 'l_btn-4']
    clicked = False
    for btn_id in button_ids:
        try:
            button = wait.until(EC.element_to_be_clickable((By.ID, btn_id)))
            button.click()
            print(f"Tombol dengan ID '{btn_id}' diklik.")
            clicked = True
            break  # Keluar dari loop setelah berhasil klik
        except:
            continue  # Jika tidak ditemukan, lanjut ke ID berikutnya

    if not clicked:
        print("Tidak ada tombol yang tersedia dari daftar ID.")
    
    # order_reguler = driver.find_element(By.ID, 'l_btn-1')
    # order_reguler.click()
    alert = driver.switch_to.alert
    # print("Isi alert:", alert.text)  # Opsional: tampilkan isi pesan alert
    alert.accept()
    time.sleep(10)
    driver.save_screenshot("output/BerhasilOrderCOD.png")
    # driver.save_screenshot("Berhasil Order.png")
    cetak_label = driver.find_element(By.ID, 'f_btn_cetak')
    cetak_label.click()
    time.sleep(10)
    driver.save_screenshot("output/CetakanOrderCOD.png")
    # driver.save_screenshot("Cetakan Order NON COD.png")
    print("Uji Normal - Order COD berhasil")
except Exception as e:
    print("[!] Terjadi ERROR:")
    traceback.print_exc()
    handle_error(driver, e)
    
finally:
    driver.quit()

