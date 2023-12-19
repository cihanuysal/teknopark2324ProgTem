class Atm:
    def __init__(self,bankaAdi,para=0):
        self.bankaAdi=bankaAdi
        self.para=para
        self.KartYuvasi:Kart=None

    def paraEkle(self,miktar):
        self.para +=miktar

    def karTak(self,disardanGelenKart):
        self.KartYuvasi=disardanGelenKart

    def paraCek(self,miktar):
        if type(self.KartYuvasi)==Kart:
            self.para-=miktar
            self.KartYuvasi.bakiye -=miktar
            print(miktar," TL Para Çekilmiştir.")
        else:
            print("Para çekme işlemi başarısız oldu.")
            return False
     
    
class Kart:
    def __init__(self,ad,bankaAdi,sifre) -> None:
        self.ad=ad
        self.bankaAdi=bankaAdi
        self.bakiye=0
        self.sifre=sifre

    def hesabaParaYatir(self,miktar):
        self.bakiye +=miktar

    def sifreDegistir(self,yeniSifre):
        self.sifre=yeniSifre
    
    def bakiyeSorgula(self):
        return self.bakiye

    
kurtIsBank=Atm("is",10000)
uskudarHalk=Atm("halk")
uskudarHalk.paraEkle(50000)











# teknoHalk=Atm("halk",5000)
# print("ATM deki PARA:",teknoHalk.para)

# betulKart=Kart("Betül","halk","1234")
# betulKart.hesabaParaYatir(500)
# print(f"{betulKart.ad} isim kişinin parası :",betulKart.bakiyeSorgula())

# teknoHalk.karTak(betulKart)
# teknoHalk.paraCek(200)
# print("ATM deki PARA:",teknoHalk.para)
# print(f"{betulKart.ad} isim kişinin parası :",betulKart.bakiyeSorgula())




