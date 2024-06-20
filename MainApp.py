import mysql.connector
import os
import time
import random
from datetime import datetime 

class MainApp:
    def __init__(self):
        self.koneksi = mysql.connector.connect(user='root', database='tiket_kereta')
        self.conn = self.koneksi.cursor()
        self.login_id_penumpang = 0
        self.login_nama_penumpang = ''

    def lihat_daftar_tiket(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Daftar Kereta Api beserta tujuannya.")
        query = "SELECT nama_kereta, kelas, id_tiket, tujuan, berangkat, waktu_berangkat FROM kereta_api INNER JOIN tiket ON kereta_api.id_kereta = tiket.id_kereta"
        self.conn.execute(query)
        print(f"| {'-'*4} | {'-'*20} | {'-'*20} | {'-'*20} | {'-'*20} | {'-'*10} |")
        print(f"| {'ID':<4} | {'Nama Kereta':<20} | {'Berangkat':<20} | {'Tujuan':<20} | {'Waktu Keberangkatan':<20} | {'Kelas' :<10} |")
        print(f"| {'-'*4} | {'-'*20} | {'-'*20} | {'-'*20} | {'-'*20} | {'-'*10} |")

        for (nama_kereta, kelas, id_tiket, tujuan, berangkat, waktu_berangkat) in self.conn:
            print(f"| {id_tiket :<4} | {nama_kereta :<20} | {berangkat :<20} | {tujuan :<20} | {waktu_berangkat :%m/%d/%Y, %H:%M:%S} | {kelas :<10} |")

        print(f"| {'-'*4} | {'-'*20} | {'-'*20} | {'-'*20} | {'-'*20} | {'-'*10} |")

    def beli_tiket(self):
        print("Masukkan ID tiket yang ingin di beli")
        pilih_tiket = input("=> ")
        no_kursi = random.randint(1,40)
        tgl_pembelian = datetime.now()
        query = "INSERT INTO pembelian VALUES(null, %s, %s, %s, %s)"
        data_pembelian = (self.login_id_penumpang, pilih_tiket, no_kursi, tgl_pembelian)
        self.conn.execute(query, data_pembelian)
        self.koneksi.commit()
        print("Selamat, pembelian tiket Anda berhasil!")
        time.sleep(3)
    
    def riwayat_pembelian(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Berikut adalah riwayat pembelian tiket Anda:")
        query = "SELECT id_pembelian, id_tiket, tgl_pembelian FROM pembelian WHERE id_penumpang= " + str(self.login_id_penumpang)
        self.conn.execute(query)
        print(f"| {'-'*3} | {'-'*8} | {'-'*20} |")
        print(f"| {'ID' :<3} | {'ID Tiket' :<8} | {'Tgl Pembelian' :<20} |")
        print(f"| {'-'*3} | {'-'*8} | {'-'*20} |")

        for (id_pembelian, id_tiket, tgl_pembelian) in self.conn:
            print(f"| {id_pembelian :<3} | {id_tiket :<8} | {tgl_pembelian :%m/%d/%Y, %H:%M:%S} |")
        
        print(f"| {'-'*3} | {'-'*8} | {'-'*20} |")

    def detail_pembelian(self):
        print("Tekan 'enter' untuk kembali atau masukkan ID untuk melihat detail tiket")
        pilih_id_pembelian = input("=> ")
        if pilih_id_pembelian != '':
            query = "SELECT no_nik, nama, tiket.id_tiket, berangkat, waktu_berangkat, nama_kereta, kelas, tujuan, id_pembelian, no_kursi, tgl_pembelian FROM penumpang INNER JOIN pembelian ON penumpang.id_penumpang = pembelian.id_penumpang INNER JOIN tiket ON pembelian.id_tiket = tiket.id_tiket INNER JOIN kereta_api ON tiket.id_kereta = kereta_api.id_kereta WHERE id_pembelian=" + pilih_id_pembelian
            self.conn.execute(query)
            for (no_nik, nama, id_tiket, berangkat, waktu_berangkat, nama_kereta, kelas, tujuan, id_pembelian, no_kursi, tgl_pembelian) in self.conn:
                print(f"| {'-'*43} |")
                print(f"| {'Nomor tiket' :<20} | {str(id_tiket) + '/' + str(id_pembelian) :<20} |")
                print(f"| {'Nomor identitas' :<20} | {no_nik :<20} |")
                print(f"| {'Nama Penumpang' :<20} | {nama :<20} |")
                print(f"| {'Waktu keberangkatan' :<20} | {waktu_berangkat :%m/%d/%Y, %H:%M:%S} |")
                print(f"| {'-'*43} |")
                print(f"| {'Kelas ' + kelas + ' dengan nomor kursi ' + str(no_kursi) :<43} |")
                print(f"| {'Dari stasiun ' + berangkat + ' ke stasiun ' + tujuan :<43} |")
                print(f"| {'Kereta Api ' + nama_kereta :<43} |")
                print(f"| {'-'*43} |")
            print("Tekan 'enter' untuk kembali ke menu sebelumnya")
            input("=> ")

    def ubah_rute_perjalanan(self):
        print("Tekan 'enter' untuk kembali atau masukkan ID untuk mengubah stasiun tujuan")
        pilih_id_pembelian = input("=> ")
        if pilih_id_pembelian != '':
            self.lihat_daftar_tiket()
            print("Masukkan ID tiket")
            pilih_id_tiket = input("=> ")
            query = "UPDATE pembelian SET id_tiket='" + pilih_id_tiket + "' WHERE id_pembelian=" + pilih_id_pembelian
            self.conn.execute(query)
            self.koneksi.commit()
            print("tujuan stasiun berhasil diubah")
            time.sleep(3)
    
    def batalkan_pembelian(self):
        print("Tekan 'enter' untuk kembali atau masukkan ID untuk membatalkan pembelian")
        pilih_id_pembelian = input("=> ")
        if pilih_id_pembelian != '':
            query = "DELETE FROM pembelian WHERE id_pembelian=" + pilih_id_pembelian
            self.conn.execute(query)
            self.koneksi.commit()
            print("tiket berhasil dibatalkan")
            time.sleep(3)

    def sign_in_menu(self):
        ulangi = True
        while ulangi:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("selamat datang, ", self.login_nama_penumpang, "!")
            print("1. Lihat Daftar Tiket")
            print("2. Beli Tiket")
            print("3. Riwayat Pembelian Tiket")
            print("4. Ubah rute perjalanan")
            print("5. batalkan pembelian tiket")
            print("6. Keluar")
            while True:
                print("Masukkan pilihan Anda (1/2/3/4/5/6) lalu tekan 'enter'")
                pilihan = input("=> ")
                if pilihan == "1":
                    self.lihat_daftar_tiket()
                    print("Tekan 'enter' untuk kembali ke menu sebelumnya")
                    input("")
                    break
                elif pilihan == "2":
                    self.lihat_daftar_tiket()
                    self.beli_tiket()
                    break
                elif pilihan == "3":
                    self.riwayat_pembelian()
                    self.detail_pembelian()
                    break
                elif pilihan == "4":
                    self.riwayat_pembelian()
                    self.ubah_rute_perjalanan()
                    break
                elif pilihan == "5":
                    self.riwayat_pembelian()
                    self.batalkan_pembelian()
                    break
                elif pilihan == "6":
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


app = MainApp()
app.home_menu()