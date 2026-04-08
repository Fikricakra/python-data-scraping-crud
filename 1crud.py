# crud_file.py
import json
import os

DATA_FILE = "data.json"

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
def tambah_item(nama, harga):
    data = load_data()
    new_id = max([item["id"] for item in data], default=0) + 1
    data.append({"id": new_id, "nama": nama, "harga": harga})
    save_data(data)
    print(f"Item '{nama}' berhasil ditambahkan.")

# READ
def lihat_semua():
    data = load_data()
    if not data:
        print("Tidak ada data.")
    for item in data:
        print(f"{item['id']}. {item['nama']} - Rp{item['harga']}")

# UPDATE
def update_item(item_id, nama_baru, harga_baru):
    data = load_data()
    for item in data:
        if item["id"] == item_id:
            item["nama"] = nama_baru
            item["harga"] = harga_baru
            save_data(data)
            print(f"ID {item_id} berhasil diupdate.")
            return
    print("ID tidak ditemukan.")

# DELETE
def hapus_item(item_id):
    data = load_data()
    new_data = [item for item in data if item["id"] != item_id]
    save_data(new_data)
    print(f"ID {item_id} berhasil dihapus.")

# Menu interaktif
def menu():
    while True:
        print("\n=== MENU CRUD ===")
        print("1. Tambah item")
        print("2. Lihat semua")
        print("3. Update item")
        print("4. Hapus item")
        print("5. Keluar")
        pilih = input("Pilihan: ")
        if pilih == "1":
            nama = input("Nama: ")
            harga = int(input("Harga: "))
            tambah_item(nama, harga)
        elif pilih == "2":
            lihat_semua()
        elif pilih == "3":
            id = int(input("ID item: "))
            nama = input("Nama baru: ")
            harga = int(input("Harga baru: "))
            update_item(id, nama, harga)
        elif pilih == "4":
            id = int(input("ID item: "))
            hapus_item(id)
        elif pilih == "5":
            break

if __name__ == "__main__":
    menu()