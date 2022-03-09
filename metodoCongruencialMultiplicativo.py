


# constante = 35
# semilla = 15
# moduloInicial = 64

constante = int(input("Ingresa la constante: "))
semilla = int(input("Ingresa la semilla: "))
moduloInicial = int(input("Ingresa el modulo: "))




for i in range(10):
    numero = (constante * semilla) % moduloInicial
    numero2 = numero / (moduloInicial - 1)
    semilla = numero
    print(numero)

