# Pieza 07 - Inputs

## Objetivo

Pedir datos al usuario desde la terminal.

## Concepto

`input()` pausa el programa y espera que el usuario escriba algo.

Todo lo que entra por `input()` entra como texto.

## Formula

```python
respuesta = input("Pregunta: ")
numero = int(respuesta)
```

## Ejemplo

```python
nombre = input("Tu nombre: ")
edad_texto = input("Tu edad: ")
edad = int(edad_texto)

print(nombre)
print(edad + 1)
```

## Tu problema

En `2-main.py`, pedi:

- nombre de producto
- precio
- stock

Converti precio a `float`.

Converti stock a `int`.

Mostra un resumen del producto cargado.

