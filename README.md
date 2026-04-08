# 🌍 Web Scraping Data Negara

Project ini merupakan program Python untuk melakukan web scraping data negara dari sebuah website, kemudian menyimpannya ke dalam format JSON dan CSV. Selain itu, project ini dilengkapi dengan fitur CRUD (Create, Read, Update, Delete) untuk mengelola data.

---

## 📌 Deskripsi
Project ini dibuat untuk memenuhi tugas mata kuliah dengan menerapkan konsep **data pipeline (Extract, Transform, Load)** menggunakan Python.

---

## 🎯 Tujuan
- Mengambil data dari website menggunakan web scraping
- Membersihkan dan mengolah data
- Menyimpan data ke dalam format JSON dan CSV
- Mengelola data menggunakan sistem CRUD

---

## 🌐 Sumber Data
Data diambil dari:
https://www.scrapethissite.com/pages/simple/

Data yang diambil:
- Nama negara
- Ibu kota
- Populasi
- Luas wilayah

---

## ⚙️ Teknologi yang Digunakan
- Python
- requests
- BeautifulSoup (bs4)
- JSON
- CSV

---

## 🔄 Alur Program (Data Pipeline)

1. **Extract**
   - Mengambil data dari website menggunakan `requests`

2. **Transform**
   - Membersihkan data (strip, konversi tipe data)

3. **Load**
   - Menyimpan data ke:
     - `countries.json`
     - `countries.csv`

---

## 📂 Struktur Project

scraping.py → proses scraping data

crud.py → fitur CRUD

countries.json → hasil data JSON

countries.csv → hasil data CSV


---

## ▶️ Cara Menjalankan

### 1. Install dependency
```
pip install requests beautifulsoup4
```
### 2. Jalankan scraping
```
python scraping.py
```
### 3. Jalankan CRUD
```
python crud.py
```
📊 Output

Program menghasilkan:

- countries.json (format JSON)
- countries.csv (format CSV)

Contoh data:

```
{
  "negara": "Indonesia",
  "ibu_kota": "Jakarta",
  "populasi": 273523615,
  "luas": 1910931.0
}
```
---

## 🧪 Fitur CRUD

- Menambahkan data negara
- Menampilkan seluruh data
- Mengupdate data
- Menghapus data

---

## 📌 Catatan
- Data digunakan untuk keperluan pembelajaran
- Website yang digunakan adalah situs latihan scraping

---

## 🔗 Link Repository GitHub
https://github.com/Fikricakra/python-data-scraping-crud

---
## 👤 Author

Nama: Muhammad Fikri Cakra Wardana

NIM: 241080200128

Mata Kuliah: Pengembangan Aplikasi Berbasis WEB

---
