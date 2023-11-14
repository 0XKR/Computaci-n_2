def copiar_bordes(matriz):
    m = len(matriz)
    n = len(matriz[0])
    v = []

    # Copiar el borde superior
    for j in range(n):
        v.append(matriz[0][j])

    # Copiar el borde derecho
    for i in range(1, m):
        v.append(matriz[i][n-1])

    # Copiar el borde inferior en orden inverso
    for j in range(n-2, -1, -1):
        v.append(matriz[m-1][j])

    # Copiar el borde izquierdo en orden inverso
    for i in range(m-2, 0, -1):
        v.append(matriz[i][0])

    return v

# Ejemplo de uso
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

vector_resultante = copiar_bordes(matriz)
print(vector_resultante)