from abc import ABC, abstractmethod
import math

class Figura(ABC):
    def __init__(self, color):
        self._color = color

    @abstractmethod
    def obtenerArea(self):
        pass

    def getColor(self):
        return self._color

class Cuadrado(Figura):
    def __init__(self, color, lado):
        super().__init__(color)
        self._lado = lado

    def obtenerArea(self):
        return self._lado * self._lado

    def __str__(self):
        return f"Cuadrado, Color: {self._color}, Área: {self.obtenerArea()}"


class Triangulo(Figura):
    def __init__(self, color, lado1, lado2, lado3):
        super().__init__(color)
        self._lado1 = lado1
        self._lado2 = lado2
        self._lado3 = lado3

    def obtenerArea(self):
        s = (self._lado1 + self._lado2 + self._lado3) / 2
        return math.sqrt(s * (s - self._lado1) * (s - self._lado2) * (s - self._lado3))

    def __str__(self):
        return f"Triángulo, Color: {self._color}, Área: {self.obtenerArea():.2f}"


class Redondo(Figura):
    def __init__(self, color, radio):
        super().__init__(color)
        self._radio = radio

    def obtenerArea(self):
        return math.pi * (self._radio ** 2)

    def __str__(self):
        return f"Redondo, Color: {self._color}, Área: {self.obtenerArea():.2f}"

class main():

    c1 = Cuadrado("Rojo", 4)
    c2 = Cuadrado("Azul", 6)

    t1 = Triangulo("Verde", 3, 4, 5)
    t2 = Triangulo("Amarillo", 5, 5, 6)

    r1 = Redondo("Negro", 3)
    r2 = Redondo("Blanco", 5)

    print(c1)
    print(c2)
    print(t1)
    print(t2)
    print(r1)
    print(r2)

    if c1.obtenerArea() > t1.obtenerArea():
        print(f"figura con mayor área es el Cuadrado de color {c1.getColor()}")
    else:
        print(f"figura con mayor área es el Triángulo de color {t1.getColor()}") 