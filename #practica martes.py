#practica
import random

def llenadoAleatorio(mat,f,c):
    for i in range(f):
        for j in range(c):
            mat[i][j] = random.randint(1,9)

def llenadoManual(mat,f,c):
    for i in range(f):
        for j in range(c):
            mat[i][j] = int(input(f'matriz[{i},{j}]'))


def mostrarVector(mat,f,c):
    for i in range(f):
        for j in range(c):
            print(mat[i][j],end = ' ')
        print()

def cargarVector(v,n):
    
    for i in range(n):
        v[i] = int(input(f'v[{i+1}]: '))
    

def mostrarVector(v,n):
    for i in range(n):
        print(v[i],end = ' ')

    print()

def insertaFila(mat,f,c,fil,v):
    mat.extend([0])
    mat[f] = [0] * c
    for i in range(f-1,fil-2,-1):
        for j in range(c):
            mat[i+1][j] = mat[i][j]
        
    for j in range(c):
        mat[fil-1][j] = v[j]
    return f + 1

def insertaColumna(mat,f,c,col,v):
    for i in range(f):

        mat[i].extend([0])
    for i in range(f):
        for j in range(c-1,col-2,-1):
            mat[i][j+1] = mat[i][j]
    
    for i in range(j):
        mat[i][col-1] = v[i]

def mostrarMatriz(mat,f,c):
    for i in range(f):
        for j in range(c):
            print(mat[i][j],end = ' ')
        print()

def eliminarFila(mat,f,c,fil):
    for i in range(fil-1,f-1):
        for j in range(c):
            mat[i][j] = mat[i+1][j]
    return f - 1

def eliminarColumna(mat,f,c,col):
    for i in range(f):
        for j in range(col-1,c-1):
            mat[i][j] = mat[i][j+1]
    return c - 1

def ordenamientoFilaColumnaInd(mat,f,c):
    aux = 0
    for i in range(c-1):
        for j in range(i+1,c):
            if mat[f][i] > mat[f][j]:
                aux = mat[f][i]
                mat[f][i] = mat[f][j]
                mat[f][j] = aux

def ordenamientoFilaColumnaDep(mat,k,f,c):
    aux = 0
    for i in range(c-1):
        for j in range(i+1,c):
            if mat[k][i] > mat[k][j]:
                for s in range(f):
                    aux = mat[s][i]
                    mat[s][i] = mat[s][j]
                    mat[s][j] = aux

def convMatrizAVector(mat,f,c,v):
    i=0
    j=0
    tv = 0 
    for i in range(f):
        for j in range(c):
            v[tv] = mat[i][j]
            tv =tv+ 1
    return v

def ConvVectorAMatriz(mat,f,c,v):
    tv = 0
    for i in range(f):
        for j in range(c):
            mat[i][j] = v[tv]
            tv += 1

def ordVector(v):
    n=len(v)
    for i in range(n-1):
        for j in range((n-1)-i):
            if v[j] > v[j+1]:
                temp = v[j]
                v[j] = v[j+1]
                v[j+1]=temp

def ordenarMatriz(mat,f,c):
    
    v = [0] * f * c
    convMatrizAVector(mat,f,c,v)
    ordVector(v)
    ConvVectorAMatriz(mat,f,c,v)

def busquedaSecuencial(v,valor):
    n = len(v)
    i = 0
    while (i < n) and (v[i] != valor):
        i = i+1
    if (i < n) and (v[i] == valor):
        return i
    else:
        return -1
    
def buscarElemento(mat,f,c):
    v = [0] * f * c
    v=convMatrizAVector(mat,f,c,v)
    valor = input('inserte valor a buscar: ')
    pos=busquedaSecuencial(v,valor)
    print(f'su valor esta en la pos {pos}')


#Principal

print()
print(' 1. Crear matriz A')
print(' 2. Cargar matriz aleatoriamente')
print(' 3. Cargar matriz manualmente')
print(' 4. Mostrar matriz')
print(' 5. Insertar una fila en A')
print(' 6. Insertar una columna en A')
print(' 7. Eliminar fila de A')
print(' 8. Elimina columna de A')
print(' 9. Ordenar todos los elementos de la matriz ')
print()

opc = int(input('Seleccione su opcion: '))
while opc != 0:
    
    v = [0]
    if opc != 1:   
        print()
        print(' 1. Crear matriz A')
        print(' 2. Cargar matriz aleatoriamente')
        print(' 3. Cargar matriz manualmente')
        print(' 4. Mostrar matriz')
        print(' 5. Insertar una fila en A')
        print(' 6. Insertar una columna en A')
        print(' 7. Eliminar fila de A')
        print(' 8. Elimina columna de A')
        print(' 9. Ordenar todos los elementos de la matriz ')
        print()

    
    if opc == 1:
        f = int(input('Cuantos filas tiene la matriz?: '))
        c = int(input('Cuantos columnas tiene la matriz?: '))
        while (f < 0 and c < 0):
            f = int(input('Cuantos filas tiene la matriz?: '))
            c = int(input('Cuantos columnas tiene la matriz?: '))
        a = [[0]*c for i in range(f)]
        print('Matriz creada!')
        print()

    elif opc == 2:
        llenadoAleatorio(a,f,c)

    elif opc == 3:
        llenadoManual(a,f,c)

    elif opc == 4:
        mostrarMatriz(a,f,c)
        print()
    
    elif opc == 5:
        v = [0] * c
        print('Cargue la fila:')
        cargarVector(v,c)
        fila = int(input('Ingrese la posicion de insercion de la nueva fila: '))
        insertaFila(a,f,c,fila,v)
        print()

    elif opc == 6:
        v = [0] * f
        print('Cargue la columna:')
        cargarVector(v,f)
        col = int(input('Ingrese la posicion de insercion de la nueva columna: '))
        insertaColumna(a,f,c,col,v)
        print()

    elif opc == 7:
        fila = int(input('Ingrese la posicion de la fila a eliminar:'))
        f = eliminarFila(a,f,c,fila)
        print()
    
    elif opc == 8:
        col = int(input('Ingrese la posicion de la columna a eliminar:'))
        c = eliminarColumna(a,f,c,col)
        print()

    else:
        print('Fin del programa!')

    opc = int(input('Seleccione su opcion: '))
