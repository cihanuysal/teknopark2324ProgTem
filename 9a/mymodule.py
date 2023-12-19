from datetime import date
class insan:
    def __init__(self,ad,dtarih) -> None:
        self.__ad=ad
        self.__tarih_olustur(dtarih)
        self.__AYLAR=[
                "aylar",
                "OCAK",
                "ŞUBAT",
                "MART",
                "NİSAN",
                "MAYIS",
                "HAZİRAN",
                "TEMMUZ",
                "AĞUSTOS",
                "EYLÜL",
                "EKİM",
                "KASIM",
                "ARALIK"
                      ]
        self.__GUNLER=["gunler","PAZARTESİ","SALI","ÇARŞAMBA","PERŞEMBE","CUMA","CUMARTESİ","PAZAR"]

    def __tarih_olustur(self,tarih):
        veri=str(tarih).split(".")
        self.__dtarih=date(day=int(veri[0]),month=int(veri[1]),year=int(veri[2]))

    def setAd(self,ad):
        self.__ad=ad
    
    def getAd(self):
        return self.__ad
    
    def getAge(self):
        return date.today().year - self.__dtarih.year
    
    def kimsinSen(self):
        mesaj=f"Benim adım {self.__ad}. {self.__dtarih.day} {self.__AYLAR[self.__dtarih.month]} {self.__dtarih.year} YILINDA {self.__GUNLER[self.__dtarih.isoweekday()]} GÜNÜ DOĞDUM."
        return mesaj

