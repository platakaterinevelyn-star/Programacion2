class Persona(): 
    def __init__(self,nombre,carnet,edad):
        self._nombre = nombre
        self._carnet = carnet
        self._edad = edad

    def __str__(self):
        return f"nombre: {self._nombre}, carnet: {self._carnet}, edad: {self._edad}"
    

class Estudiante(Persona):
    def __init__(self, nombre, carnet, edad, matricula, carrera):
        super().__init__(nombre, carnet, edad)
        self.__matricula = matricula
        self.__carrera = carrera

    def __str__(self):
        return super().__str__() + f", matricula: {self.__matricula}, carrera: {self.__carrera}"
    
    def getCarrera(self):
        return self.__carrera

    def mismaCarrera(self, otro):
        return self.__carrera == otro.getCarrera()


class Docente(Persona):
    def __init__(self, nombre, carnet, edad, antiguedad, sueldo):
        super().__init__(nombre, carnet, edad)
        self.__antiguedad = antiguedad
        self.__sueldo = sueldo

    def __str__(self):
        return super().__str__() + f", antiguedad: {self.__antiguedad}, sueldo: {self.__sueldo}"


class main():

    Estudiante1 = Estudiante("Kurmi Plata", 1234585, 23, 100195, "Psicologia")
    Estudiante2 = Estudiante("Alejandro Huallpa", 67890, 20, 100296, "Construccion Civil")
    docente = Docente("Ing.Lorena Gomez", 11223, 35, 10, 30500)

    print(Estudiante1)
    print(Estudiante2)
    print(docente)

    if Estudiante1._edad == docente._edad or Estudiante2._edad == docente._edad:
        print("Algún estudiante tiene la misma edad que el docente")
    else:
        print("Ningún estudiante tiene la misma edad que el docente")

    if Estudiante1.mismaCarrera(Estudiante2):
        print("Son de la misma carrera")
    else:
        print("saon de diferentes carreras")