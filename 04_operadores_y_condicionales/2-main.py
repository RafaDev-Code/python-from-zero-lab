cantidad = int(input("cantidad: "))

producto_1 = {
    "nombre": "escritorio" ,
    "precio": 399.99,
    "stock": 20,
    "activo": True,
}

total = producto_1["precio"] * cantidad

if cantidad <= producto_1["stock"]:
    print("Tenemos stock!")
    print("el total es: ", total, "usd")
else:
    print(" No hay stock suficiente :/ ")


