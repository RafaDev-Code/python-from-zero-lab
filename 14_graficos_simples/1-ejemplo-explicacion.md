# Pieza 14 - Graficos simples

## Objetivo

Visualizar cantidades de forma simple.

## Concepto

Un grafico no siempre necesita una libreria.

Para aprender la idea, se puede hacer un grafico de barras en texto.

## Formula

```python
print(nombre, "#" * cantidad)
```

## Ejemplo

```python
ventas = {
    "lunes": 3,
    "martes": 5,
    "miercoles": 2,
}

for dia, cantidad in ventas.items():
    print(dia, "#" * cantidad)
```

## Tu problema

En `2-main.py`, crea un diccionario con productos y stock.

Mostra un grafico en texto donde cada `#` represente una unidad de stock.

Ejemplo de salida esperada, no de codigo:

```text
lapiz #####
cuaderno ########
```

