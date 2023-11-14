n = int(input('n: \n'))

v = [0] * n
w = [0] * n

print('llenado de v: \n')
for i in range(n):
    v[i] = int(input(f'V[{i+1}]: '))

print('llenado de w: \n')
for i in range(n):
    w[i] = int(input(f'W[{i+1}]: '))

print('Calculando el producto escalar...\n')
prod = 0
for i in range(n):
    prod += v[i]*w[i]

print(f'El producto escalar de V y W es: {prod:.2f}')

        
