import re

patron = r"PROD-[0-9]{3}"
codigo_1 = "PROD-002"
codigo_2 = "ACBE-321200"

if re.fullmatch(patron, codigo_1):
    print("Codigo 1 valido")
else:
    print("Codigo 1 invalido")

if re.fullmatch(patron, codigo_2):
    print("Codigo 2 valido")
else:
    print("Codigo 2 invalido")
