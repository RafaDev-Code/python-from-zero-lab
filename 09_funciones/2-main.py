producto = {
    "nombre": "Silla Ergo",
    "precio": 100.99,
    "stock": 5
}


precio = producto["precio"]
stock = producto["stock"]
cantidad = int(input("Cantidad total a pedir: "))

def calcular_total(precio, cantidad):
    return precio * cantidad
resultado_monto_total = calcular_total(precio, cantidad)

def verificar_stock(stock, cantidad):
    return stock >= cantidad
control = verificar_stock(stock, cantidad)

def mostrar(producto):
    print("Esta es la ", producto)


if control == False:
    print("No hay stock disponible")
elif control == True:
    print("Hay stock disponible")
    print("El monto total es de ", resultado_monto_total)
    mostrar(producto)
else:
    print("ocurrio algo raro")





    
