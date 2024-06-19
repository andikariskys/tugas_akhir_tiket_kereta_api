import mysql.connector
import os
import time

class Config:
    def __init__(self):
        self.koneksi = mysql.connector.connect(user='root', database='tiket_kereta')
        self.conn = self.koneksi.cursor()
        self.login_id_penumpang = 0
        self.login_nama_penumpang = ''

    def sign_in_menu(self):
        ulangi = True
        while ulangi:
            print("selamat datang, ", self.login_nama_penumpang, "!")
            print("1. Lihat Daftar Kereta")
            print("2. Lihat Daftar Tiket")
            print("3. Beli Tiket")
            print("4. Riwayat Pembelian Tiket")
            print("5. Keluar")
            while True:
                print("Masukkan pilihan Anda (1/2/3/4) lalu tekan 'enter'")
                pilihan = input("=> ")
                if pilihan == "1":
                    # lihat daftar kereta
                    break
                elif pilihan == "2":
                    # lihat daftar tiket
                    break
                elif pilihan == "3":
                    # lihat daftar tiket
                    # beli tiket
                    break
                elif pilihan == "4":
                    # lihat riwayat pembelian tiket
                    break
                elif pilihan == "5":
                    print("Sign Out berhasil")
                    time.sleep(3)
                    ulangi = False
                    break
                else:
                    print("Pilihan yang Anda masukkan salah")

    def sign_in(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        while True:
            print("Masukkan NIK yang telah terdaftar lalu tekan 'enter'")
            user_nik = input("=> ")
            if len(user_nik) == 16:
                break
            else:
                print("Nomor NIK tidak sesuai")
        print("Masukkan password Anda")
        user_pass = input("=> ")
        query = "SELECT count(*) as count, id_penumpang, nama FROM penumpang WHERE no_nik = '" + user_nik + "' AND password='" + user_pass + "'"
        self.conn.execute(query)
        for (count, id_penumpang, nama) in self.conn:
            if count != 0:
                self.login_id_penumpang = id_penumpang
                self.login_nama_penumpang = nama
                self.sign_in_menu()
                break
            else:
                print("Nik tidak terdaftar/password yang Anda masukkan salah")
                time.sleep(3)
                self.sign_in()

    def sign_up(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Pendaftaran 'KAI TiketKu Solo' silakan isi data dengan benar")
        print("Masukkan Nomor NIK Anda")
        no_nik = input("=> ")
        print("Masukkan nama lengkap Anda")
        nama_penumpang = input("=> ")
        print("Masukkan alamat lengkap Anda")
        alamat = input("=> ")
        print("Masukkan password untuk login")
        password = input("=> ")
        query = "INSERT INTO penumpang VALUES(null, %s, %s, %s, %s)"
        data_penumpang = (no_nik, password, nama_penumpang, alamat)
        self.conn.execute(query, data_penumpang)
        self.koneksi.commit()
        print("Pendaftaran berhasil, silakan kembali login")
        time.sleep(3)

    def home_menu(self):
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Selamat datang di 'KAI TiketKu Solo' (Aplikasi pemesanan tiket kereta terbaik Solo)")
            print("Silakan pilih menu dibawah:")
            print("1. Sign In")
            print("2. Sign Up")
            print("3. Keluar")
            print("Silakann masukkan pilihan Anda (1/2/3) lalu tekan enter")
            pilihan = input("=> ")
            if pilihan == "1":
                self.sign_in()
            elif pilihan == "2":
                self.sign_up()
            elif pilihan == "3":
                print("Terima kasih telah menggunakan aplikasi kami.")
                break
            else:
                print("Pilihan yang Anda masukkan salah/tidak ada.")

    def get_kereta_api(self):
        query = "SELECT * FROM kereta_api"
        self.conn.execute(query)
        for (id_kereta, nama_kereta, kelas, tujuan) in self.conn:
            print("{} - {} - {} - {}".format(id_kereta, nama_kereta, kelas, tujuan))

    def get_tiket(self):
        query = "SELECT * FROM tiket"
        self.conn.execute(query)
        for (id_tiket, id_kereta, berangkat, waktu_berangkat, jumlah_kursi) in self.conn:
            print("{} - {} - {} - {}".format(id_tiket, id_kereta, berangkat, waktu_berangkat, jumlah_kursi ))

    def get_pembelian(self):
        query = "SELECT * FROM pembelian"
        self.conn.execute(query)
        for (id_pembelian, id_penumpang, id_tiket, no_kursi, tgl_pembelian) in self.conn:
            print("{} - {} - {} - {}".format(id_pembelian, id_penumpang, id_tiket, no_kursi, tgl_pembelian))

config = Config()
config.home_menu()