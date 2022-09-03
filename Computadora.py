from Monitor import Monitor
from Raton import Raton
from Teclado import Teclado


class Computadora:
    contadorComputadoras = 0

    def __init__(self, nombre, monitor, teclado, raton):
        Computadora.contadorComputadoras += 1
        self._nombre = nombre
        self._monitor = monitor
        self._teclado = teclado
        self._raton = raton

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def monitor(self):
        return self._monitor

    @monitor.setter
    def monitor(self, monitor):
        self._monitor = monitor

    @property
    def teclado(self):
        return self._teclado

    @teclado.setter
    def teclado(self, teclado):
        self._teclado = teclado

    @property
    def raton(self):
        return self._raton

    @raton.setter
    def raton(self, raton):
        self._raton = raton

    def __str__(self):
        return f'''
        {self.nombre}: {self.contadorComputadoras}
        Monitor: {self.monitor}
        Teclado: {self.teclado}
        Raton: {self.raton}
        '''
if __name__ == '__main__':
    teclado1 = Teclado('HP', 'usb')
    raton1 = Raton('HP','usb')
    monitor1 = Monitor('Hp', '15 pulgadas')
    computadora1 = Computadora('HP', monitor1, teclado1, raton1)
    print(computadora1)
