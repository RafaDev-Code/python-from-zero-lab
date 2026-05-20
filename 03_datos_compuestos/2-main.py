producto_escritorio = {
    "nombre": "Escritorio 100x100x80",
    "precio": 399.99,
    "stock": 20,
    "activo": True
}

producto_silla = {
    "nombre": "Silla Ergonomica",
    "precio": 199.99,
    "stock": 20,
    "activo": True,
}

producto_periferico = {
    "nombre": "Auriculares Gamer",
    "precio": 90.00,
    "stock": 0,
    "activo": False,
}

producto_led = {
    "nombre": "Tira Led RGB",
    "precio": 28.99,
    "stock": 10,
    "activo": True,
}

productos = [producto_silla, producto_escritorio, producto_periferico, producto_led]

print(productos)
print("\n")
print(producto_escritorio)
print("\n")
print(producto_silla)
print("\n")
print(producto_periferico)
print("\n")
print(producto_led)