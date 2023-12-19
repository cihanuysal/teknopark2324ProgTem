import ogrenci
class derslik:
    def __init__(self,kapasite,sube) -> None:
        self.__kapasite=kapasite
        self.__sube=sube   
        self.__ogrenciler=list() 

    def setKapasite(self,val):
        self.__kapasite=val
    
    def getKapasite(self):
        return self.__kapasite
    
    def setSube(self,val):
        self.__sube=val
    
    def getSube(self):
        return self.__sube
    
    def setOgrenci(self,val:ogrenci):
        self.__ogrenciler.append(val)
    
    def getOgrenci(self):
        return self.__ogrenciler
