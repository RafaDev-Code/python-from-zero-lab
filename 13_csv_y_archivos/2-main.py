import csv

with open("productos.csv", "w", newline="") as pepe:
    escribir = csv.writer(pepe)
    escribir.writerow(["nombre", "precio", "stock"])
    escribir.writerow(["silla", 150.99, 25])
    escribir.writerow(["mesa", 300.99, 25])
    escribir.writerow(["pala", 20.99, 25])
    escribir.writerow(["martillo", 6.99, 25])

with open("productos.csv", "r") as pepe:
    leer = csv.reader(pepe)
    for row in leer:
        print(row)