n = int(input('cantidad de elementos de A: '))
a = [0] * n

for i in range(n):
    a[i] = int(input(f'A[{i+1}]: '))
print()
suma = 0 
for i in range(n):
    suma += a[i]
print()

media = suma / n
print(f'la media de los elementos de A es: {media:.2f}')

