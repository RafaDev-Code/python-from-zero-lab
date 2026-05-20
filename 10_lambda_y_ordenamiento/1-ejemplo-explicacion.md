# Pieza 10 - Lambda y ordenamiento

## Objetivo

Ordenar datos usando una clave.

## Concepto

`sorted()` ordena una coleccion.

`lambda` sirve para crear una funcion chica en el lugar donde se necesita.

## Formula

```python
sorted(lista, key=lambda elemento: elemento["clave"])
```

## Ejemplo

```python
personas = [
    {"nombre": "Ana", "edad": 32},
    {"nombre": "Luis", "edad": 25},
]

ordenadas = sorted(personas, key=lambda persona: persona["edad"])
print(ordenadas)
```

## Tu problema

En `2-main.py`, crea una lista de productos.

Mostralos ordenados por:

- precio
- stock

No modifiques la lista original: crea listas ordenadas nuevas.

