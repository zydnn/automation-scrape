# Customer Data Scraper

Script ini dibuat untuk **mengekspor data customer** dari sistem internal (`oxysystem-ppm`) yang biasanya hanya bisa dilihat 20 row per halaman.  
Dengan script ini, semua data (3900+ customer) bisa di-scrape otomatis dan diekspor ke file **Excel (`customers.xlsx`)**.

## 🚀 Fitur
- Scraping tabel `listgen` (hanya data customer, tabel lain tidak keikut).
- Auto navigasi semua halaman via `cmdListNext()`.
- Output langsung ke **Excel** dengan struktur kolom:
  - Type
  - Code
  - Name
  - Address
  - Province
  - State
  - Area
  - Phone

## 📦 Requirements
- Python **3.9+**
- Google Chrome (terbaru)
- [ChromeDriver](https://chromedriver.chromium.org/downloads) (sesuai versi Chrome lo)
- Python libraries:
  ```bash
  pip install selenium pandas openpyxl
