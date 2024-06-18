import mysql.connector
import os

class Config:
    def __init__(self):
        self.koneksi = mysql.connector.connect(user='root', database='tiket_kereta')
        self.conn = self.koneksi.cursor()
        self.login_id_penumpang = 0
        self.login_nama_penumpang = ''

    def sign_up(self):
        print("masukkan nama lengkap")
        
    def home(self):
        print("selamat datang")

    def sign_in(self):
        print("Selamat datang di 'KAI TiketKu' silakan masuk terlebih dahulu")
        while True:
            print("Masukkan NIK yang telah terdaftar/jika belum mendaftar ketik 'daftar' lalu tekan enter")
            nik_penumpang = input("=> ")
            if nik_penumpang == 'daftar':
                self.sign_up()
                break
            print("Masukkan password untuk masuk")
            pass_penumpang = input("=> ")
            query = "SELECT count(*) as count, id_penumpang, nama FROM penumpang WHERE no_nik = '" + nik_penumpang + "' AND password='" + pass_penumpang + "'"
            self.conn.execute(query)
            for (count, id_penumpang, nama) in self.conn:
                if count != 0:
                    self.login_id_penumpang = id_penumpang
                    self.login_nama_penumpang = nama
                    self.home()
                    break
                else:
                    print("Nik tidak terdaftar/password yang Anda masukkan salah")
            break

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

    def get_penumpang(self):
        query = "SELECT * FROM penumpang"
        self.conn.execute(query)
        for (id_penumpang, no_nik, password, nama, alamat) in self.conn:
            print("{} - {} - {} - {}".format(id_penumpang, no_nik, password, nama, alamat))

    def get_pembelian(self):
        query = "SELECT * FROM pembelian"
        self.conn.execute(query)
        for (id_pembelian, id_penumpang, id_tiket, no_kursi, tgl_pembelian) in self.conn:
            print("{} - {} - {} - {}".format(id_pembelian, id_penumpang, id_tiket, no_kursi, tgl_pembelian))

config = Config()
config.sign_in()