class Libro:
    def __init__(self, nombre, autor, año):
        self.__nombre = nombre
        self.__autor = autor
        self.__año = año

    @property
    def nombre(self):
        return self.__nombre

    def __str__(self):
        return f"Libro: {self.__nombre}, Autor: {self.__autor}, Año: {self.__año}"

class Biblioteca:
    def __init__(self, nombre):
        self.__nombre = nombre
        self.__libros = []  
        self.__cantLibros = 0

    @property
    def nombre(self):
        return self.__nombre

    @property
    def cantLibros(self):
        return len(self.__libros)

    def agregarLibro(self, libro):
        if len(self.__libros) < 100:
            self.__libros.append(libro)
            self.__cantLibros = len(self.__libros)
        else:
            print("Biblioteca llena.")

    def buscarLibro(self, nombre_buscar):
        for libro in self.__libros:
            if libro.nombre.lower() == nombre_buscar.lower():
                print(f"Encontrado en {self.__nombre}: {libro}")
                return True
        return False

    def __str__(self):
        return f"Biblioteca: {self.__nombre} (Libros: {self.cantLibros})"
    

b1 = Biblioteca("Central")
b2 = Biblioteca("Nacional")

l1 = Libro("Cien años de soledad", " García Márquez", 1967)
l2 = Libro("1984", "George Orwell", 1949)
l3 = Libro("El Quijote", "Cervantes", 1605)
l4 = Libro("Rayuela", "Cortázar", 1963)

b1.agregarLibro(l1)
b1.agregarLibro(l2)

b2.agregarLibro(l3)
b2.agregarLibro(l4)

nombrebuscar = "1984"
print(f"--- Buscando '{nombrebuscar}' ---")
if not b1.buscarLibro(nombrebuscar):
    print("No se encontró el libro.")

print("--- Comparando tamaño de bibliotecas ---")
bibliotecas = [b1, b2]
maxLibros = max(bib.cantLibros for bib in bibliotecas)

for bib in bibliotecas:
    if bib.cantLibros == maxLibros:
        print(f"Biblioteca con más libros: {bib}")