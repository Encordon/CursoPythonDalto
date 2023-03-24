import csv


with open("ARCHIVOS\\datos.csv") as archivo:
    reader = csv.reader(archivo)
    for row in reader:
        print(row)
