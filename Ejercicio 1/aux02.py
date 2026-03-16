class Televisor():
    def __init__(self,marca,resolucion,tipo):
        self.__marca= marca
        self.__resolucion= resolucion
        self.__tipo= tipo

    def __str__(self):
        return f"marca: {self.__marca}, resolución: {self.__resolucion}, tipo: {self.__tipo}"
    
class Main():
    tele01= Televisor("Sony", "3840","oled" )
    print(tele01)

    tele02= Televisor("Samsung", "2160","neo qled" )
    print(tele01)

    