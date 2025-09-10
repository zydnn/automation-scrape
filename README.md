# Data Scraper

Script ini dibuat untuk **mengekspor data customer dan sebagainya** dari sistem internal yang biasanya hanya bisa dilihat dalam row tertentu.  
Dengan script ini, semua data (1000+ customer) bisa di-scrape otomatis dan diekspor ke file **Excel (`namaFile.xlsx`)**.

## 🚀 Fitur
- Scraping tabel `listgen` (hanya data customer, tabel lain tidak keikut).
- Auto navigasi semua halaman via `cmdListNext()` dll.
- Output langsung ke **Excel** dengan struktur kolom:
  - Type
  - Code
  - Name
  - Address
  - Province
  - State
  - Area
  - Phone
  - (bisa di ganti)

## 📦 Requirements
- Python **3.8+**
- Google Chrome (terbaru)
- [ChromeDriver](https://chromedriver.chromium.org/downloads) (sesuai versi Chrome lo)
- Python libraries:
  ```bash
  pip install selenium pandas openpyxl
