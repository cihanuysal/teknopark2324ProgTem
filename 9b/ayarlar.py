degisken="selam" #değişken
def selamla(): #fonksiyon
    return "merhaba"


class Insan: #class
    def __init__(self,ad) -> None:
        self.__ad=ad
    def setAd(self,ad):
        self.__ad=ad

    def getAd(self):
        return self.__ad
