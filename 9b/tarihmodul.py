# from datetime import date
# bugun=date.today()
# print("Gün :",bugun.day)
# print("Ay :",bugun.month)
# print("Yıl :",bugun.year)
# print("Gün Adı :",bugun.isoweekday())
# f
#insan
  #ad
  #doğum tarihi
  #kimsinSen()
     ## Benim Adım Ramazan  ben 1950 yılında Kasım ayının 13 ünde Pazartesi Günü 
## dünyaya geldim. 

from datetime import date
class insan:
    def __init__(self,ad,dtarih) -> None:
        self.__ad=ad
        self.__tarihOlustur(dtarih)
        self.__AYLAR=["ayisimleri","OCAK","ŞUBAT","MART","NİSAN","MAYIS","HAZİRAN","TEMMUZ","AĞUSTOS","EYLÜL","EKİM","KASIM","ARALIK"]
        self.__GUNLER=["gunIsimleri","PAZARTESİ","SALI","ÇARŞAMBA","PERŞEMBE","CUMA","CUMARTESİ","PAZAR"]
    
    def __str__(self) -> str:
        mesaj=f"Benim adım {self.__ad}.Ben {self.__dtarih.year} yılında {self.__AYLAR[self.__dtarih.month]} ayının {self.__dtarih.day} ünde {self.__GUNLER[self.__dtarih.isoweekday()]} günü dünyaya geldim"
        return mesaj
    def __tarihOlustur(self,tarih):
        veri=str(tarih).split(".")
        self.__dtarih=date(day=int(veri[0]),month=int(veri[1]),year=int(veri[2]))
    def selamla(self):
        print("MErhaba")


kisi=insan("Cihan","23.03.1985")



