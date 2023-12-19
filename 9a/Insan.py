# class Insan:
#     def __init__(self,kilo=2): #constructure
#         self.ad=""
#         self.kilo=kilo
#         print("INGAAAAAAAAAAAAAAAAAAAAAA")
#     def adiniKoy(self,ad):
#         self.ad=ad
#     def adiniSoyle(self):
#         print(f"Benim Adım {self.ad}")

# adem=Insan(4)
# adem.adiniKoy("Necati")
# havva=Insan()
# havva.adiniKoy("Raziye")
# adem.adiniSoyle()
# havva.adiniSoyle()

#Insan - property     ad,kilo
       #-methods
            # adKoy()  
            # kimsinSen()
            # yemekYe()
            # sporYap()
            # tartil()


class Insan:
    def __init__(self,kilo=3):
        self.kilo=kilo
        self.ad=None
    def adKoy(self,ad):
        self.ad=ad
    def kimsinSen(self):
        print(f"Benim adım {self.ad}")
    
    def yemekYe(self):
        self.kilo+=1
    def sporYap(self):
        self.kilo=-1
    def tartil(self):
        return self.kilo    


i=Insan(4)

i.adKoy("Raziye")
i.kimsinSen()
i.yemekYe()
i.yemekYe()
print("Kaç kiloyum :",i.tartil())


print("Kaç kiloyum :",i.tartil())
i.yemekYe()
i.yemekYe()
i.yemekYe()

i.yemekYe()

i.yemekYe()
print("Kaç kiloyum :",i.tartil())