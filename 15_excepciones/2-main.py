

try: 
    precio = float(input("Cargar Precio: "))
    stock = int(input("Cargar Stock: "))
    print(precio, stock)
except ValueError:
    print("Tenes que escribir un numero")