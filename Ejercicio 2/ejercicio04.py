class Bus():
    def __init__(self,asientos):
        self.asientos= asientos
        self.pasajeros=0

    def Subenpasajeros(self,X):
        if self.pasajeros + X <= self.asientos:
            self.pasajeros = self.pasajeros + X
            print("suben",X,"pasajeros")
        else:
            print("no quedan asientos")

    def cobrar(self):
        costo=1.50
        pago= self.pasajeros * costo
        print("pagaron:",pago,"Bs")

    def asientosDisponibles(self):
        dispo=self.asientos - self.pasajeros 
        print("disponibles",dispo)

d=Bus(30)
d.Subenpasajeros(17)
d.cobrar()
d.asientosDisponibles()
