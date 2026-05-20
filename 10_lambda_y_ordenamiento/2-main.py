productos = [
    {"nombre": "silla ergo", "stock": 10, "precio": 100.80},
    {"nombre": "mause", "stock": 5, "precio": 90.99},
    {"nombre": "auriculares", "stock": 6, "precio": 60.99}
]
print(productos)
orden_precio = sorted(productos, key=lambda producto: producto["precio"])
print(orden_precio)
orden_stock = sorted(productos, key=lambda producto: producto["stock"])
print(orden_stock)
