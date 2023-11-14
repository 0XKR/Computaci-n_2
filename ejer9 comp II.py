m = int(input('numero de filas: '))
n = int(input('numero de columnos: '))

a = [[0] * n for i in range(m)]

for i in range(m):
    for j in range(n):
        a[i][j] = float(input(f'A[{i+1}][{j+1}]: '))
        

    print()




for i in range(m):
    sumf = 0
    
    for j in range(n):
        print(a[i][j], end = ' ')
        sumf += a[i][j]
    print(sumf)


    print()


