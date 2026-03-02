class Instrumento():
    def __init__(self,nombre,material,tipo):
        self.nombre= nombre
        self.__material= material
        self.__tipo= tipo

    def __str__(self):
        return f"nombre: {self.nombre} , material: {self.__material} , tipo:{self.__tipo}"

class Main():
    x=Instrumento ("Piano", "abeto", "acustico")
    print(x)

    y=Instrumento ("bajo elecrico","mastil","cuerda")
    print(y)