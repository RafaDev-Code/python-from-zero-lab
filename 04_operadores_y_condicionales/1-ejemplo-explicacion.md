# Pieza 04 - Operadores y condicionales

## Objetivo

Calcular valores y tomar decisiones.

## Concepto

Los operadores aritmeticos calculan.

Los operadores de comparacion preguntan.

`if` ejecuta codigo solo si una condicion se cumple.

## Formula

```python
if condicion:
    accion_si_es_verdad
else:
    accion_si_es_falso
```

## Ejemplo

```python
edad = 20

if edad >= 18:
    print("Puede entrar")
else:
    print("No puede entrar")
```

## Tu problema

En `2-main.py`, crea:

- precio
- cantidad
- stock

Calcula el total de una compra.

Si la cantidad pedida es menor o igual al stock, mostra:

```text
Venta posible
```

Si no, mostra:

```text
No hay stock suficiente
```

