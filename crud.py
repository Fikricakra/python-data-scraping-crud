# crud_file.py
import json
import os

DATA_FILE = "countries.json"

# Inisialisasi file jika belum ada
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, "w") as f:
        json.dump([], f)
def load_data():
    with open(DATA_FILE, "r") as f:
        return json.load(f)
def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

# CREATE
def tambah_item(nama, Capital, Population, Area):
    data = load_data()
    for item in data:
        if item["negara"].lower() == nama.lower():
            print("Negara sudah ada!")
            return
    data.append({
        "negara": nama,
        "ibu_kota": Capital,
        "populasi": Population,
        "luas": Area,
    })
    save_data(data)
    print(f"Negara '{nama}' berhasil ditambahkan.")

# READ
def lihat_semua():
    data = load_data()
    if not data:
        print("Tidak ada data.")
        return
    for i, item in enumerate(data, start=1):
        print(f"{i}. {item['negara']}")
        print(f"Ibu Kota : {item['ibu_kota']}")
        print(f"Populasi : {item['populasi']}")
        print(f"   Luas     : {item['luas']}")
        print("-" * 40)

# UPDATE
def update_item(nama_negara, ibu_kota, populasi, luas):
    data = load_data()
    for item in data:
        if item["negara"].lower() == nama_negara.lower():
            item["ibu_kota"] = ibu_kota
            item["populasi"] = populasi
            item["luas"] = luas
            save_data(data)
            print("Data berhasil diupdate.")
            return
    print("Negara tidak ditemukan.")

# DELETE
def hapus_item(nama_negara):
    data = load_data()
    data_baru = [item for item in data if item["negara"].lower() != nama_negara.lower()]
    save_data(data_baru)
    print(f"Negara '{nama_negara}' berhasil dihapus.")

# Menu interaktif
def menu():
    while True:
        print("\n=== MENU CRUD NEGARA ===")
        print("1. Tambah negara")
        print("2. Lihat semua")
        print("3. Update negara")
        print("4. Hapus negara")
        print("5. Keluar")
        pilih = input("Pilihan: ")
        if pilih == "1":
            negara = input("Nama negara: ")
            ibu_kota = input("Ibu kota: ")
            populasi = input("Populasi: ")
            luas = input("Luas: ")
            tambah_item(negara, ibu_kota, populasi, luas)
        elif pilih == "2":
            lihat_semua()
        elif pilih == "3":
            negara = input("Nama negara yang ingin diupdate: ")
            ibu_kota = input("Ibu kota baru: ")
            populasi = input("Populasi baru: ")
            luas = input("Luas baru: ")
            update_item(negara, ibu_kota, populasi, luas)
        elif pilih == "4":
            negara = input("Nama negara yang ingin dihapus: ")
            hapus_item(negara)
        elif pilih == "5":
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    menu()