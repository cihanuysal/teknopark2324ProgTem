#Ogrenci Class
    #Properties------------
    # ad,okulno,dersIslemleri
    # durumGoster()
#Not Class
    #Properties------------
    # notlar
    # Method
    # notlaryaz()
    # notEkle()
    # tumNotlariSil()
    # ortlama()
class Not:
    def __init__(self) -> None:
        self.notlar=list()
    def notEkle(self,puan):
        if puan>=0 and puan <=100:
            self.notlar.append(puan)
    def notlariYaz(self):
        for n in self.notlar:
            print(n)
    def tumNotlariSil(self):
        self.notlar.clear()
    def ortalama(self):
        ortalama=0
        for n in self.notlar:
            ortalama +=n
        ortalama=ortalama/len(self.notlar)
        return ortalama 
class Ogrenci:
    def __init__(self,ad,okulno):
        self.ad=ad
        self.okulno=okulno
        self.dersIslemleri=Not()
    def durumGoster(self):
        if self.dersIslemleri.ortalama()>=50:
            print(f"{self.okulno} - {self.ad} -{self.dersIslemleri.ortalama()} ile Dersten Geçmiştir.")
        else:
            print(f"{self.okulno} - {self.ad} -{self.dersIslemleri.ortalama()} ile Dersten KALDI.")
        


# ogrenci=Ogrenci("Muhammed",77)
# ogrenci.dersIslemleri.notEkle(65)
# ogrenci.dersIslemleri.notEkle(30)
# ogrenci.dersIslemleri.notEkle(25)
# ogrenci.dersIslemleri.notEkle(20)
# ogrenci.durumGoster()
# ogrenci.dersIslemleri.notlariYaz()
# ogrenci.dersIslemleri.tumNotlariSil()
# ogrenci.dersIslemleri.notEkle(95)
# ogrenci.dersIslemleri.notEkle(100)
# ogrenci.durumGoster()
# ogrenci.dersIslemleri.notlariYaz()
sinif:list[Ogrenci]=list()

sinif.append(Ogrenci("Oğuzhan",67))
sinif.append(Ogrenci("Serhent",86))
sinif.append(Ogrenci("Ahmet",70))
sinif.append(Ogrenci("Emre",83))

sinif[0].dersIslemleri.notEkle(100)
sinif[0].dersIslemleri.notEkle(75)
sinif[0].dersIslemleri.notEkle(86)


