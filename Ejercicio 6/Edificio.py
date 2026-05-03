class Mueble:
    def __init__(self, tipo, material):
        self.__tipo = tipo
        self.__material = material


class Habitacion:
    def __init__(self, nombre, tamanio):
        self.__nombre = nombre
        self.__tamanio = tamanio
        self.__muebles = []

    def agreMueble(self, mueble):
        self.__muebles.append(mueble)

    def cantMuebles(self):
        return len(self.__muebles)

    def getMuebles(self):
        return self.__muebles

    def getNombre(self):
        return self.__nombre


class Departamento:
    def __init__(self, nroPuerta, nroPiso):
        self.__nroPuerta = nroPuerta
        self.__nroPiso = nroPiso
        self.__habitaciones = []

    def agreHabitacion(self, hab):
        self.__habitaciones.append(hab)

    def cantHabitaciones(self):
        return len(self.__habitaciones)

    def totMuebles(self):
        total = 0
        for h in self.__habitaciones:
            total += h.cantMuebles()
        return total

    def getHabitaciones(self):
        return self.__habitaciones

    def getNroPuerta(self):
        return self.__nroPuerta

    def getNroPiso(self):
        return self.__nroPiso


class Parqueo:
    def __init__(self, capacidad):
        self.__capacidad = capacidad
        self.__autos = []

    def agreAuto(self, placa):
        if len(self.__autos) < self.__capacidad:
            self.__autos.append(placa)
        else:
            print("No hay espacio en el parqueo")


class Edificio:
    def __init__(self, nombre):
        self.__nombre = nombre
        self.__departamentos = []
        self.__parqueo = None

    def agreDepartamento(self, dep):
        self.__departamentos.append(dep)

    def agreParqueo(self, parqueo):
        self.__parqueo = parqueo

    def getDepartamentos(self):
        return self.__departamentos

    def getParqueo(self):
        return self.__parqueo
    
ed = Edificio("edificio michi")

p = Parqueo(2)
ed.agreParqueo(p)

d1 = Departamento(101, 1)
d2 = Departamento(102, 2)

h1 = Habitacion("Dormitorio", 20)
h2 = Habitacion("Cocina", 10)
h3 = Habitacion("Sala", 25)

m1 = Mueble("Cama", "Madera")
m2 = Mueble("Mesa", "Metal")
m3 = Mueble("Sofa", "Cuero")

h1.agreMueble(m1)
h2.agreMueble(m2)
h3.agreMueble(m3)

d1.agreHabitacion(h1)
d1.agreHabitacion(h2)
d2.agreHabitacion(h3)

ed.agreDepartamento(d1)
ed.agreDepartamento(d2)

Y = 1
mayor = None

for d in ed.getDepartamentos():
    if d.getNroPiso() == Y:
        if mayor is None or d.cantHabitaciones() > mayor.cantHabitaciones():
            mayor = d

if mayor:
    print("Depto con más habitaciones:", mayor.getNroPuerta())

X = 1
Z = 101

for d in ed.getDepartamentos():
    if d.getNroPiso() == X and d.getNroPuerta() == Z:
        nuevo = Mueble("TV", "Plastico")
        d.getHabitaciones()[0].agreMueble(nuevo)

maxdep = max(ed.getDepartamentos(), key=lambda d: d.totMuebles())
print("Dep con más muebles:", maxdep.getNroPuerta())

Z = 1
mayorhab = None

for d in ed.getDepartamentos():
    if d.getNroPiso() == Z:
        for h in d.getHabitaciones():
            if mayorhab is None or h.cantMuebles() > mayorhab.cantMuebles():
                mayorhab = h

if mayorhab:
    print("Habitación con más muebles:", mayorhab.getNombre())

def primo(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

ed.EdificioDeps = [
    d for d in ed.getDepartamentos()
    if not primo(d.cantHabitaciones())
]


ed.getParqueo().agreAuto("123-ABC")
ed.getParqueo().agreAuto("456-DEF")
ed.getParqueo().agreAuto("789-GHI")