m = int(input('numero de filas: '))
n = int(input('numero de columnos: '))
s = 0
a = [[0] * n for i in range(m)]

for i in range(m):
    for j in range(n):
        a[i][j] = float(input(f'A[{i+1}][{j+1}]: '))

        if j == 0 or j == n - 1 or i == j:
            s += a[i][j]
        
        
for i in range(m):
    for j in range(n):
        print(a[i][j], end = ' ')

    print()

print(s)
