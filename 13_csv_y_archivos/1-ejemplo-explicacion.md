# Pieza 13 - CSV y archivos

## Objetivo

Guardar datos tipo tabla.

## Concepto

CSV significa valores separados por comas.

Python trae el modulo `csv` para leer y escribir filas.

## Formula

```python
import csv

with open("archivo.csv", "w", newline="") as archivo:
    escritor = csv.writer(archivo)
    escritor.writerow(["columna1", "columna2"])
```

## Ejemplo

```python
import csv

with open("clientes.csv", "w", newline="") as archivo:
    escritor = csv.writer(archivo)
    escritor.writerow(["nombre", "email"])
    escritor.writerow(["Ana", "ana@mail.com"])
```

## Tu problema

En `2-main.py`, crea un CSV de productos con columnas:

- nombre
- precio
- stock

Escribi al menos 3 productos.

Despues lee el CSV y mostralo en terminal.

