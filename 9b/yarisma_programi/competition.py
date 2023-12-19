class Competition:
    def __init__(self,name,judge,date) -> None:
        self.__name=name
        self.__date=date
        self.__judge=judge
        self.__questions=list()
        self.__competitors=list()

