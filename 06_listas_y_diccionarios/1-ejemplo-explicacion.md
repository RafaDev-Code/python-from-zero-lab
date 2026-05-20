# Pieza 06 - Listas y diccionarios

## Objetivo

Agregar, buscar y modificar datos dentro de colecciones.

## Concepto

Las listas sirven para colecciones ordenadas.

Los diccionarios sirven para representar una cosa con varias propiedades.

## Formula

```python
lista.append(valor)
diccionario["clave"] = nuevo_valor
```

## Ejemplo

```python
tareas = []
tareas.append("limpiar")
tareas.append("comprar")

tarea = {"nombre": "limpiar", "hecha": False}
tarea["hecha"] = True

print(tareas)
print(tarea)
```

## Tu problema

En `2-main.py`, crea una lista vacia de productos.

Agrega 3 productos como diccionarios.

Despues modifica el stock de uno y mostra la lista completa.

