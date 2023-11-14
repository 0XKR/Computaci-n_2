import random

#declaracion de variables 

def llenadoManual(mat,f,c):
    for i in range(f):
        for j in range(c):
            mat[i][j] = int(input(f'mat[{i+1},{j+1}]: '))

def llenadoAleatorio(mat,f,c):
    for i in range(f):
        for j in range(c):
            mat[i][j] = random.randint(1,9)

def mostrarMatriz(mat,f,c):
    for i in range(f):
        for j in range(c):
            print(mat[i][j], end = ' ')
        print()

#cuerpo principal

#variables de entrada 

opc = 1
fa = 0
ca = 0
a = [[]]

#variables de salida
print()
print('Nueva ejecución')
while opc != 0:
    print('1. Crear Matriz A de F x C')
    print('2. Llenar matriz A de F x C')
    print('3. Llenar matriz aleatoriamente')
    print('4. Mostrar matriz A')
    print('0. salir')

    opc = int(input('Seleccione la opción: '))

    if opc == 1:
        fa = int(input('Ingrese las filas de la matriz A: '))
        while fa <= 0:
            fa = int(input('Ingrese las filas de la matriz A: '))
        ca = int(input('Ingrese las columnas de la matriz A: '))
        while ca <= 0:
            ca = int(input('Ingrese las columnas de la matriz A: '))
        a = [[0] * ca for i in range(fa) ]
    elif opc == 2:
        llenadoManual(a,fa,ca)
        print()

    elif opc == 3:
        llenadoAleatorio(a,fa,ca)
        print()
    
    elif opc == 4:
        mostrarMatriz(a,fa,ca)
        print()
    
    elif opc == 0 :
        print('Fin del programa, hasta luego =D')

    else:
        print('Opcion invalida!')