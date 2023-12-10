def cargarArchivo():
	arch = open('datos.txt','r')
	cont = arch.readlines()
	ave = cont[0].split(',')
	c = len(ave) + 1
	f = len(cont)
	calle = [0] * (f-1)
	matriz =[[0]*c for i in range(f)]
	
	for j in range(1,c):
		matriz[0][j]=ave[j-1]
		
	for i in range(1,f):
		for j in range(c):
			linea = cont[i].split(',')
			matriz[i][j] = linea[j]
			calle[i-1] = linea[0]
	arch.close()
	return matriz, f, c, calle, ave
	
	'''
	print(matriz)
	print()
	print(calle)
	print(ave)
	'''
def actualizarArch(mat,f,c):
	arch = open('datos.txt','w')
	for i in range(f):
		for j in range(c):
			if j < c-1:
				arch.write(str(mat[i][j]))
				arch.write(',')
				
			else:
				arch.write(str(mat[i][j]))
				arch.write('\n')
	arch.close()

def sumarFilaColumna(matriz, f, c, fila, columna):
	
	suma = 0
	for j in range(1,c-1):
		suma += int(matriz[fila][j])
		
	for i in range(1,f-1):
		suma += int(matriz[i][columna])
	suma -= int(matriz[fila][columna])
	return suma

def crucePeligroso(mat,f,c,fila,):
	mayor = 0
	for i in range(1,f-1):
		for j in range(1,c-1):
			suma = sumarFilaColumna(mat,f,c,i,j)
			if mayor < suma:
				fila = i - 1
				columna = j - 1
				total = suma

	return fila,columna,total
	


def insertCalle(mat,f,c,fila,v):

	mat.extend([0])
	mat[f] = [0] * c
	for i in range(f-1,fila-2,-1):
		for j in range(c):
			mat[i+1][j] = mat[i][j]
	for j in range(c):
		mat[fila-1][j] = v[j]

	f += 1
	actualizarArch(mat,f,c)

	return f + 1

def  insertAvenida(mat,f,c,col,v):
	for i in range(f):
		mat[i].extend([0])
	for i in range(f):
		for j in range(c-1,col-2,-1):
			mat[i][j+1] = mat[i][j]
	for i in range(f):
		mat[i][col-1] = v[i]

	c += 1
	actualizarArch(mat,f,c)
	return c + 1

def eliminarCalle(mat,f,c,fila):
	for i in range(fila-1,f-1):
		for j in range(c):
			mat[i][j] = mat[i+1][j]
	
	f -=1
	actualizarArch(mat,f,c)
	return f - 1

def eliminarAvenida(mat,f,c,col):
	for i in range(f):
		for j in range(col-1,c-1):
			mat[i][j] = mat[i][j+1]
	
	c -=1
	actualizarArch(mat,f,c)
	return c - 1

def mostrarDatos(mat,f,c,calle,ave):
	
		for j in range(c-1):
			if j == 0:
				print(f'           {ave[j]}',end=' ')
			else:
				print(f'{ave[j]}',end=' ')
		print()
			
		for i in range(1,f-1):
			for j in range(c):
				if c==0:
					print(calle[j],end = ' ')
				else: 
					print(mat[i][j],end=' ')
			print()
