m = int(input('numero de filas: '))
n = int(input('numero de columnos: '))

a = [[0] * n for i in range(n)]

for i in range(n):
    for j in range(m):
        a[i][j] = float(input(f'A[{i+1}][{j+1}]: '))

    print()

menor = float('inf')
mayor = 0
for i in range(n):
    for j in range(m):
        if mayor < a[i][j]:
            mayor = a[i][j]
        if menor > a[i][j]:
            menor = a[i][j]

print(f'Mayor: {mayor}, Menor: {menor}') 