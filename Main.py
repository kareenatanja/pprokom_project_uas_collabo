from passengerinfo import*
from TicketShow import*
from admin import*

global ch # declare global variable

print("-----------------------------------------------------")
print("              Welcome to BusKita                     ")
print("-----------------------------------------------------")
print()

def start(): #called function
    print("1. Buat Akun Baru")
    print("2. Login       ")
    print()
    adminObj = Admin()
    ch = int(input("Pilih sesuai dengan nomornya: "))

    if ch == 1:
        #admin class object creation
        adminObj.adminRegistration()
        start()
        
    if ch == 2:
        
        adminObj.adminLogin()

        print()
        print("1. Pesan tiket")
        print("2. Lihat tiket")
        print()
        ch = int(input("Pilih opsi: "))
        if ch == 1:
            pd_obj = PassengerDataCsv()
            pd_obj.getPassengerInfo()
            pd_obj.saveInfo()

            print("Apakah kamu ingin memesan tiket lagi [yes/no]? ") 
            y = input("").lower()
            if y == "yes":
                pd_obj.getPassengerInfo()
            elif y == "no":
                start()
            else:
                print("Pilih yes/no!")  
        elif ch ==2:
            obj = TicketShow()
            obj.ticketShow()

start()#calling function
#=======================================================================
