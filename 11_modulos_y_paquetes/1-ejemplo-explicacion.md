# Pieza 11 - Modulos y paquetes

## Objetivo

Dividir codigo en mas de un archivo.

## Concepto

Un modulo es un archivo `.py` que se puede importar desde otro archivo.

Sirve para que `main.py` no tenga todo mezclado.

## Formula

```python
from archivo import funcion
```

## Ejemplo

Archivo `saludos.py`:

```python
def saludar(nombre):
    return f"Hola {nombre}"
```

Archivo `main.py`:

```python
from saludos import saludar

print(saludar("Ana"))
```

## Tu problema

En esta pieza, ademas de `2-main.py`, crea vos un archivo `productos.py`.

En `productos.py`, defini una funcion que reciba un producto y lo muestre.

En `2-main.py`, importala y usala.

