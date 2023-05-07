from module import *
from os import system
system("cls")

while True:
    sesion = validar_user(user, pas) 
    if sesion == True:
        while True:
            welcome()
            for i in range(len(menu)):
                print(str(i+1), ". "  + menu[i])
            opcion = int(input("Elegir opción: "))
            if opcion == 1:
                inv = input("Inventario de generacion 20 ó 30: ")
                if inv == "20":
                    show_products(inventario_GPU_GEN20)
                    producto, cantidad = var()
                    inv_gen20 = inventario_GPU_GEN20
                    sell(producto, cantidad, inv_gen20)
                elif inv == "30":
                    show_products(inventario_GPU_GEN30)
                    producto, cantidad = var()
                    inv_gen30 = inventario_GPU_GEN30
                    sell(producto, cantidad, inv_gen30)
            elif opcion == 2:
                    while True:
                        agregar()
                        next = input("Agregar otro prodructo? si/no: ").lower
                        if next == "no":
                            break
            elif opcion == 3:
                while True:
                    here = input("Nombre del producto: ").upper()
                    search(here)
                    skip = input("Buscar otro prodructo? si/no: ").lower
                    if next == "no":
                        break
            elif opcion == 4:
                while True:
                    name = input("Nombre del producto: ").upper()
                    delete(name)
                    if next == "no":
                        break
            elif opcion == 5:
                while True:
                    change = input("Inventario del producto a cambiar: presionar 1 si es GEN20 // presionar 2 si es GEN30: ")
                    if change == "1":
                        print()
                        print("\tInventario de la generación 20")
                        print()
                        show_products(inventario_GPU_GEN20)
                        name = input("Escriba el nombre, precio, cantidad o codigo a cambiar (SOLO UNA OPCION): ").upper()
                        nuevo_product = input("Nuevo parametro del producto: ").upper()
                        edit(name, inventario_GPU_GEN20, nuevo_product)
                    elif change == "2":
                        print()
                        print("\t\tInventario de la generación 30")
                        print()
                        show_products(inventario_GPU_GEN30)
                        name = input("Escriba el nombre, precio, cantidad o codigo a cambiar (SOLO UNA OPCION): ").upper()
                        nuevo_product = input("Nuevo parametro del producto: ").upper()
                        edit(name, inventario_GPU_GEN30, nuevo_product)  
                    seguir = input("Cambiar otro producto? si/no: ").lower
                    if seguir == 'no':
                        break
            elif opcion == 6:
                print("Cerrando sesión...")
                exit()