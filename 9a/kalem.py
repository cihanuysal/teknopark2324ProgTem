class kalem:
    def __init__(self,tip,boy) -> None:
        self.__tip=tip
        self.__boy=boy
    def kalemAc(self,tur=1):
        if self.tip=="kurşun":
            for i in range(1,tur+1):
                self.__boy -=1
        else:
            print(self.__tip ," kalem açılmaz")
    def nasilBirKalem(self):
      return f"Ben {self.__tip} türünde {self.__boy} mm uzunluğunda bir kalemim."



    

