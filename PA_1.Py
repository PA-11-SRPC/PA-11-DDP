import pwinput
import csv
import datetime
import os
from prettytable import PrettyTable

CSV_FILE = "petcare.csv"
CSV_USER = "users.csv"
CSV_RESERVASI = "reservasi.csv"
CSV_INVOICE = "invoice.csv"

#Minimal & Maksimal Top-Up
MAX_SALDO = 300_000
TOPUP_NOMINALS = [50_000, 100_000, 150_000, 200_000, 250_000, 300_000]

DEFAULT_USERS = [
    {"username": "admin", "password": "123", "role": "admin", "saldo": 0},
    {"username": "pom", "password": "321", "role": "pengguna", "saldo": 0},
]


def human_currency(amount):
    try:
        return f"Rp{int(amount):,}".replace("," ".")
    except Exception:
        return f"Rp{amount}"

def safe_input(prompt):
    try:
        return input(prompt)
    except (KeyboardInterrupt, EOFError):
        print("\nProgram dihentikan sama pengguna.")
        raise SystemExit(0)

def print_header(title):
    print("\n" + "=" * 60)
    print(f"{title.center(52)}")
    print("=" * 60)

def read_csv_dict(path):
    if not os.path.exists(path):
        return []
    try:
        with open(path, mode="r", newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            return [row for row in reader]
    except Exception:
        return []

def atomic_write_csv(path, fieldnames, rows):
    tmp = f"{path}.tmp"
    try:
        with open(tmp, mode="w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for r in rows:
                writer.writerow({k: r.get(k, "") for k in fieldnames})
        os.replace(tmp, path)
        return True
    except Exception:
        if os.path.exists(tmp):
            os.remove(tmp)
        return False

#User
def ensure_default_users():
    if not os.path.exists(CSV_USER):
        rows = []
        for u in DEFAULT_USERS:
            rows.append({
                "username": u["username"],
                "password": u["password"],
                "role": u["role"],
                "saldo": u["saldo"]
            })
        atomic_write_csv(CSV_USER, ["username", "password", "role", "saldo"], rows)

def load_users():
    ensure_default_users()
    rows = read_csv_dict(CSV_USER)
    users = {}
    for r in rows:
        uname = (r.get("username") or "").strip()
        pwd = r.get("password") or ""
        role = r.get("role") or "pengguna"
        try:
            saldo = float(r.get("saldo", 0))
        except ValueError:
            saldo = 0.0
        if uname:
            users[uname] = {"password": pwd, "role": role, "saldo": saldo}
    return users

def save_users(users):
    rows = []
    for uname, info in users.items():
        rows.append({
            "username": uname,
            "password": info.get("password", ""),
            "role": info.get("role", "pengguna"),
            "saldo": info.get("saldo", 0)
        })
    atomic_write_csv(CSV_USER, ["username", "password", "role", "saldo"], rows)

#Data Hewan
def load_pets():
    if not os.path.exists(CSV_FILE):
        atomic_write_csv(CSV_FILE, ["Jenis Hewan", "Umur"], [])
        return []
    rows = read_csv_dict(CSV_FILE)
    pets = [[r.get("Jenis Hewan", ""), r.get("Umur", "")] for r in rows]
    return pets

def save_pets(pets):
    rows = [{"Jenis Hewan": p[0], "Umur": p[1]} for p in pets]
    atomic_write_csv(CSV_FILE, ["Jenis Hewan", "Umur"], rows)

#Reservasi & Invoice
def append_reservation(username, layanan, harga):
    ada = os.path.exists(CSV_RESERVASI)
    try:
        with open(CSV_RESERVASI, mode="a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            if not ada:
                writer.writerow(["Username", "Layanan", "Harga"])
            writer.writerow([username, layanan, int(harga)])
        return True
    except Exception:
        return False

def append_invoice(username, layanan, harga):
    ada = os.path.exists(CSV_INVOICE)
    waktu = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    try:
        with open(CSV_INVOICE, mode="a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            if not ada:
                writer.writerow(["Tanggal", "Username", "Layanan", "Harga"])
            writer.writerow([waktu, username, layanan, int(harga)])
        return True
    except Exception:
        return False

#Tabel 
def format_pet_table(pets):
    t = PrettyTable(["No", "Jenis Hewan", "Umur"])
    for i, p in enumerate(pets, start=1):
        t.add_row([i, p[0], p[1]])
    return t

def format_reservasi_table(rows):
    t = PrettyTable(["No", "Username", "Layanan", "Harga"])
    for i, r in enumerate(rows, start=1):
        try:
            harga = float(r.get("Harga", 0))
        except Exception:
            harga = 0.0
        t.add_row([i, r.get("Username", ""), r.get("Layanan", ""), human_currency(harga)])
    return t

#Login
def login(users):
    while True:
        print_header("LOGIN SISTEM PETCARE")
        username = safe_input("Masukkan username: ").strip()
        password = pwinput.pwinput("Masukkan password: ")

        user = users.get(username)
        if user and user["password"] == password:
            print(f"\nLogin berhasil! Selamat datang, {username}.")
            return username, user["role"]
        else:
            print("\nUsername atau password salah, coba lagi.")

#Menu Admin
def menu_admin(data_hewan):
    while True:
        print_header("MENU ADMIN")
        print("1. Tambah Data Hewan")
        print("2. Lihat Data Hewan")
        print("3. Ubah Data Hewan")
        print("4. Hapus Data Hewan")
        print("5. Lihat Data Reservasi")
        print("6. Hapus Data Reservasi")
        print("7. Logout")

        pilih = safe_input("Pilih menu: ").strip()

        if pilih == "1":
            jenis = safe_input("Jenis Hewan: ").strip()
            umur = safe_input("Umur: ").strip()
            if jenis:
                data_hewan.append([jenis, umur])
                save_pets(data_hewan)
                print("Data berhasil ditambahkan!")

        elif pilih == "2":
            if not data_hewan:
                print("Data hewan kosong.")
            else:
                print(format_pet_table(data_hewan))

        elif pilih == "3":
            if not data_hewan:
                print("Data kosong.")
                continue
            for i, h in enumerate(data_hewan, start=1):
                print(f"{i}. {h[0]} - {h[1]}")
            try:
                idx = int(safe_input("Nomor yang diubah: "))
                if 1 <= idx <= len(data_hewan):
                    new_jenis = safe_input("Jenis baru: ").strip()
                    new_umur = safe_input("Umur baru: ").strip()
                    if new_jenis:
                        data_hewan[idx - 1][0] = new_jenis
                    if new_umur:
                        data_hewan[idx - 1][1] = new_umur
                    save_pets(data_hewan)
                    print("Data diperbarui.")
            except ValueError:
                print("Input harus angka.")

        elif pilih == "4":
            if not data_hewan:
                print("Data kosong.")
                continue
            for i, h in enumerate(data_hewan, start=1):
                print(f"{i}. {h[0]} - {h[1]}")
            try:
                hapus = int(safe_input("Nomor yang dihapus: "))
                if 1 <= hapus <= len(data_hewan):
                    data_hewan.pop(hapus - 1)
                    save_pets(data_hewan)
                    print("Data dihapus.")
            except ValueError:
                print("Input harus angka.")

        elif pilih == "5":
            if not os.path.exists(CSV_RESERVASI):
                print("Belum ada data reservasi.")
                continue
            rows = read_csv_dict(CSV_RESERVASI)
            if not rows:
                print("Belum ada data reservasi.")
            else:
                print(format_reservasi_table(rows))

        elif pilih == "6":
            if not os.path.exists(CSV_RESERVASI):
                print("Belum ada data reservasi.")
                continue
            rows = read_csv_dict(CSV_RESERVASI)
            for i, r in enumerate(rows, start=1):
                print(f"{i}. {r.get('Username','')} - {r.get('Layanan','')} ({r.get('Harga','')})")
            try:
                hapus = int(safe_input("Nomor yang akan dihapus: "))
                if 1 <= hapus <= len(rows):
                    del rows[hapus - 1]
                    atomic_write_csv(CSV_RESERVASI, ["Username", "Layanan", "Harga"], rows)
                    print("Data reservasi dihapus.")
            except ValueError:
                print("Input harus angka.")

        elif pilih == "7":
            print("Logout berhasil.")
            break

        else:
            print("Pilihan tidak valid.")

#Menu Pengguna 
def menu_pengguna(username, users):
    while True:
        print_header(f"MENU PENGGUNA ({username})")
        print("1. Lihat Saldo")
        print("2. Isi Saldo (Top Up)")
        print("3. Reservasi Layanan")
        print("4. Lihat Riwayat Transaksi")
        print("5. Logout")

        pilih = safe_input("Pilih menu: ").strip()

        if pilih == "1":
            saldo = users.get(username, {}).get("saldo", 0)
            print(f"\nSaldo Anda saat ini: {human_currency(saldo)}")

        elif pilih == "2":
            print("\n=== PILIH NOMINAL ISI SALDO ===")
            t = PrettyTable(["No", "Nominal (Rupiah)"])
            for i, n in enumerate(TOPUP_NOMINALS, start=1):
                t.add_row([i, human_currency(n)])
            print(t)

            try:
                idx = int(safe_input("Nomor pilihan: "))
                if 1 <= idx <= len(TOPUP_NOMINALS):
                    jumlah = TOPUP_NOMINALS[idx - 1]
                    current = users[username]["saldo"]
                    if current + jumlah > MAX_SALDO:
                        print("\nSaldo melebihi batas maksimum.")
                    else:
                        users[username]["saldo"] = current + jumlah
                        save_users(users)
                        print(f"\nSaldo berhasil ditambahkan sebesar {human_currency(jumlah)}.")
                        print(f"Saldo sekarang: {human_currency(users[username]['saldo'])}")
                else:
                    print("Pilihan tidak tersedia.")
            except ValueError:
                print("Input tidak valid. Harus angka.")

        elif pilih == "3":
            layanan = {
                "1": ("Grooming", 50_000),
                "2": ("Vaksin", 75_000),
                "3": ("Penitipan", 100_000)
            }
            print("\nPILIH LAYANAN")
            t = PrettyTable(["Kode", "Nama Layanan", "Harga"])
            for k, (nama, harga) in layanan.items():
                t.add_row([k, nama, human_currency(harga)])
            print(t)

            pilih_layanan = safe_input("Pilih kode layanan: ").strip()
            if pilih_layanan in layanan:
                nama, harga = layanan[pilih_layanan]
                current = users[username]["saldo"]
                if current >= harga:
                    users[username]["saldo"] = current - harga
                    save_users(users)
                    append_reservation(username, nama, harga)
                    append_invoice(username, nama, harga)
                    print(f"\n Reservasi '{nama}' berhasil!")
                    print(f"Sisa saldo: {human_currency(users[username]['saldo'])}")
                else:
                    print("\nSaldo tidak cukup untuk reservasi ini.")
            else:
                print("Pilihan tidak valid.")

        elif pilih == "4":
            if not os.path.exists(CSV_INVOICE):
                print("Belum ada transaksi.")
            else:
                rows = read_csv_dict(CSV_INVOICE)
                user_transaksi = [r for r in rows if r.get("Username") == username]
                if not user_transaksi:
                    print("Belum ada transaksi Anda.")
                else:
                    t = PrettyTable(["Tanggal", "Layanan", "Harga"])
                    for r in user_transaksi:
                        t.add_row([r.get("Tanggal"), r.get("Layanan"), human_currency(r.get("Harga"))])
                    print("\nRIWAYAT TRANSAKSI")
                    print(t)

        elif pilih == "5":
            print("Logout berhasil.")
            break
        else:
            print("Pilihan tidak valid.")

#Main Program
def main():
    users = load_users()
    pets = load_pets()
    username, role = login(users)
    if role == "admin":
        menu_admin(pets)
    else:
        menu_pengguna(username, users)

if __name__ == "__main__":
    main()
