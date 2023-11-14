n = int(input('cantidad de elementos de A: '))
a = [0] * n
for i in range(n):
    a[i] = int(input(f'A[{i+1}]: '))
print()

menor = float('inf')
mayor = 0

for i in range(n):
    if mayor < a[i]:
        mayor = a[i]
    if menor > a[i]:
        menor = a[i]

print(f'el menor es: {menor} y el mayor es: {mayor}')