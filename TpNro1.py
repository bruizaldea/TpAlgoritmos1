def menu():
    print("1-Administración")
    print("2-Entrega de cupos")
    print("3-Recepción")
    print("4-Registrar calidad")
    print("5-Registrar peso bruto")
    print("6-Registrar descargas")
    print("7-Registrar tara")
    print("8-reportes")
    print("0-Fin del programa")

menu()
opc = int(input("Bienvenidos a el menu pricnipal. Ingrese una opción o 0 para terminar"))
while opc != 0:
    while opc != 1 and opc != 2 and opc != 3 and opc != 4 and opc != 5 and opc != 6 and opc != 7 and opc != 8 and opc != 0:
        opc = int(input("Opción incorrecta elija una opción entre 1 y 8 o 0 para terminar"))

def recepcion():
    elec = str(input("Desea ingresar un camion? S o N"))
    elec.upper()
    while elec != "S" and elec != "N":
        elec = str(input("Opción incorrecta elija S o N"))
    while elec != "N":
        cantcam = cantcam + 1 
        patent = str(input("Ingrese la patente del camion"))
        prod = str(input("Ingrese el producto transportado: S (Soja) o M (Maíz)"))
        prod.upper()
        while prod != "S" and prod != "M":
            prod = str(input("Prodcuto invalido ingrese S o M"))
        if prod == "S":
