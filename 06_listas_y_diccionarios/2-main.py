productos = []

producto_silla = {
    "nombre": "silla",
    "stock": 0,
}

producto_escritorio = {
    "nombre": "escritorio",
    "stock": 0,
}

producto_periferico = {
    "nombre": "periferico",
    "stock": 0,
}

productos.append(producto_silla)
productos.append(producto_escritorio)
productos.append(producto_periferico)

producto_silla["stock"] = int(input("cambiar stock de sillas: "))
producto_escritorio["stock"] = int(input("cambiar stock de escritorios: "))
producto_periferico["stock"] = int(input("cambiar stock de perifericos: "))

print(productos)
print(producto_silla)
print(producto_escritorio)
print(producto_periferico)