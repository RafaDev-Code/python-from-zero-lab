stock_productos = {
    "martillo": 1,
    "mesa": 5,
    "silla": 10,
    "manguera": 15,
}

for producto, cantidad in stock_productos.items():
    print(producto, "#" * cantidad)