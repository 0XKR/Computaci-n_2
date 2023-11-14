import random
n= int(input('filas: '))
m= int(input('columnas: '))
matriz = [[0]*m for i in range(n)]
matriz1 = [[0]*m for i in range(n)]
summatriz = [[0]*m for i in range(n)]
sfila = [0] * n
scolumna = [0] *m

for i in range(n):
    for j in range(m):
        matriz[i][j] = random.randint(1,8)
        matriz1[i][j] = random.uniform(1,8)
        summatriz[i][j] = matriz[i][j] + matriz1[i][j]
        sfila[i] = sfila[i] + summatriz[i][j]
        scolumna[j] = scolumna[j] + summatriz[i][j]

print('Matriz Cargada...')
for i in range(n):
    for j in range(m):
        print(matriz[i][j],end=' ')
    print()

print('Matriz 1 Cargada...')
for i in range(n):
    for j in range(m):
        print('{0:2.2f}'.format(matriz1[i][j]),end=' ')
    print()

print('Matriz suma y total fila')
for i in range(n):
    for j in range(m):
        print('{0:2.2f}'.format(summatriz[i][j]),end=' ')
    print('{0:2.2f}'.format(sfila[i]))
for j in range(m):
    print('{0:2.2f}'.format(scolumna[j]),end=' ')