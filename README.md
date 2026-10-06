# MinPro-2-DDP-SistemSmartLocker
Nama : Bintang Dzikri Al Bukhari 
NIM : 2609116030 
Program Studi : Sistem Informasi

## Tentang Program Ini
Smart Locker System Mini Project 2 adalah pengembangan dari Mini Project 1 berupa sistem manajemen loker berbasis terminal Python. Program ini dilengkapi sistem Autentikasi (Login) multi-role (admin dan user), pengelolaan loker menggunakan struktur data Dictionary & Function, validasi input, error handling (try-except), serta manipulasi data secara CRUD lengkap untuk role Admin.

## Flowchart
<img width="2273" height="1929" alt="Diagram Tanpa Judul drawio (5)" src="https://github.com/user-attachments/assets/4cef03a0-5037-4a12-98f5-67697bb9c799" />

ini adalah hasil dari alur flowchart dari program Smart Locker.

## Materi di Program Ini
### 1. Tuple = UKURAN = ("kecil", "sedang", "besar")
   dipergunakan untuk menyimpan kategori ukuran dari loker yang nilainya tetap dan tidak dapat berubah.
### 2. Nested List = loker
   digunakan untuk menyimpan data dari banyaknya loker di program dengan menyimpan secara struktur dan sesuai format.
   [nomor loker, ukuran, status, PIN]
### 3. While Loop = While True
   digunakan untuk proses pemilihan di menu utama (Titip barang, Ambil barang, Cek status, Keluar)
### 4. If/else 
   digunakan dalam menangani di halaman Menu Utama, Ukuran Loker, Validasi Nomor Loker, Verifikasi PIN saat pengambilan barang
### 5. For Loop
   digunakan pada :
   1. Mencari loker yang kosong sesuai permintaan pengguna
   2. Menyimpan PIN
   3. Menghapus dan mengosongkan data PIN setelah pengambilan barang
### 6. Dictionary & Nested Dictionary (users, loker)
   Digunakan untuk menyimpan data pengguna (username, password, role) serta menyimpan data loker beserta propertinya secara terstruktur (ukuran, status, dan pin).
   
## Alur OUTPUT (user)

### Halaman awal saat login
<img width="666" height="132" alt="Screenshot 2026-10-06 113201" src="https://github.com/user-attachments/assets/ad901a1d-2cc7-4db9-b76e-cca34622704d" />

Berikut ini adalah hasil output halaman awal dimana terdapat proses login yang meminta pengguna untuk menginput username dan password

### Menu saat login sebagai user
<img width="650" height="140" alt="Screenshot 2026-10-06 165558" src="https://github.com/user-attachments/assets/ac7118ad-f5af-4137-9b79-438d4809a591" />

Berikut ini tampilan menu awal (user) yang terdapat pilihan menitip barang, mengambil barang,  melihat status, logout.

### Full tampilan menu 1 (menitipkan barang)
<img width="650" height="300" alt="Screenshot 2026-10-06 121723" src="https://github.com/user-attachments/assets/73a047c1-39f3-47f0-8376-d7b698611705" />

Berikut ini adalah tampilan penuh yang dilihat oleh user ketika ingin menitipkan barang dengan memilih ukuran loker dan memasukan pin

### Full tampilan menu 2 (mengambil barang)
<img width="662" height="295" alt="Screenshot 2026-10-06 171845" src="https://github.com/user-attachments/assets/fb9bf354-4d5a-4b1b-9dc9-6535fcc34237" />

Berikut ini adalah tampilan penuh yang dilihat oleh user ketika ingin mengambil barang dengan menginput nomor loker dan ukuran loker

### Full tampilan menu 3 (menampilkan status semua loker)
<img width="641" height="207" alt="Screenshot 2026-10-06 173008" src="https://github.com/user-attachments/assets/4fd8809e-3317-4cbd-9676-a3fdbfa16c11" />

