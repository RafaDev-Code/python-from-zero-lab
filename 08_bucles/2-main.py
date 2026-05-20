print ("Hola! Para cargar productos, te voy a pedir: ")

productos = []

opcion = ""

while opcion != "salir":

    print("1 - añadir producto")
    print("salir - salir")
    opcion = input("opcion: ")

    if opcion == "1":

        nombre = input("nombre del producto: ")
        stock_text = input("stock del producto: ")
        stock = int(stock_text)

        producto = {
            "nombre": nombre,
            "stock": stock,
        }

        productos.append(producto)

        for producto in productos: 
            print (producto["nombre"])
            print (producto["stock"])

    elif opcion == "salir":
        print("saliendo....")
    else:
        print("opcion no valida")
