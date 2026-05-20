# Pieza 12 - Archivos TXT

## Objetivo

Leer y escribir archivos de texto.

## Concepto

`open()` abre un archivo.

Con modo `"w"` escribis.

Con modo `"r"` lees.

Usar `with` hace que Python cierre el archivo solo.

## Formula

```python
with open("archivo.txt", "w") as archivo:
    archivo.write("texto")
```

## Ejemplo

```python
with open("nota.txt", "w") as archivo:
    archivo.write("Recordar comprar insumos")

with open("nota.txt", "r") as archivo:
    contenido = archivo.read()

print(contenido)
```

## Tu problema

En `2-main.py`, guarda en un TXT una nota de stock.

Despues lee el archivo y mostra el contenido.

El archivo puede llamarse `stock.txt`.

