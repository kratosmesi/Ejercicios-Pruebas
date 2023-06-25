import numpy as np

#este me quedo de pana siu

datos_clientes = []
reportes = 0

def grabar():
    rut = input("Ingrese rut del cliente:\n")
    if len(rut) < 8 or len(rut) >9:
        print("La longitud del rut debe tener entre 8 y 9 dígitos.")
        return
    nombre = input("Ingrese nombre del cliente:\n")
    print("Proyectos de departamento:")
    print("1) Vive Santiago.")
    print("2) Vive La Florida.")
    print("3) Vive Ñuñoa.")
    proyecto = int(input("Ingrese una de las opciones del proyecto:\n"))
    try:
        if proyecto == 1:
            proyecto = "VS"
        elif proyecto == 2:
            proyecto = "VF"
        elif proyecto == 3:
            proyecto = "VS"
        else:
            print("Opción no válida.")
    except ValueError:
        print("Ingrese un número de los que se muestra.")
    try:
        renta = int(input("Ingrese su renta:\n"))
    except ValueError:
        print("Solo valores númericos.")
    cliente = {"Rut": rut,
               "Nombre": nombre,
               "Proyecto": proyecto,
               "Renta": renta}
    datos_clientes.append(cliente)
    print("Cliente registrado con éxito!")
    
def buscar():
    if len(datos_clientes) == 0:
        print("No hay clientes registrados.")
        return
    
    buscar_rut = input("Ingrese rut del cliente: ")
    for persona in datos_clientes:
        if persona['Rut'] == buscar_rut:
            print(f"Rut: {persona['Rut']}")
            print(f"Nombre: {persona['Nombre']}")
            print(f"Proyecto escogido: {persona['Proyecto']}")
            print(f"Renta: {persona['Renta']}")

def reporte_segun_renta(reportes):
    if len(datos_clientes) == 0:
        print("No hay clientes registrados.")
        return
    
    for cliente in datos_clientes:
        if cliente['Renta'] >= 900000:
            departamento = np.random.randint(2500, 3700)
            print("-----------Reporte Immo LTDA-----------")
            print(f"Sr/a de nombre: {cliente['Nombre']}")
            print(f"Rut: {cliente['Rut']}\n")
            print(f"Su renta mensual de: {cliente['Renta']}")
            print(f"Con el proyecto elegido: {cliente['Proyecto']}\n")
            print(f"Puede acceder a un departamento de cantidad UF: {departamento}\n")
            reportes += 1
            print(f"Reportes generados: {reportes}")
            print("----------------------------------------")
            
def menu():
    print("------IMMO Ltda.------")
    print("[1] Registrar clientes.")
    print("[2] Buscar por rut.")
    print("[3] Reportes.")
    print("[4] Salir del programa.")
    
while True:
    try:
        menu()
        op = int(input("Ingrese una opción: "))
        if op == 1:
            grabar()
        elif op == 2:
            buscar()
        elif op == 3:
            reporte_segun_renta(reportes)
        elif op == 4:
            print("Saliste del programa.")
            break
        else:
            print("Opcion no válida.")
    except ValueError:
        print("Ingrese un número de las siguientes opciones.")