import os
import pwinput
import time
# Data pengguna (username, password, role) dan loker (nomor, ukuran, status, pin)
users = {
    "admin": {"pass": "adminlocker2", "role": "admin"},
    "user": {"pass": "userlocker1", "role": "user"}
}

loker = {
    1: {"ukuran": "Kecil", "status": "Kosong", "pin": ""},
    2: {"ukuran": "Kecil", "status": "Kosong", "pin": ""},
    3: {"ukuran": "Sedang", "status": "Kosong", "pin": ""},
    4: {"ukuran": "Besar", "status": "Kosong", "pin": ""}
}

# Function untuk loker

def bersihkan_layar():
    os.system("cls" if os.name == "nt" else "")
    
def lihat_loker():
    print("\n" + "=" * 70)
    print("=                         STATUS LOKER           ")
    print("=" * 70)
    for no, data in loker.items():
        print(f"Loker #{no} [{data['ukuran']}] : {data['status']}")

def titip_barang():
    lihat_loker()
    try:
        no = int(input("\nPilih nomor loker yang kosong: "))
        if no in loker:
            if loker[no]["status"] == "Kosong":
                pin = input("Buat PIN loker: ")
                loker[no]["status"] = "Terisi"
                loker[no]["pin"] = pin
                print(f" Barang berhasil disimpan di Loker #{no}!")
            else:
                print(" Loker sudah terisi!")
        else:
            print(" Nomor loker tidak ditemukan!")
    except ValueError:
        print(" Input harus berupa angka!")

def ambil_barang():
    try:
        no = int(input("\nMasukkan nomor loker: "))
        if no in loker:
            if loker[no]["status"] == "Terisi":
                pin = input("Masukkan PIN: ")
                if pin == loker[no]["pin"]:
                    loker[no]["status"] = "Kosong"
                    loker[no]["pin"] = ""
                    print(" PIN benar! Silakan ambil barang.")
                else:
                    print(" PIN salah!")
            else:
                print(" Loker sedang kosong!")
        else:
            print(" Nomor loker tidak ditemukan!")
    except ValueError:
        print("Input harus berupa angka!")

def tambah_loker():
    try:
        no = int(input("\nMasukkan nomor loker baru: "))
        if no in loker:
            print(" Nomor loker sudah ada!")
        else:
            ukuran = input("Masukkan ukuran (Kecil/Sedang/Besar): ")
            loker[no] = {"ukuran": ukuran, "status": "Kosong", "pin": ""}
            print(f" Loker #{no} berhasil ditambahkan!")
    except ValueError:
        print(" Input harus berupa angka!")

def hapus_loker():
    try:
        no = int(input("\nMasukkan nomor loker yang akan dihapus: "))
        if no in loker:
            del loker[no]
            print(f" Loker #{no} berhasil dihapus!")
        else:
            print(" Nomor loker tidak ditemukan!")
    except ValueError:
        print(" Input harus berupa angka!")

# Menu program utama
while True:
    print("=" * 70)
    print("                        SMART LOCKER - LOGIN     ")
    print("=" * 70)
    username = input("Username : ")
    password = pwinput.pwinput ("Password : ")

    if username in users and users[username]["pass"] == password:
        role = users[username]["role"]
        
        while True:
            bersihkan_layar()
            print("\n" + "=" * 70)
            print(f"                        MENU LOCKER ({role.upper()})   ")
            print("=" * 70)

            if role == "admin":
                print("1. Lihat Loker")
                print("2. Tambah Loker (Create)")
                print("3. Hapus Loker (Delete)")
                print("4. Logout")
                pilih = input("Pilih menu (1-4): ")

                if pilih == "1":
                    lihat_loker()
                    time.sleep(1)
                elif pilih == "2":
                    tambah_loker()
                    time.sleep(1)
                elif pilih == "3":
                    hapus_loker()
                    time.sleep(1)
                elif pilih == "4":
                    time.sleep(1)
                    break
                else:
                    print("Pilihan tidak valid!")

            elif role == "user":
                print("1. Titip Barang")
                print("2. Ambil Barang")
                print("3. Lihat Loker")
                print("4. Logout")
                pilih = input("Pilih menu (1-4): ")

                if pilih == "1":
                    titip_barang()
                    time.sleep(1)
                elif pilih == "2":
                    ambil_barang()
                    time.sleep(1)
                elif pilih == "3":
                    lihat_loker()
                    time.sleep(1)
                elif pilih == "4":
                    time.sleep(1)
                    break
                else:
                    print("Pilihan tidak valid!")

    else:
        print("\nUsername atau Password salah!")
        time.sleep(1.5)