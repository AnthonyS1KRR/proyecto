
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


change = input("Inventario del producto a cambiar: presionar 1 si es GEN20 // presionar 2 si es GEN30: ")
if change == "1":
    print("\tInventario de la generación 20")
    show_products(inventario_GPU_GEN20)
    while True:
        name = input("Escriba el nombre, precio, cantidad o codigo a cambiar (SOLO UNA OPCION): ").upper()
        new_producto = input("Nombre del nuevo producto: ").upper()
        for i in inventario_GPU_GEN20:
            if name in list(map(str, (inventario_GPU_GEN20[i]))):
                lista_str = list(map(str, (inventario_GPU_GEN20[i])))
                pos = lista_str.index(name)
                inventario_GPU_GEN20[i].pop(pos)
                inventario_GPU_GEN20[i].insert(pos, new_producto)
                show_products(inventario_GPU_GEN20)
                break
            else:
                print("El producto no se encuentra en el inventario")
                break

#elif change == "2":
 #   print("\tInventario de la generación 30")
  #  show_products( inventario_GPU_GEN30)
   # name = input("Nombre del producto: ")
    #edit(name, inventario_GPU_GEN20)


#for i in inventario_GPU_GEN20:
 #       for j in inventario_GPU_GEN20[i]:
  #          if name in j:
   #             print("hola")
