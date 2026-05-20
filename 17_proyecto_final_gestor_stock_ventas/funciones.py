import csv

ARCHIVO_PRODUCTOS = "productos.csv"

def guardar_productos_csv(productos):
    with open(ARCHIVO_PRODUCTOS, "w", newline="") as archivo:
        columnas = ["nombre", "precio", "stock", "active"]
        escritor = csv.DictWriter(archivo, fieldnames=columnas)

        escritor.writeheader()

        for producto in productos:
            escritor.writerow(producto)

def cargar_productos_csv():
    productos = []

    try:
        with open(ARCHIVO_PRODUCTOS, "r") as archivo:
            lector = csv.DictReader(archivo)

            for fila in lector:
                producto = {
                    "nombre": fila["nombre"],
                    "precio": float(fila["precio"]),
                    "stock": int(fila["stock"]),
                    "active": fila["active"] == "True",
                }
                productos.append(producto)

    except FileNotFoundError:
        return productos
    
    return productos

def cargar_producto(productos):

    nombre = input("Nombre: ")

    for producto in productos:
        if producto["nombre"] == nombre:
            print("Ya existe un producto con ese nombre")
            return None
    try:    
        precio = float(input("Precio: "))
        stock = int(input("Stock: "))
    except ValueError:
        print("Precio y stock tienen que ser numeros")
        return None
    
    producto = {
        "nombre": nombre,
        "precio": precio,
        "stock": stock,
        "active": True, 
    }

    return producto


def listar_productos(productos):
    if len(productos) == 0:
        print("No hay productos cargados")
        return
    
    for producto in productos:
        print("--------------------")
        print("Nombre:", producto["nombre"])
        print("Precio:", producto["precio"])
        print("Stock:", producto["stock"])

        if producto["active"] == True:
            print("Estado: activo")
        else:
            print("Estado: desactivado")


def vender_productos(productos):
    buscar_producto = input("Nombre del producto a vender: ")
    try:
        cantidad_venta = int(input("Cantidad a vender: "))
    except ValueError:
        print("La cantidad debe ser un numero entero")
        return
    
    for producto in productos:
        if producto["nombre"] == buscar_producto:
            if producto["active"] == False:
                print("No vender. Producto desactivado.")
                return
            if producto["stock"] >= cantidad_venta:
                producto["stock"] = producto["stock"] - cantidad_venta
                total = cantidad_venta * producto["precio"]

                print("Venta Exitosa")
                print("Total ", total) 
                print("Stock restante:", producto["stock"])
                return
            else:
                print("No hay stock suficiente")
                return           
    print("No encontramos ese Producto")


def cambiar_estado(productos):
    buscar_producto = input("Nombre del producto: ")

    for producto in productos:
        if producto["nombre"] == buscar_producto:
            if producto["active"] == True:
                producto["active"] = False
                print("producto desactivado")
                return
            else:
                producto["active"] = True
                print("producto activado")
                return
    print("No encontramos ese Producto")

def borrar_producto(productos):
    buscar_producto = input("Nombre del producto a borrar: ")

    for producto in productos:
        if producto["nombre"] == buscar_producto:
            productos.remove(producto)
            print("Producto Eliminado")
            return
    print("No encontramos el producto que buscabas...")