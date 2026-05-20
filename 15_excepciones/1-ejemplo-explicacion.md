# Pieza 15 - Excepciones

## Objetivo

Evitar que el programa se rompa por errores esperables.

## Concepto

`try` intenta ejecutar codigo.

`except` captura un error si ocurre.

Sirve para manejar entradas invalidas o archivos que faltan.

## Formula

```python
try:
    codigo_riesgoso
except TipoDeError:
    accion_si_falla
```

## Ejemplo

```python
try:
    edad = int(input("Edad: "))
    print(edad)
except ValueError:
    print("Tenes que escribir un numero")
```

## Tu problema

En `2-main.py`, pedi precio y stock por terminal.

Si el usuario escribe algo que no se puede convertir a numero, mostra un mensaje
claro y no dejes que el programa explote.

