# Herencia, es la posibilidad de compartir atributos y metodos entre clases

class Persona:
    '''
    nombre =
    apellidos =
    altura =
    edad =
    '''
    @property
    def getNombre(self):
        return self.nombre

    @property
    def getApellidos(self):
        return self.apellidos

    @property
    def getAletura(self):
        return self.altura

    @property
    def getEdad(self):
        return self.edad


    def setNombre(self, nombre):
        self.nombre = nombre

    def setApellidos(self, apellidos):
        self.apellidos = apellidos

    def setAltura(self, altura):
        self.altura = altura

    def setEdad(self, edad):
        self.edad = edad

    def hablar(self):
        return 'Estoy Hablando'

    def caminar(self):
        return 'Estoy caminando'

    def dormir(self):
        return 'Estoy durmiendo'


class Informatico(Persona):
    '''
    lenuajes
    experiencia
    '''

    def __init__(self):
        self.lenguajes = 'HTML, CSS, JAVASCRIPT'
        self.experiencia = 5

    def getLenguajes(self):
        return self.lenguajes

    def getExperiencia(self):
        return self.experiencia

    def programar(self):
        return 'Estoy programando'

    def reparar(self):
        return 'Estoy reparando'