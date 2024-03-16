import csv
import random

archivo_csv_original = input("Ingrese  el archivo a desordenar: ")
archivo_csv_desordenado = archivo_csv_original.replace(".csv",  "_desordenado.csv")
datos = []

with open(archivo_csv_original, newline='') as csvfile:
    lector_csv = csv.reader(csvfile)
    primera_fila = next(lector_csv)
    for fila in lector_csv:
        datos.append(fila)

random.shuffle(datos)
with open(archivo_csv_desordenado, mode='w', newline='') as csvfile:
    escritor_csv = csv.writer(csvfile)
    escritor_csv.writerow(primera_fila)
    for fila in datos:
        escritor_csv.writerow(fila)

