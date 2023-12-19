class urun:
    def __init__(self,urn,fiyat) -> None:
        self.__urn=urn
        self.__fiyat=fiyat

    def setUrun(self,urn):
        self.__urn=urn

    def getUrun(self):
        return self.__urn
    
    def setFiyat(self,val):
        self.__fiyat=val

    def getFiyat(self):
        return self.__fiyat