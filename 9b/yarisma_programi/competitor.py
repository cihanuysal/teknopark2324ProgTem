class Competitor:
    def __init__(self,mail,name,surname,birthDate,gender,hometown) -> None:
      self.__mail=mail
      self.__name=name
      self.__surname=surname
      self.__birthDate=birthDate
      self.__gender=gender
      self.__hometown=hometown
      self.__score=0
      
    def set_mail(self,mail):
       self.__mail=mail
    def get_mail(self):
       return self.__mail
    def addScore(self,puan):
       self.__score+=puan
    def reduceScore(self,puan):
       self.__score -=puan
    def resetScore(self):
       self.__score=0
    def getScore(self):
       return self.__score
    