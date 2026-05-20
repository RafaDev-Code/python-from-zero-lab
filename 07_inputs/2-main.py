productos = []

nombre =  input("producto: ")
precio_texto = input("precio: ")
stock_texto = input("stock: ")

precio = float(precio_texto)
stock = int(stock_texto)


producto = {
    "nombre": nombre,
    "precio": precio,
    "stock": stock,
}

productos.append(producto)

nombre =  input("producto: ")
precio_texto = input("precio: ")
stock_texto = input("stock: ")

precio = float(precio_texto)
stock = int(stock_texto)


producto = {
    "nombre": nombre,
    "precio": precio,
    "stock": stock,
}

productos.append(producto)


print(productos)