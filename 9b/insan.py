#Örn Insan properties ---> ad , kilo
#          methods    ---> yemekye(), 
#                          sporyap(),
#                          !!!adiniKoy(), 
#                          !!!adiniSoyle(),
#                          kacKilosun()


class Insan:
    def __init__(self,kilo=3):
        self.kilo=kilo
        self.ad=""

    def adiniKoy(self,ad="Mustafa"):
        self.ad=ad

    def adiniSoyle(self):
        print(f"Benim Adım {self.ad}")
    def kacKilosun(self):
        return self.kilo
    def yemekYe(self):
        self.kilo +=1
    def sporYap(self):
        self.kilo -=1



ali=Insan()
ali.adiniKoy("Recai")
print(ali.ad)

ali.yemekYe()
ali.yemekYe()

ali.yemekYe()

print(f"kilosu {ali.kacKilosun()}")



