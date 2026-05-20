from funciones import (
    cargar_producto,
    listar_productos,
    vender_productos,
    cambiar_estado,
    guardar_productos_csv,
    cargar_productos_csv,
    borrar_producto,
)

productos = cargar_productos_csv()
opcion = ""

while opcion != "0":
    print("---------------------")
    print("1 - cargar producto")
    print("2 - listar productos")
    print("3 - vender productos")
    print("4 - cambiar estado del producto")
    print("5 - borrar producto")
    print("0 - salir")
    
    opcion = input("Elige una opcion: ")

    if opcion == "1":
        producto_nuevo = cargar_producto(productos)

        if producto_nuevo != None: 
            productos.append(producto_nuevo)
            guardar_productos_csv(productos)
            print("Producto Cargado")

    elif opcion == "2":
       listar_productos(productos)
        
    elif opcion == "3":
        vender_productos(productos)
        guardar_productos_csv(productos)
    
    elif opcion == "4":
        cambiar_estado(productos)
        guardar_productos_csv(productos)

    elif opcion == "5":
        borrar_producto(productos)
        guardar_productos_csv(productos)

    elif opcion == "0":
        print("Saliendo.....")
    
    else:
        print("Opcion Incorrecta, intenta de nuevo.")