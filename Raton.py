from DispositivoEntrada import DispositivoEntrada


class Raton(DispositivoEntrada):
    contadorRaton = 0

    def __init__(self, marca, tipoEntrada):
        Raton.contadorRaton += 1
        super().__init__(marca,tipoEntrada)
        self.idRaton = Raton.contadorRaton

    def __str__(self):
        return f'ID: {self.contadorRaton}, marca: {self.marca}, tipo_entrada: {self.tipoEntrada} '


if __name__ == '__main__':
    raton1 = Raton('HP','usb')
    print(raton1)

    raton2 = Raton('ACER','Bluetooth')
    print(raton2)