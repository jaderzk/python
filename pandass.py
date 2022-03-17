import pandas as pd

print ("Ejercicio de Dataframes con Pandas")
dffelicidad = pd.read_csv("https://raw.githubusercontent.com/AlanCIO/hapinnes/main/world-happiness-report-2021.csv")
print(dffelicidad)

for d in dffelicidad:
    print("dato:", d)