
#TERMINADO


# constante = 6965
# semilla = 9803
constante = input("Ingresa la constante: ")
semilla= input("Ingresa la semilla: ")
while len(constante) < 4 or len(semilla) < 4:

        print("La semilla y/o la constante debe ser > 4 digitos")

        constante = input("Ingresa la constante: ")
        semilla= input("Ingresa la semilla: ")


for i in range(10):

    constante = int(constante)
    semilla = int(semilla)
    resultado = constante * semilla
    resultado = str(resultado)
    semilla = resultado[2:6]
    semilla = int(semilla)  

    print(semilla/10000)

    



    




