#Menu de opciones
def menu():
    while (opc <= 8 and opc >= 0):
        print("MENU PRINCIPAL")
        print("1- ADMINISTRACIONES")
        print("2- ENTREGAS DE CUPOS")
        print("3- RECEPCION")
        print("4- REGISTRAR CALIDAD")
        print("5- REGISTRAR PESO BRUTO")
        print("6- REGISTRAR DESCARGA")
        print("7- REGISTRAR TARA")
        print("8- REPORTES")
        print("0- FIN DEL PROGRAMA")
        print()

        opc = int(input("Seleccione una opción: "))
       
        while (opc < 0 or opc > 8):	
        	print("")
        	print("Opcion incorrecta")
        	opc = int(input("Seleccione una opción: "))

        if (opc == 1):
            administracion()
        
        elif (opc == 2):
            entregadecupos()
        
        elif (opc == 3):
            recepcion()
        
        elif (opc == 4):
            registrarcalidad()
        
        elif (opc == 5):
            registrarpesobruto()

        elif (opc == 6):
            registrardescarga()

        elif (opc == 7):
            registrartara()

        elif (opc == 8):
            reportes()
        
        else:
            exit() #break

def administracion():
    print ("ADMINISTRACION")

def menuadmin():
	while (opc != 'A' and opc != 'B' and opc != 'C' and opc != 'D' and opc != 'E' and opc != 'F' and opc != 'V'):
        #print("MENU ADMINISTRACIONES")
        print("A- TITULARES")
        print("B- PRODUCTOS")
        print("C- RUBROS")
        print("D- RUBROS x PRODUCTO")
        print("E- SILOS")
        print("F- SUCURSALES")
        print("G- PRODUCTO POR TITULAR")
        print("V- VOLVER Al MENU PRINCIPAL")
        print()

        opc = int(input("Seleccione una opción: "))
   

        if (opc == 'A'):  
        
        elif (opc == 'B'):
            
        elif (opc == 'C'):
            
        elif (opc == 'D'):

        elif (opc == 'E'):

        elif (opc == 'F'):
    

        else (opc == 'V'):
            menu()

     	"""
		A- TITULARES
		B- PRODUCTOS
		C- RUBROS
		D- RUBROS x PRODUCTO
		E- SILOS
		F- SUCURSALES
		G- PRODUCTO POR TITULAR
		V- VOLVER al MENU PRINCIPAL

     	"""
def menuadmin2():


def entregadecupos():
    print ("En proceso")

def recepcion():
    print ("En proceso")

def registrarcalidad():
    print ("En proceso")

def registrarpesobruto():
    print ("En proceso")

def registrardescarga():
    print ("En proceso")

def registrartara():
    print ("En proceso")

def reportes():
    print ("En proceso")
    
menu()