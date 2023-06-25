import numpy as np

datos_cliente = []

def menu():
    print("-----Inmobiliaria IMMO-----")
    print("1) Registrar")
    print("2) Buscar")
    print("3) Reporte")
    print("4) Salir.")
    print("---------------------------")

def registrar():
    try:
        rut = input("Ingrese rut: ")
        if len(rut) <8 or len(rut)>9:
            print("El rut debe tener entre 8 y 9 números.")
            return
        nombre = input("Ingrese el nombre: ")
        proyecto = int(input("Ingrese su proyecto:\n1) Vive Santiago\n2) Vive la Florida\n3) Vive Ñuñoa\n"))
        if proyecto == 1:
            proyecto = "VS"
        elif proyecto == 2:
            proyecto = "VF"
        elif proyecto == 3:
            proyecto = "VÑ"
        else:
            print("Opción no está en el menú.")
            return
        renta = int(input("Ingrese su renta: "))
        cliente = {"Rut": rut, "Nombre": nombre, "Proyecto": proyecto, "Renta": renta}
        datos_cliente.append(cliente)
        print("Cliente registrado.")
    except ValueError:
        print("Datos erróneos.")

def buscar():
    buscar_rut = int(input("Ingrese el rut para buscar al cliente: "))
    for cliente in datos_cliente:
        if cliente['Rut'] == buscar_rut:
            print(f"Rut: {cliente['Rut']}")
            print(f"Nombre: {cliente['Nombre']}")
            print(f"Proyecto: {cliente['Proyecto']}")
            print(f"Renta: {cliente['Renta']}")
            return
    print("Cliente no encontrado.")

cantidad_reportes = 0

def reporte():
    global cantidad_reportes
    try:
        buscar_cliente = int(input("Ingrese el rut: "))
        for cliente in datos_cliente:
            if cliente['Rut'] == buscar_cliente:
                print("Reporte IMMO Ltda.")
                print(f"Sr/a: {cliente['Nombre']}")
                print(f"Rut: {cliente['Rut']}")
                print(f"Con su renta de: {cliente['Renta']}")
                print(f"En el proyecto de: {cliente['Proyecto']}")
                dpto = np.random.randint(2500, 3700)
                print(f"Puede acceder a un Dpto de UF: {dpto}")
                cantidad_reportes += 1
                print(f"Cantidad de reportes generados: {cantidad_reportes}")
                return
        print("Rut no encontrado.")
    except ValueError:
        print("No hay reportes registrados.")

while True:
    try:
        menu()
        opcion = int(input("Ingrese una opción: "))
        if opcion == 1:
            registrar()
        elif opcion == 2:
            buscar()
        elif opcion == 3:
            reporte()
        elif opcion == 4:
            print("Saliendo del Programa...")
            break
    except ValueError:
        print("Ingrese una opción válida")
