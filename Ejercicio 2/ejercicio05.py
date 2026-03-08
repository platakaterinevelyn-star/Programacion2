class Minecraft():

    def __init__(self):
        self.jugadores=[]

    def jugador(self,nombre,diamante):
        if len(self.jugadores) < 10 :
            self.jugadores.append({"nombre":nombre ,"diamantes":diamante})
            print(f"jugador {nombre} agregado")
        else:
            print("lleno")

    def Diamantes(self):
        for jugador in self.jugadores:
            stacks = jugador["diamantes"] // 64
            sobra = jugador["diamantes"] % 64
            print(f"{jugador['nombre']},{stacks} stacks,{sobra} diamantes")

    def jugadorDiam(self):
        if not self.jugadores:
            print("sin jugadores")
            return
        max_jugador = self.jugadores[0]
        for j in self.jugadores:
            if j["diamantes"] > max_jugador["diamantes"]:
                max_jugador = j
        print( max_jugador["nombre"], "con", max_jugador["diamantes"])

    def total(self):
        suma = 0
        for j in self.jugadores:
            suma = suma + j["diamantes"]
        print("Total de diamantes:", suma)

d= Minecraft()
d.jugador("alejandro", 50)
d.jugador("wara", 130)
d.jugador("kurmi", 10)

d.jugadorDiam()
d.total()