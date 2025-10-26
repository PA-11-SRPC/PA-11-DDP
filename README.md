# PA-11-DDP

# Kelompok 11 ( Projek Akhir Dasar-Dasar Pemrograman )

foto 1
![WhatsApp Image 2025-10-26 at 20 33 47_d07165da](https://github.com/user-attachments/assets/162a6fd4-7277-4e0e-bb29-2cffefff98e4)
jadi dari kode yang keliatan di foto itu, intinya dia bikin sistem buat PetCare yang nyimpen data di CSV, terus ada beberapa file buat data hewan, user, reservasi, sama invoice. Ada settingan saldo maksimal buat top-up dan nominal top-up yang bisa dipilih, terus ada daftar user default yang isinya admin sama user biasa. Fungsi human_currency dipake buat ubah angka jadi format rupiah biar gampang dibaca, misal 100000 jadi Rp100.000, dan kalau error ya balik ke angka biasa. Terus ada fungsi safe_input yang basically mirip input biasa tapi aman, jadi kalau user tiba-tiba stop program pake Ctrl+C atau ada EOF, program ga crash, cuma ngeprint pesan “program dihentikan sama pengguna.” Intinya, ini bagian awal kode setup semua data, constant, sama beberapa fungsi bantu buat handle input sama format uang.
foto 2
![WhatsApp Image 2025-10-26 at 20 33 47_0ea2babb](https://github.com/user-attachments/assets/5af206d7-e68d-48b0-be4f-06f9913cef56)
foto kedua ini nunjukin potongan kode Python di VS Code yang isinya beberapa fungsi buat ngatur input dan baca/tulis data CSV. Ada fungsi safe_input() yang langsung nutup program kalau dipanggil, print_header() buat nampilin judul biar rapi di konsol, read_csv_dict() buat baca file CSV jadi list of dictionary (setiap baris jadi dict), dan atomic_write_csv() yang nulis data ke file CSV secara aman — dia nulis dulu ke file sementara lalu ganti file aslinya biar data nggak korup kalau ada error. Intinya, bagian kode ini fokus ke manajemen file CSV dan tampilan teks di terminal
foto 3
![WhatsApp Image 2025-10-26 at 20 33 48_0fd9b941](https://github.com/user-attachments/assets/44d45835-99dc-457f-a6be-35282075540c)
foto ini nunjukin bagian kode Python yang ngatur data pengguna dalam bentuk CSV. Ada fungsi ensure_default_users() buat ngecek apakah file CSV user sudah ada atau belum, kalau belum, dia bakal bikin file itu dan isi dengan data user default dari variabel DEFAULT_USERS. Terus ada load_users() yang baca isi CSV tersebut dan ubah jadi dictionary Python, lengkap dengan username, password, role, dan saldo tiap user. Fungsi ini juga nge-handle kalau ada error pas konversi saldo jadi angka. Intinya, bagian ini dipakai buat inisialisasi dan load data akun pengguna ke dalam program
foto 4
![WhatsApp Image 2025-10-26 at 20 33 48_b5037eb9](https://github.com/user-attachments/assets/1af2961d-cc38-4085-97a5-4feaa46e2f98)
di foto ini  nampilin lanjutan kode Python yang ngatur penyimpanan data pengguna, hewan, dan reservasi. Fungsi save_users() dipakai buat nyimpen data user ke file CSV dengan format yang udah rapi (username, password, role, saldo). Lalu ada bagian #DATA HEWAN yang isinya dua fungsi: load_pets() buat baca data hewan dari file CSV (kalau file belum ada, langsung dibuat kosong), dan save_pets() buat nyimpen data hewan ke CSV juga. Terakhir, bagian #RESERVASI & INVOICE punya fungsi append_reservation() yang nambah data pesanan baru ke file CSV, termasuk username, layanan, dan harga, sambil bikin file baru kalau belum ada sebelumnya. Jadi, bagian ini fokusnya ke pengelolaan dan penyimpanan data dalam bentuk CSV supaya semua informasi bisa disimpan dengan aman
foto 5
![WhatsApp Image 2025-10-26 at 20 33 48_7cdddb37](https://github.com/user-attachments/assets/2f976731-7e1c-466d-a4a5-2b04bfa40ecc)
foto ini nunjukin tampilan kode Python di VS Code yang lagi buka file bernama **PA_1.Py**. Di bagian yang kelihatan, ada beberapa fungsi yang ngatur proses penyimpanan data ke file CSV dan format tampilan tabel. Misalnya, fungsi `append_invoice()` buat nambah data invoice (seperti tanggal, username, layanan, dan harga) ke file CSV, terus ada `format_pet_table()` dan `format_reservasi_table()` buat nampilin data hewan peliharaan atau reservasi dalam bentuk tabel rapi pakai library `PrettyTable`. Jadi intinya, kode ini kayak bagian backend dari aplikasi kecil buat layanan pet care atau reservasi hewan.
foto 6
![WhatsApp Image 2025-10-26 at 20 33 49_79b66350](https://github.com/user-attachments/assets/25d48211-796d-4412-8497-344d928401f0)
foto ini nunjukin bagian kode Python di VS Code yang lagi fokus ke fitur login dan menu admin dari sistem pet care. Di fungsi login(users), program minta username dan password dari user, terus ngecek apakah datanya cocok sama yang ada di daftar pengguna (users). Kalau cocok, user bisa masuk dan dapet peran sesuai rolenya. Di bawahnya ada menu_admin(data_hewan) yang isinya daftar pilihan menu buat admin, seperti nambah, liat, ubah, dan hapus data hewan atau reservasi. Jadi bagian kode ini ngatur proses masuknya pengguna dan tampilan menu utama buat admin
foto 7
![WhatsApp Image 2025-10-26 at 20 33 49_696a27f5](https://github.com/user-attachments/assets/8576ea3a-8531-45d1-957a-864bc2d66439)
ini juga masih nunjukin kelanjutan dari fungsi menu_admin(data_hewan) di program Python tadi. Di bagian ini, kodenya ngatur beberapa opsi menu buat admin: nambah data hewan (dengan input jenis dan umur), liat daftar hewan dalam format tabel, dan ubah data hewan yang udah ada. Kalau admin milih ubah data, program bakal nampilin daftar hewan, minta nomor hewan yang mau diedit, lalu ganti jenis atau umurnya sesuai input baru. Setelah itu data disimpan lagi lewat fungsi save_pets(). Intinya, potongan kode ini ngatur logika CRUD (Create, Read, Update) buat data hewan di sistem pet care
foto 8
![WhatsApp Image 2025-10-26 at 20 33 49_696a27f5](https://github.com/user-attachments/assets/d5d28dc9-e40a-4b48-8957-bc4037cdbf60)
fotonya masih lanjutan dari fungsi menu_admin(data_hewan) di program Python tadi. Di bagian ini, admin bisa menghapus data hewan (pilihan menu 4) dengan cara milih nomor hewan yang mau dihapus dari daftar, lalu data disimpan ulang pakai save_pets(). Selain itu, ada juga menu buat melihat data reservasi (menu 5) dan menghapus data reservasi (menu 6). Program bakal cek dulu apakah file CSV reservasi ada atau nggak, lalu menampilkan atau menghapus data sesuai pilihan admin. Jadi potongan kode ini lebih fokus ke fitur delete dan manajemen data reservasi di sistem
foto 9
![WhatsApp Image 2025-10-26 at 20 33 51_29325bc6](https://github.com/user-attachments/assets/04c7643d-9d08-4a46-bcff-644e3c0aa2aa)
foto ini nampilin bagian akhir dari fungsi menu_admin(data_hewan) dan awal dari fungsi menu_pengguna(username, users). Di bagian admin, ada fitur buat hapus data reservasi (menu 6) dengan cara milih nomor reservasi yang mau dihapus dari file CSV, lalu datanya ditulis ulang pakai atomic_write_csv(). Kalau admin pilih menu 7, sistem bakal keluar dari menu dengan pesan “Logout berhasil.” Setelah itu lanjut ke fungsi menu_pengguna, yang isinya daftar menu untuk user biasa seperti lihat saldo, isi saldo, reservasi layanan, lihat riwayat transaksi, dan logout. Jadi bagian ini memisahkan fungsi admin dan pengguna biar masing-masing punya akses sesuai perannya
foto 10
![WhatsApp Image 2025-10-26 at 20 33 51_d6eee73d](https://github.com/user-attachments/assets/3f8c4ca8-5d9e-4bb2-9154-bfda9055e241)
codingan ini nunjukin bagian tengah dari fungsi menu_pengguna(username, users). Di sini, user bisa melihat saldo dan mengisi saldo (top up). Kalau pilih menu 1, program bakal nampilin saldo pengguna dalam format uang lewat fungsi human_currency(). Kalau pilih menu 2, program nampilin daftar nominal top up yang bisa dipilih (pakai PrettyTable), lalu user milih jumlah saldo yang mau ditambahin. Kode juga ngecek biar saldo nggak melebihi batas maksimum (MAX_SALDO). Kalau input valid, saldo ditambah, disimpan lewat save_users(), dan hasilnya ditampilkan lagi. Intinya, bagian ini ngatur transaksi saldo pengguna secara interaktif
foto 11
![WhatsApp Image 2025-10-26 at 19 33 38 (10)](https://github.com/user-attachments/assets/6f8629b8-5f8d-4d14-8a71-d0cc5a0cafe1)
ini nunjukin lanjutan dari fungsi menu_pengguna(username, users) yang ngatur bagian reservasi layanan dan lihat riwayat transaksi. Di bagian atas, user bisa milih layanan seperti grooming, vaksin, atau penitipan yang ditampilin dalam bentuk tabel (PrettyTable). Kalau saldo cukup, sistem bakal ngurangin saldo user, nyimpen data ke file reservasi lewat append_reservation(), dan juga nambah invoice lewat append_invoice(). Kalau saldo kurang, muncul pesan gagal. Di bawahnya, ada fitur buat melihat riwayat transaksi yang ngambil data dari file CSV_INVOICE dan nampilin transaksi yang sesuai sama username pengguna. Jadi, bagian ini ngebuat sistem jadi interaktif dan terhubung antara data saldo, reservasi, dan invoice
foto 12
![WhatsApp Image 2025-10-26 at 19 33 38 (11)](https://github.com/user-attachments/assets/2ea56372-62ca-4277-9530-09a62da80fae)
di foto terakhir ini nunjukin bagian akhir dari program Python sistem pet care. Di sini ada penutupan fungsi menu_pengguna(), yang nampilin riwayat transaksi user dalam bentuk tabel berisi tanggal, layanan, dan harga pakai PrettyTable. Kalau user pilih menu 5, maka sistem bakal keluar dengan pesan “Logout berhasil.” Di bawahnya ada fungsi utama main(), yang jadi titik awal program. Fungsi ini bakal memuat data pengguna dan hewan, lalu manggil fungsi login() buat masukin user. Kalau role-nya “admin”, sistem buka menu admin, kalau bukan berarti user biasa masuk ke menu pengguna. Baris paling bawah if __name__ == "__main__": main() nunjukin bahwa program ini langsung jalan saat file dijalankan










