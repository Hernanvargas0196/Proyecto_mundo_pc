from Persona import *
persona = Persona()
persona.setNombre('Victor')
persona.setApellidos('Robles')
persona.setEdad('800años')
persona.setAltura('190 cm')

print(f'La persona es : {persona.getNombre} {persona.getApellidos}')
print(persona.hablar())

informatico = Informatico()
informatico.setNombre('Carlos')
informatico.setApellidos('Martinez')

print(f'El informatico es: {informatico.getApellidos} {informatico.getApellidos}')
print(informatico.programar())