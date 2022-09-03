from DispositivoEntrada import DispositivoEntrada


class Teclado(DispositivoEntrada):
    contadorTeclado = 0

    def __init__(self, tipoEntrada, marca):
        Teclado.contadorTeclado += 1
        super().__init__(tipoEntrada, marca)
        self.idTeclado = Teclado.contadorTeclado

    def __str__(self):
        return f'Id: {self.idTeclado}, marca: {self.marca}, tipo_entrada: {self.tipoEntrada}'

if __name__ == '__main__':
    teclado1 = Teclado('HP', 'usb')
    print(teclado1)
    teclado2 = Teclado('Gamer', 'bluetooth')
    print(teclado2)