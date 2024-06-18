import mysql.connector

koneksi = mysql.connector.connect(user='root', database='tiket_kereta')
conn = koneksi.cursor()

def get_kereta_api() :
    query = "SELECT * FROM kereta_api"
    conn.execute(query)
    for (id_kereta, nama_kereta, kelas, tujuan) in conn:
        print("{} - {} - {} - {}".format(id_kereta, nama_kereta, kelas, tujuan))
    conn.close()
    koneksi.close()

get_kereta_api()