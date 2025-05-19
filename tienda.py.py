productos = [
    [1,"Papa", "Verdulería", 1000],
    [2,"Cebolla", "Verdulería", 3000],
    [3,"Zanahoria", "Verdulería", 2000],
    [4,"Apio", "Verdulería", 2500],
    [5,"Fideo", "Almacén", 200],
    [6,"Arroz", "Almacén", 350],
    [7,"Yerba", "Almacén", 5000],
    [8,"Azúcar", "Almacén", 2460],
    [9,"Aceite", "Almacén", 456],
    [10,"Jabón", "Art limpieza", 3280],
    [11,"Jabón líquido", "Art limpieza", 2500],
    [12,"Detergente", "Art limpieza", 1564],
    [13,"Hamburguesa", "Congelados", 2800],
    [14,"Helado", "Congelados", 4500],
    [15,"Tornillo", "Ferretería", 3700],
    [16,"Lapicera", "Bazar", 345]
]

producto_id = len(productos) + 1 
opc = ""
while opc != 6:
    print("*" * 20)
    print("       🏪  Menú de Tienda       ")
    print("*" * 20)
    print("1.🛒 Agregar un nuevo producto")
    print("2. Ver productos")
    print("3.⚒️ Actualizar producto")
    print("4.🔍 Buscar un producto")
    print("5. ❌ Eliminar producto")
    print("6. Salir del sistema")
    print("*" * 20)

    opc = input("Elija una opción (1-6): ").strip()
    while not (opc.isdigit() and 1 <= int(opc) <= 6):
        print("❌ Opción inválida, intente nuevamente.")
        opc = input("Selecciona una opción (1-6): ").strip()
    opc = int(opc)

    match opc:
        case 1:
            print("-----|Registrar un nuevo producto|-----")

            nombre = input("Ingrese el nombre del producto: ").strip().title()
            while not nombre.replace(" ", "").isalpha():
                print("❌ El nombre solo debe contener letras.")
                nombre = input("vuelva a ingresar el nombre del producto: ").strip().title()

            print("\nIngrese una categoría:")
            print("1. Verdulería\n2. Congelados\n3. Almacén\n4. Art limpieza\n5. Ferretería\n6. Bazar")

            categoria = input("Ingrese categoría (1-6): ").strip()
            while not (categoria.isdigit() and 1 <= int(categoria) <= 6):
                print("❌ Opción inválida, debe ser un número entre 1 y 6.")
                categoria = input("Ingrese categoría (1-6): ").strip()

            categoria_num = int(categoria)
            categorias = ["Verdulería", "Congelados", "Almacén", "Art limpieza", "Ferretería", "Bazar"]
            categoria_texto = categorias[categoria_num - 1]

            precio = input("Ingrese el precio del producto: ").strip()
            while not precio.isdigit():
                print("❌ El precio debe ser un número.")
                precio = input("Ingrese el precio del producto: ").strip()

            precio = int(precio)

            productos.append([producto_id, nombre, categoria_texto, precio])

            print("\n🛒 Producto cargado correctamente:")
            print(f"N° :  {producto_id}")
            print(f"Nombre: {nombre}")
            print(f"Categoría: {categoria_texto}")
            print(f"Precio: ${precio}")
             
            producto_id += 1  

        case 2:
            print("----|Lista de productos|-----")
            if not productos:
                print("❌ Producto sin cargar")
            else:
                print("\n📋 {:^50}".format("LISTADO DE PRODUCTOS"))
                print("-" * 60)
                print("{:<5} {:<25} {:<25} {:>10}".format("N°", "Producto", "Categoría", "Precio"))
                print(":" * 65)

                for prod in productos:
                    print("{:<5} {:<25} {:<25} ${:>9}".format(prod[0], prod[1], prod[2], prod[3]))  

        case 3:
            pass

        case 4:
            print("----|Búsqueda de Productos|----")
            if not productos:
                print("❌ No hay productos cargados.")
            else:
                producto_buscado = input("🔍 Ingrese el nombre del producto a buscar: ").strip().title()
                encontrados = [p for p in productos if p[1] == producto_buscado]  

                if encontrados:
                    print("📝 Productos encontrados:")
                    print("-" * 60)
                    print("{:<5} {:<25} {:<25} {:>10}".format("N°", "Producto", "Categoría", "Precio"))
                    print("-" * 60)

                    for producto in encontrados:
                        print("{:<5} {:<25} {:<25} ${:>9}".format(producto[0], producto[1], producto[2], producto[3]))  
                else:
                    print(f"❌ No se encontraron productos con el nombre: {producto_buscado}")

        case 5:
            print("======== Eliminar un producto ============")
            if not productos:
                print("❌ No hay productos cargados.")
            else:
                print("\n📋 {:^60}".format("LISTADO DE PRODUCTOS"))
                print("-" * 60)
                print("{:<3} {:<25} {:<20} {:>10}".format("N°", "Producto", "Categoría", "Precio"))
                print("-" * 60)

                for i, prod in enumerate(productos, 1):
                    print("{:<3} {:<25} {:<20} ${:>9}".format(i, prod[1], prod[2], prod[3]))

                posicion = input("Ingrese el n° del producto a eliminar: ").strip()
                while not (posicion.isdigit() and 1 <= int(posicion) <= len(productos)):
                    print("❌ Número inválido.")
                    posicion = input("Ingrese el n° del producto a eliminar: ").strip()

                eliminado = productos.pop(int(posicion) - 1)
                print(f"🗑 Producto '{eliminado[1]}' eliminado correctamente.")


        case 6:
            print("👋 GRACIAS POR USAR NUESTRO SISTEMA 🛒")

