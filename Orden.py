from Computadora import Computadora
from Monitor import Monitor
from Raton import Raton
from Teclado import Teclado


class Orden:
    contadorOrdenes = 0

    def __init__(self, computadoras):
        Orden.contadorOrdenes += 1
        self._idOrden = Orden.contadorOrdenes
        self._computadoras = list(computadoras)

    @property
    def idOrden(self):
        return self._idOrden

    @idOrden.setter
    def idOrden(self, idOrden):
        self._idOrden = idOrden

    @property
    def computadoras(self):
        return self._computadoras

    @computadoras.setter
    def computadoras(self, computadora):
        self._computadoras = computadora

    def agregarComputadora(self,computadora):
        self.computadoras.append(computadora)

    def __str__(self):
        computadoras_str = ''
        for computadora in self.computadoras:
            computadoras_str += computadora.__str__()

        return f'''
        Orden: {self.idOrden}
        computadoras: {computadoras_str}
        '''

if __name__ == '__main__':
    teclado1 = Teclado('HP', 'usb')
    raton1 = Raton('HP','usb')
    monitor1 = Monitor('Hp', '15 pulgadas')
    computadora1 = Computadora('HP', monitor1, teclado1, raton1)


    teclado2 = Teclado('HP', 'usb')
    raton2 = Raton('HP', 'usb')
    monitor2 = Monitor('Hp', '15 pulgadas')
    computadora2 = Computadora('HP', monitor2, teclado2, raton2)

    listaComputadoras = [computadora1,computadora2]
    orden1 = Orden(listaComputadoras)
    print(orden1)
