#suma de los cuadrados de las comp. del vector

n = int(input('Ingrese los elementos del vector: '))

v = [0] * n

for i in range(n):
    v[i] = float(input(f'v[{i+1}]: '))
print()
s = 0 
for i in range(n):
    s += v[i] ** 2

print(f'la suma de cuadrados es: {s}')
