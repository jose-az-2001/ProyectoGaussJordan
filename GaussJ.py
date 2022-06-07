#programa para resolver ecuaciones por medio de Gauss-Jordan

import numpy as np
import sys

def RecibirEcuaciones(incognitas):
    ecua = []
    for i in range (0, incognitas):
        valor = float(input("Ingrese el valor: "))
        ecua = ecua + [valor]
    return ecua


print("Programa para resolver ecuaciones por Gauss-Jordan")
filas = int(input("cuantas incognitas tendra el sistema: "))
columnas = filas
mat = np.zeros([filas, columnas+1], dtype=float)
x = np.zeros(filas)
print(mat)

for i in range(0, filas):
    ecn = np.array(RecibirEcuaciones(columnas +1))
    mat[i]=ecn
    
    print(mat)
    
#operaciones

for i in range(filas):
    if mat[i][i] == 0.0:
        sys.exit('Divsion incorrecta detectada')
        
    for j in range(filas):
        if i != j:
            ratio = mat[j][i]/mat[i][i]

            for k in range(filas+1):
                mat[j][k] = mat[j][k] - ratio * mat[i][k]
    print(mat)

#Obtener soluciones

for i in range(filas):
    x[i] = mat[i][filas]/mat[i][i]
                
           
print('\nLa solucion es: ')
for i in range(filas):
    print('X%d = %0.2f' %(i,x[i]), end = '\t' )
        

 