#encapsulation
class Araba:
    def __init__(self,marka,model,yil,km,renk) -> None:
        self.setMarka(marka)
        self.model=model
        self.yil=yil
        self.km=km
        self.renk=renk
        self.__fiyat=0

    def setMarka(self,marka):
        self.__marka=marka
    def getMarka(self):
        return self.__marka



