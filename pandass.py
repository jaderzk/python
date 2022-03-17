import pandas as pd
import numpy as np

arreglo = [1,21,3,4,5,6]
nmpys = np.array(arreglo)

print("el tamaño del arreglo es: ", nmpys.size)

print("el maximo del arreglo es: ", nmpys.max())

print("el mínimo del arreglo es: ", nmpys.min())


print ("Ejercicio de Dataframes con Pandas")
dffelicidad = pd.read_csv("https://raw.githubusercontent.com/AlanCIO/hapinnes/main/world-happiness-report-2021.csv")
print(dffelicidad)

for d in dffelicidad:
    print("dato:", d)
    

print("Las columnas del DataFrame:", dffelicidad.columns)    
print("Los valores del DataFrame:", dffelicidad.values) 
    
print("La cantidad de valores del DataFrame:", dffelicidad.count())    
