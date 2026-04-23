class Animal:
    def __init__(self, nombre, edad, nombreDueño):
        self._nombre = nombre
        self._edad = edad
        self._nombreDueño = nombreDueño

    def getNombre(self):
        return self._nombre

    def getEdad(self):
        return self._edad
    
    def getNombreDueño(self): 
        return self._nombreDueño
    
class Perro(Animal):
    def __init__(self, nombre, edad, nombreDueño, requiereBosal, ladraFuerte):
        super().__init__(nombre, edad, nombreDueño)
        self.__requiereBosal = requiereBosal
        self.__ladraFuerte = ladraFuerte

    def __str__(self):
        return f"Perro: {self.getNombre()}, Edad: {self.getEdad()}, Dueño: {self.getNombreDueño()}"

class Gato(Animal):
    def __init__(self, nombre, edad, nombreDueño, cazaRatones, tomaLeche):
        super().__init__(nombre, edad, nombreDueño)
        self.__cazaRatones = cazaRatones
        self.__tomaLeche = tomaLeche

    def getTomaLeche(self): 
        return self.__tomaLeche

    def __str__(self):
        return f"Gato: {self.getNombre()}, Edad: {self.getEdad()}, Dueño: {self.getNombreDueño()}"
    
class CentroVeterinario:
    def __init__(self, nombre):
        self.__nombre = nombre
        self.__perros = []     
        self.__gatos = []       
        self.__cantPerros = 0
        self.__cantGatos = 0

    def agregarPerro(self, perro):
        if len(self.__perros) < 100:
            self.__perros.append(perro)
            self.__cantPerros = len(self.__perros)

    def agregarGato(self, gato):
        if len(self.__gatos) < 100:
            self.__gatos.append(gato)
            self.__cantGatos = len(self.__gatos)

    def ordenarPerros(self):
        self.__perros.sort(key=lambda p: (p.getEdad(), p.getNombreDueño(), p.getNombre()))

    def ordenarGatos(self):
        self.__gatos.sort(key=lambda g: (not g.getTomaLeche(), -g.getEdad(), g.getNombre()))

    def verificarDueños(self):
        print(f"--- Revisando dueños en {self.__nombre} ---")
        conteo = {}
        todos = self.__perros + self.__gatos
        
        for a in todos:
            dueño = a.getNombreDueño()
            conteo[dueño] = conteo.get(dueño, 0) + 1
        
        encontrado = False
        for dueño, cantidad in conteo.items():
            if cantidad >= 2:
                print(f"El dueño '{dueño}' tiene {cantidad} animales registrados.")
                encontrado = True
        if not encontrado:
            print("No se encontraron dueños con más de un animal.")

    def mostrarTodo(self):
        print(f"\nESTADO DE: {self.__nombre}")
        print(f"Cant. Perros: {self.__cantPerros}, Cant. Gatos: {self.__cantGatos}")
        for p in self.__perros: print(f"  {p}")
        for g in self.__gatos: print(f"  {g}")

cv1 = CentroVeterinario("Veterinaria kiki")
cv2 = CentroVeterinario("Clínica Animal choco")

cv1.agregarPerro(Perro("Boby", 5, "Juan", False, True))
cv1.agregarPerro(Perro("Rex", 3, "Ana", True, False))
cv1.agregarGato(Gato("Michi", 2, "Juan", True, True))
cv1.agregarGato(Gato("Pelusa", 4, "Maria", False, False))

cv2.agregarPerro(Perro("Zar", 4, "Beto", False, False))
cv2.agregarPerro(Perro("Aron", 4, "Beto", False, True))
cv2.agregarGato(Gato("Luna", 3, "Carla", True, True))
cv2.agregarGato(Gato("Guty", 6, "Carla", True, True))

print("--- DATOS ORDENADOS ---")
cv1.ordenarPerros()
cv1.ordenarGatos()
cv1.mostrarTodo()

cv2.ordenarPerros()
cv2.ordenarGatos()
cv2.mostrarTodo()

cv1.verificarDueños()
cv2.verificarDueños()