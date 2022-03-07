def mixedMethod(x, a, c, mod):
 
    periodo = 0
    bandera = 0
 
    while(bandera != x):
        if (periodo == 0):
            bandera = x
        x = (a * x + c) % mod
        print(x)
        periodo = periodo + 1
 
    if(periodo == mod):
        print("El periodo es completo: ", periodo)
    else:
        print("El periodo es incompleto:", periodo)
 
def main():
    x = int(raw_input("Introduce el valor de la semilla: "))
    a = int(raw_input("Introduce el valor del multiplicador: "))
    c = int(raw_input("Introduce el valor de la constante aditiva: "))
    m = int(raw_input("Introduce el valor del modulo: "))
    mixedMethod(x,a,c,m)