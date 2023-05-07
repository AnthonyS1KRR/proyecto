import random

inventario_GPU_GEN30 = {
    "GPU_list" : ["RTX 3090 TI", "RTX 3090", "RTX 3080 TI", "RTX 3080", "RTX 3070 TI", "RTX 3070", "RTX 3060 TI", "RTX 3060", "RTX 3050"],
    "Price" : [ 1999, 1499, 1199, 699, 599, 499, 399, 329, 239 ],
    "Code" : [ 6950, 6900, 6850, 6800, 6750, 6700, 6650, 6600, 6500 ],
    "Stock" : [random.randint(0, 100) for i in range(9)] 
} 
inventario_GPU_GEN20 = {
    "GPU_list" : ["RTX TITAN", "RTX 2080 TI", "RTX 2080 super", "RTX 2080", "RTX 2070 SUPER", "RTX 2070", "RTX 2060 SUPER", "RTX 2060"],
    "Price" : [ 2499, 999, 699, 699, 499, 499, 399, 349],
    "Code" : [ 5900, 5850, 5800, 5750, 5700, 5650, 5600, 5500 ],
    "Stock" : [random.randint(0, 100) for i in range(8)]
} 

ventas = []
factura = []
total_precio = []

menu = [ 'Abrir menú de ventas', 'Agregar nuevo productos','Buscar un producto','Eliminar un producto', 'Cambiar algún producto', 'Cerrar sesión']

user = "MASTER"
pas = "123"

def validar_user(User, Pass):
    usuario = input("Ingresar usuario: 'master' ").upper()
    if usuario == User:
        contraseña = input("Ingresar contraseña: '123'  ").upper()
        if contraseña == Pass:
            termino1 = 675
            termino2 = (50 * 6 + 21)
            while True:
                try:
                    captcha = int(input( str(termino1) + " + " + str(termino2) + " = '998' " ))
                    break
                except ValueError:
                    print("Error")
                    exit()
            if captcha == (termino1 + termino2) + 2:
                print("Sesión iniciada")
                return True
            else:
                print("Error")
                return False
        else:
            print("Error")
            return False
    else:
        print("Error")
    return False

def sell(product, cant, inventario):
    if product in inventario["GPU_list"]:
        posi_name = inventario["GPU_list"]
        stock = inventario["Stock"]
        price = inventario["Price"]
        code = inventario["Code"]
    posicion_producto = posi_name.index(product)
    valor_cantiddad = stock[posicion_producto]
    valor_precio = price[posicion_producto]
    if  cant > valor_cantiddad:
        print("No hay la cantidad suficiente de productos")
    elif posicion_producto == posi_name.index(product):
        ventas.append(cant)
        stock.pop(posicion_producto)
        stock.insert(posicion_producto,(valor_cantiddad-cant))
        total_precio.append(cant*valor_precio)
        factura.append([" // Producto --> " + str(product)])
        factura.append([" // Precio --> " + str(price[posicion_producto])])
        factura.append([" // Cantidad --> " + str(cant)]) 
        factura.append([" // Código --> " + str(code[posicion_producto])])
        factura.append([" // El total es --> " + str(price[posicion_producto]*cant)])
        show_facture = input("Mostrar factura? si/no: ").lower()
        if show_facture == "si":
            print("-- factura -- " )
            for i in range(len(factura)):
                print(str(*factura[i]))
                print()
        else:
            pass
    return inventario, ventas, total_precio

def var():
    producto = input("Digite el nombre del producto: ").upper()
    cantidad = int(input("Cantidad de productos: "))
    return producto, cantidad

def show_products(inventario):
    for i in range(len(inventario["GPU_list"])):
            print(
                str(1+i) + ". ", 
                "Nombre =", inventario["GPU_list"][i], 
                "--- Precio = " + str(inventario["Price"][i]), 
                "--- Cantidad = " + str(inventario["Stock"][i]), 
                "--- Código del producto = " + str(inventario["Code"][i])
            )
    return

def welcome():
    print("\t"*2,"*"*79)
    print("\t"*2, "Bienvenido al programa para controlar inventario de la tienda 'PC Master Race'")
    print("\t"*2,"*"*79)
    print()
    print("***Programa especializado en la gestión de Unidades de Procesamiento Gráfico***")
    print()

def agregar():
    while True:
        nuevo = input("Agregue el nuevo producto: ").upper()
        if nuevo in inventario_GPU_GEN20["GPU_list"] or nuevo in inventario_GPU_GEN30["GPU_list"]:
            print("El producto ya está en el inventario")
            break
        try:    
            stay = int(input("En que inventario desea agregar? 20 ó 30: "))
        except ValueError:
            print("Debe ser el valor de 20 ó 30")
            break
        if stay != 20 and stay != 30:
            print("No se eligio ni 20 ni 30")
            break
        elif stay == 20:
            list_gpu = inventario_GPU_GEN20["GPU_list"]
            list_gpu.append(nuevo)
            nuevo1 = int(input("Cantidad del producto: "))
            list_stock = inventario_GPU_GEN20["Stock"]
            list_stock.append(nuevo1)
            nuevo3 = int(input("Código del producto: "))
            list_code = inventario_GPU_GEN20["Code"]
            list_code.append(nuevo3)
            nuevo4 = int(input("Precio del producto: "))
            list_price = inventario_GPU_GEN20["Price"]
            list_price.append(nuevo4)
            break
        elif stay == 30:
            list_gpu = inventario_GPU_GEN30["GPU_list"]
            list_gpu.append(nuevo)
            nuevo1 = int(input("Cantidad del producto: "))
            list_stock = inventario_GPU_GEN30["Stock"]
            list_stock.append(nuevo1)
            nuevo3 = int(input("Código del producto: "))
            list_code = inventario_GPU_GEN30["Code"]
            list_code.append(nuevo3)
            nuevo4 = int(input("Precio del producto: "))
            list_price = inventario_GPU_GEN30["Price"]
            list_price.append(nuevo4)
            break
    return 

def search(product):
    for j in inventario_GPU_GEN20.values():
        if product in j:  
            print()
            print("El prodructo se encuetra en el inventario GEN20")
            print()
            break    
        else: 
            print()
            print("El producto no se encuentra en el inventario GEN20 ")
            print()
            break
    for i in inventario_GPU_GEN30.values():
        if product in i:
            print()
            print("El prodructo se encuetra en el inventario GEN30")
            print()
            break    
        else: 
            print()
            print("El producto no se encuentra en el inventario GEN30")
            print()
            break
    return

def delete(producto):
    for things in range(len(inventario_GPU_GEN20())):
        print(things)
        for i in inventario_GPU_GEN20.values():
            if producto in i:
                posicion = inventario_GPU_GEN20["GPU_list"].index(producto)
                print(posicion)
                inventario_GPU_GEN20[things].pop(posicion)
                print(f"Se elimonó {producto} del inventario")
                print(inventario_GPU_GEN20)
                break
        for j in inventario_GPU_GEN30.values():
            if producto in j:
                inventario_GPU_GEN20["GPU_list"].remove(producto)
                print(f"Se elimonó {producto} del inventario")
                break
    return print(inventario_GPU_GEN20)

def edit(nombre, inventario, new_producto):
    for i in inventario:
        if nombre in list(map(str, (inventario[i]))):
            lista_str = list(map(str, (inventario[i])))
            pos = lista_str.index(nombre)
            inventario[i].pop(pos)
            inventario[i].insert(pos, new_producto)
            show_products(inventario)
            break
    return inventario

if __name__ == "__main__":
    show_products
    welcome
    validar_user
    sell
    var
    search
    agregar
    delete
    edit