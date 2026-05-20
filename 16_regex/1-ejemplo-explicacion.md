# Pieza 16 - Regex

## Objetivo

Validar textos que tienen un patron.

## Concepto

Una expresion regular describe una forma de texto.

En Python se usa el modulo `re`.

## Formula

```python
import re

re.fullmatch(patron, texto)
```

## Ejemplo

```python
import re

patron = r"[A-Z]{3}-[0-9]{2}"
codigo = "ABC-12"

if re.fullmatch(patron, codigo):
    print("Codigo valido")
else:
    print("Codigo invalido")
```

## Tu problema

En `2-main.py`, valida codigos de producto con este formato:

```text
PROD-001
```

Regla:

- empieza con `PROD-`
- termina con 3 numeros

Proba un codigo valido y uno invalido.

