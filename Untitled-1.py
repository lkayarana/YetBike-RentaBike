import time
import datetime

class bikerental:

    def __init__(self, stock=0):
        self.stock=stock
    
    def displaystock(self):
        print("Su anda {} bisiklet mevcut".format(self.stock))
        return self.stock

    def hourlyrental(self, n):
        if n<=0:
            print("Bisiklet sayisi pozitif olmali.")
            return None
       
        elif n>self.stock:
            print("Maalesef. Mevcut bisiklet sayisi {}.".format(self.stock))
            return None
        
        else:
            now=datetime.datetime.now()
            print("{} tarihinde {} adet bisikleti saatlik olarak kiraladiniz.".format(now, n))
            print("Her bisiklet saatlik olarak 7.5 TL uzerinden ucretlendirilir.\nIyi eglenceler.")

            self.stock -= n
            return now

    def dailyrental(self, n):
        if n<=0:
            print("Bisiklet sayisi pozitif olmali.")
            return None
       
        elif n>self.stock:
            print("Maalesef. Mevcut bisiklet sayisi {}.".format(self.stock))
            return None
        
        else:
            now=datetime.datetime.now()
            print("{} tarihinde {} adet bisikleti gunluk olarak kiraladiniz.".format(now, n))
            print("Her bisiklet gunluk olarak 20 TL uzerinden ucretlendirilir.\nIyi eglenceler.")

            self.stock -=n
            return now
    
    def weeklyrental(self, n):
        if n<=0:
            print("Bisiklet sayisi pozitif olmali.")
            return None
       
        elif n>self.stock:
            print("Maalesef. Mevcut bisiklet sayisi {}.".format(self.stock))
            return None
        
        else:
            now=datetime.datetime.now()
            print("{} tarihinde {} adet bisikleti haftalik olarak kiraladiniz.".format(now, n))
            print("Her bisiklet haftalik olarak 75 TL uzerinden ucretlendirilir.\nIyi eglenceler.")

            self.stock -=n
            return now
    
    def returnbike(self, request):
        rentaltime, rentaltype, numberofbikes = request
        bill=0

        if rentaltime and rentaltype and numberofbikes:
            self.stock += numberofbikes
            now=datetime.datetime.now()
            rentalperiod= now - rentaltime

            if rentaltype==1:
                bill=round(rentalperiod.seconds/3600) * 7.5 * numberofbikes

            elif rentaltype==2:
                bill=round(rentalperiod.days) * 20 * numberofbikes
            
            elif rentaltype==3:
                bill=round(rentalperiod.days / 7) * 75 * numberofbikes

            print("Bisikletinizi iade ettiginiz icin teSekkur ederiz.\nodemeniz gereken tutar {} TL.".format(bill))
            return bill
        
        else:
            print("Bisikletinizi kiraladiginiza emin misiniz?")
            return None


class Customer:
    def __init__(self):
        self.bikes=0
        self.rentaltype=0
        self.rentaltime=0
        self.bill=0

    def request(self):
        bikes=int(input("Kac adet bisiklet kiralamak istiyorsunuz?"))

        try:
            bikes=int(bikes)
        except ValueError:
            print("Girdiginiz sayi pozitif olmali.")
            return -1

        if bikes<1:
            print("Gecersiz giriS. Bisiklet sayisi 0'dan buyuk olmali.")
            return -1

        else:
            self.bikes=bikes
        
        return self.bikes

    def returnbike(self):
        if self.rentaltype and self.rentaltime and self.bikes:
            return self.rentaltime, self.rentaltype, self.bikes
        
        else:
            return 0,0,0


def cikti_olustur(secim, bill):
    kayit_tarihi=time.ctime(time.time())
    t1=f"Yapilan secim {secim}\n"
    t2=f"odenen miktar {bill}\n"
    t3=f"OluSturulma tarihi {kayit_tarihi}\n"

    output=t1+t2+t3
    return output


def main():
    shop = bikerental(250)
    customer = Customer()
    
    while True:
        print("""
        **************YetBike Bisiklet Kiralama************
        1. Mevcut bisikletleri goster
        2. Saatlik 7.5 TL karSiliginda bisiklet talep edin
        3. Gunluk 25 TL karSiliginda bisiklet talep edin
        4. Haftalik 75 TL karSiliginda bisiklet talep edin
        5. Bisikleti iade edin
        6. cikiS
        """)
        
        secim=int(input("Lutfen tercihinizi giriniz: "))
        
        try:
            secim=int(secim)
        
        except ValueError:
            print("YanliS tercih yaptiniz.")
            continue
        
        if secim==1:
            shop.displaystock()
            
        elif secim==2:
            customer.rentaltime=shop.hourlyrental(customer.request())
            customer.rentaltype=1
        
        elif secim==3:
            customer.rentaltime=shop.dailyrental(customer.request())
            customer.rentaltype=2
            
        elif secim==4:
            customer.rentaltime=shop.weeklyrental(customer.request())
            customer.rentaltype=3
            
        elif secim==5:
            customer.bill=shop.returnbike(customer.returnbike())
            customer.rentaltype, customer.rentaltime, customer.bikes=0,0,0
        
        elif secim==6:
            break

        
        else:
            print("Gecersiz giriS yaptiniz.\nLutfen 1 ve 6 arasinda secim yapiniz.")
        

        output=cikti_olustur(secim, bill=0)

        with open ("YetBike.txt", "a") as f:
            f.write(str(time.ctime(time.time())))
            f.write("\n")
            f.write(output)
            f.write("\n")
            f.write("Kullanici bilgileri kaydedildi.")
            f.write("\n")
            f.write("*"*20)
            f.write("\n")
            
    
    print("Veriler 'YetBike.txt' dosyasina kaydedildi.")
    print("YetBike Bisiklet Kiralamayi tercih ettiginiz icin teSekkur ederiz!")

if __name__=="__main__":
    main()