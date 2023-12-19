#1. Class Not
        #properties 
            #notlar type is list()
        #methods
             # - notVer()
             # - notYazdir()
             # - ortalama()
             # - tumnotlariSil()

#2. Class Ogrenci
            # propeties 
                # okulNo,ad,dersislemeri
            # methods
                # durumGoster()
class Not:
    def __init__(self) -> None:
        self.notlar=list()
    
    def notver(self,puan):
        self.notlar.append(puan)
    def notYazdir(self):
        print("VERİLEN TÜM NOTLAR")
        for n in self.notlar:
            print(n)
    def ortalama(self):
        ort=0
        for n in self.notlar:
            ort+=n
        if len(self.notlar)==0:
            return 0
        else :
            ort=ort/len(self.notlar)
            return ort
    def tumNotlariSil(self):
        self.notlar.clear()

class Ogrenci:
    def __init__(self,okulNo,ad) :
        self.okulNo=okulNo
        self.ad=ad
        self.dersIslemleri=Not()
    
    def durumGoster(self):
        if self.dersIslemleri.ortalama()>=50:
            print(f"{self.okulNo}  - {self.ad}  {self.dersIslemleri.ortalama()} ile GEÇTİ")
        else:
            print(f"{self.okulNo}  - {self.ad}  {self.dersIslemleri.ortalama()} ile KALDI")
                

# ogr1=Ogrenci(89,"Zeynep Afra")
# ogr1.dersIslemleri.notver(55)
# ogr1.dersIslemleri.notver(61)
# ogr1.dersIslemleri.notver(40)
# ogr1.dersIslemleri.notver(45)
# ogr1.dersIslemleri.notYazdir()
# ogr1.dersIslemleri.tumNotlariSil()
# ogr1.dersIslemleri.notver(100)
# ogr1.dersIslemleri.notver(95)
# ogr1.dersIslemleri.notYazdir()

# ogr1.durumGoster()

sinif:list[Ogrenci]=list()

sinif.append(Ogrenci(68,"Ayşe"))
sinif.append(Ogrenci(84,"Hümeyra"))
sinif.append(Ogrenci(65,"Halil"))
sinif.append(Ogrenci(78,"İlhan"))
sinif.append(Ogrenci(82,"Kaan"))

for o in sinif:
    sayac=1
    print(f"{o.ad} isimli Öğrencinin Notları:")
    while sayac<=4:
        o.dersIslemleri.notver(int(input(f"{sayac}. Not :")))
        sayac+=1


print("ÖĞRENCİ NO     AD    ORTALAMA     DURUM")
for o in sinif:
    print(o.durumGoster())




