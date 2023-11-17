#Data Importing section
from passengerinfo import*

class TicketShow:

    def ticketShow(self):
        bln = [] # list for storing data and retrieving from passengerData.csv file
        with open("passengerData.csv",'r+',newline="") as f:
            r =  csv.reader(f)
            data = list(r)
            while True:
                try:
                    id = int(input("Masukkan Booking ID  :"))
                    break
                except:
                    print("Booking ID hanya berupa angka!")
                    continue
                
            for i in data:
                if id == int(i[0]):
                    for j in i:
                        bln.append(j)
                    break
        #print(bln)  
        print("------------------------------------------------------------------------------")
        print("                                  BUSKITA                                     ")
        print("------------------------------------------------------------------------------")
        print()
        print(" e_Ticket :", "Alamat Kantor               : Jl. Jalan No. 100                ")
        print("           ", "Nomor Telepon               : 081292102121929                  ")
        print()
        print("",bln[3],"------------->",bln[4],"             ","        Passenger Id:",bln[0])
        print()
        print(" Nama Penumpang :", bln[1],"                   ","        Jumlah Penumpang :",bln[2])
        print("______________________________________________________________________________")
        print()
        print(" Tanggal Pemesanan :",bln[5],"            ","             Kursi Nomor :",bln[6],"          ")
        print()
        print(" Tipe Bus :       ",bln[7],"                                                           ")
        print(" Harga    :       ",bln[8],"                                                           ")
        print()
        print("------------------------------------------------------------------------------")
                




