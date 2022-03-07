

from operator import mod


constante = 3
semilla = 17
moduloInicial = 100

modulo = (constante * semilla) % moduloInicial
numeroAleatorio = modulo / (moduloInicial - 1)
print(modulo)
print(numeroAleatorio)
