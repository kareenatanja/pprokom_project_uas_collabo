import csv
import random

class pembayaran:
    def pembayaran_tiket():
        metode_pembayaran = input("Pembayaran tiket bus menggunakan [cash/e-wallet]: ").lower()

        def generate_kode_booking():
            # Fungsi untuk menghasilkan kode booking acak
            characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
            code_length = 8
            kode_booking = ''.join(random.choice(characters) for _ in range(code_length))
            return kode_booking
        if metode_pembayaran == "cash":
            # Jika menggunakan metode pembayaran cash
            kode_booking = generate_kode_booking()
            print(f"Terima kasih! Kode booking Anda adalah: {kode_booking}")

        elif metode_pembayaran == "e-wallet":
            # Jika menggunakan metode pembayaran e-wallet
            kode_verifikasi = input("Masukkan kode verifikasi e-wallet: ")

            if len(kode_verifikasi) == 6 and kode_verifikasi.isdigit():
                nomor_kursi = random.randint(1, 30)
                nomor_bus = random.randint(1, 10)
                waktu_keberangkatan = "12:00 PM"  # Ganti dengan waktu keberangkatan sesuai kebutuhan
                print(f"Pembayaran berhasil! Nomor kursi: {nomor_kursi}, Nomor bus: {nomor_bus}, Waktu keberangkatan: {waktu_keberangkatan}")
            else:
                print("Kode verifikasi tidak valid. Pembayaran gagal.")

        else:
            print("Metode pembayaran tidak valid. Silakan pilih 'cash' atau 'e-wallet'.")

        kembali = input("Ingin kembali ke menu? (ya/tidak): ").lower()
        if kembali == "ya":
            metode_pembayaran()
        else:
            print("Terima kasih!")
            
    # Panggil fungsi pembayaran_tiket untuk menjalankan program
    pembayaran_tiket()

class Admin:
    def __init__(self):
        self.username = None
        self.password = None

    def adminRegistration(self):
        print("----------------------------------------------------------------")
        print()
        with open("adminCredential.csv",'a',newline="") as f:
            w =  csv.writer(f)
            self.username = input("Masukkan username    :")
            self.password = input("Masukkan password    :")
            #saving a data into database
            w.writerow([self.username,self.password])
            f.close()
            print("Registration successfully")
        print()
        print("----------------------------------------------------------------")
            
    def adminLogin(self):
        username = []
        password = []
        
        with open("adminCredential.csv",'r+',newline="") as f:
            r =  csv.reader(f)
            data = list(r)
            #print(data)
            
            for i in data:
                username.append(i[0])
                password.append(i[1])

        #print(actList)
        while(True):
            print("----------------------------------------------------------------")
            print()
            self.username = input("Masukkan  username  :")
            self.password = input("Masukkan  password  :")
            for i in range(len(username)):
                if self.username == username[i] and self.password == password[i]:
                        print()
                        print("Login Succesfully!")
                        break
            else:
                print("Masukkan username dan password yang tepat!")
                continue
            
            print()
            print("---------------------------------------------------------------")
            break

