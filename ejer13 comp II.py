m = int(input('numero de filas: '))
n = int(input('numero de columnos: '))

v = []

a = [[0] * n for i in range(m)]

for i in range(m):
    for j in range(n):
        a[i][j] = float(input(f'A[{i+1}][{j+1}]: '))
        
        
for i in range(m):
    for j in range(n):
        print(a[i][j], end = ' ')

    print()

for j in range(n):
        v.append(a[0][j])

    # Copiar el borde derecho
for i in range(1, m):
    v.append(a[i][n-1])

    # Copiar el borde inferior en orden inverso
for j in range(n-2, -1, -1):
    v.append(a[m-1][j])

    # Copiar el borde izquierdo en orden inverso
for i in range(m-2, 0, -1):
    v.append(a[i][0])


print(v)