Berikut ini adalah tampilan layar penuh yang dilihat oleh user ketika mereka menginput menu pilihan 3 (menampilkan seluruh status loker apakah sudah terisi/kosong)

### Full tampilan menu 4 (keluar dari akun user)
<img width="648" height="147" alt="Screenshot 2026-10-06 165544" src="https://github.com/user-attachments/assets/210634d4-ce85-47af-9a5e-1b8637d50a71" />

Menu ini membawa user kembali ke halaman login

## Alur OUTPUT (admin)

### Halaman awal saat login
<img width="650" height="131" alt="Screenshot 2026-10-06 180155" src="https://github.com/user-attachments/assets/70b29f46-3d0b-44aa-b3d6-bbc8c0813b4a" />

Berikut ini adalah hasil output halaman awal dimana terdapat proses login yang meminta pengguna untuk menginput username dan password

### Menu saat login sebagai admin
<img width="642" height="192" alt="image" src="https://github.com/user-attachments/assets/35543305-ac23-44d9-bfae-31fc285d4b15" />

Berikut ini tampilan menu awal (user) yang terdapat pilihan menitip barang, mengambil barang,  melihat status, logout.

### Full tampilan menu 1 (menampilkan status semua loker)
<img width="650" height="300" alt="Screenshot 2026-10-06 121723" src="https://github.com/user-attachments/assets/73a047c1-39f3-47f0-8376-d7b698611705" />

Berikut ini adalah tampilan layar penuh yang dilihat oleh admin ketika mereka menginput menu pilihan 3 (menampilkan seluruh status loker apakah sudah terisi/kosong)

### Full tampilan menu 2 (menambahkan loker)
<img width="642" height="298" alt="Screenshot 2026-10-06 173045" src="https://github.com/user-attachments/assets/676283be-716c-4072-a1fb-37d902b3c5d2" />

Berikut ini adalah tampilan penuh yang dilihat oleh admin yang dapat menambahkan loker baru dengan menentukan ukuran loker (besar, sedang, kecil)

### Full tampilan menu 3 (menghapus loker)
<img width="646" height="265" alt="Screenshot 2026-10-06 173105" src="https://github.com/user-attachments/assets/02444429-18c7-4a8a-a332-caca9d58cb0e" />

Berikut ini adalah tampilan penuh yang dilihat oleh admin yang dapat menghapus loker 

### Full tampilan menu 4 (keluar dari akun user)
<img width="650" height="131" alt="Screenshot 2026-10-06 180155" src="https://github.com/user-attachments/assets/84cbcce5-afb7-49f2-a503-a470e4e8838c" />

Berikut ini adalah hasil output halaman awal dimana terdapat proses login yang meminta pengguna untuk menginput username dan password

## Penerapan nilai tambah

### Library (OS, PWINPUT, TIME)

#### import os
<img width="475" height="60" alt="image" src="https://github.com/user-attachments/assets/befc8c97-b951-4bd2-baf6-65cb33986f93" />

os: Mengakses perintah sistem operasi untuk membersihkan layar terminal (cls untuk Windows, clear untuk Linux/Mac) saat looping login.

#### import pwinput
<img width="635" height="140" alt="image" src="https://github.com/user-attachments/assets/8ad6a008-e730-4ddf-95a3-91beb127960a" />

pwinput: Library eksternal untuk menyembunyikan input password dengan karakter asteris (*) agar keamanan data sensitif terjaga.

#### import time

<img width="347" height="270" alt="image" src="https://github.com/user-attachments/assets/6b6685bb-06ee-4eee-a4bf-d6d171a04ce6" />

time: Mengatur jeda waktu penundaan (time.sleep()) sebelum layar dibersihkan atau beralih menu.

### Analisis Validasi Input & Error Handling

<img width="486" height="50" alt="image" src="https://github.com/user-attachments/assets/53bc4aea-0ecf-42d4-ba1a-1a29561320e0" />

jika pengguna secara tidak sengaja memasukkan huruf atau karakter khusus saat diminta nomor loker, Python tidak akan menghentikan program dengan error
