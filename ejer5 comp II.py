n = int(input('cantidad de elementos de A: '))
a = [0] * n
for i in range(n):
    a[i] = int(input(f'A[{i+1}]: '))
print()

e = float(input('ingrese el escalar: '))

for i in range(n):
    a[i] = e + a[i]

print(f'el vector resultante es {a}')