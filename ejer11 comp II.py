m = int(input('numero de filas: '))
n = int(input('numero de columnos: '))

a = [[0] * n for i in range(m)]
sumdia1 = 0
sumdia2 = 0
for i in range(m):
    for j in range(n):
        a[i][j] = float(input(f'A[{i+1}][{j+1}]: '))
        if i == j:
            sumdia1 += a[i][j]
        if (i + j + 2) == (m + 1):
            sumdia2 += a[i][j]

        
for i in range(m):
    for j in range(n):
        print(a[i][j], end = ' ')

    print()
print()

print(f'la suma de la diagonal principal es: {sumdia1}')

print(f'la suma de la diagonal secundaria es: {sumdia2}')