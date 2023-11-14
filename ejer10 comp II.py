m = int(input('numero de filas: '))
n = int(input('numero de columnos: '))
mcol = [0] * n

a = [[0] * n for i in range(m)]

for i in range(m):
    for j in range(n):
        a[i][j] = float(input(f'A[{i+1}][{j+1}]: '))
        mcol[j] += a[i][j]

for i in range(m):
    for j in range(n):
        print(a[i][j], end = ' ')

    print()

for j in range(n):
    print(mcol[j], end = ' ')







