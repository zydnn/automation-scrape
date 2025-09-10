from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time

# === SETUP DRIVER ===
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)

# === BUKA HALAMAN ===
driver.get("http://157.66.14.118:5000/oxysystem-ppm/ims/general/customer.jsp")
print("👉 Login manual jika ada, lalu tekan ENTER di terminal...")
input()

all_data = []
page = 1
prev_first_row = None

while True:
    print(f"📄 Scraping page {page}...")

    # cari tabel utama (class=listgen)
    table = driver.find_element(By.CSS_SELECTOR, "table.listgen")
    rows = table.find_elements(By.TAG_NAME, "tr")

    # skip row pertama (header)
    for row in rows[1:]:
        cols = [c.text.strip() for c in row.find_elements(By.TAG_NAME, "td")]
        if cols:
            all_data.append(cols)

    # check apakah udah di last page
    first_row = rows[1].text if len(rows) > 1 else None
    if first_row == prev_first_row:
        print("✅ Udah sampai last page.")
        break
    prev_first_row = first_row

    # auto klik tombol Next
    driver.execute_script("cmdListNext()")
    time.sleep(2)
    page += 1

# === SIMPAN KE EXCEL ===
df = pd.DataFrame(all_data, columns=["Type", "Code", "Name", "Address", "Province", "State", "Area", "Phone"])
df.to_excel("customers.xlsx", index=False)

driver.quit()
print("🎉 Export selesai! File tersimpan: customers.xlsx")