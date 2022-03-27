import base64
import os 

os.system("cls")
os.system("color a")

def menu():
	os.system('cls') 

	print()
	print(""".______      __    _  _    
|   _  \    / /   | || |   
|  |_)  |  / /_   | || |_  
|   _  <  | '_ \  |__   _| 
|  |_)  | | (_) |    | |   
|______/   \___/     |_|   
                           """)
	print()
	print()
	print(" Diseñado por Eltotiz")
	print("  github.com/Eltotiz")
	print()
	print()

	print (" [1] - Codificar")
	print()
	print (" [2] - De-Codificar")
	print()
	print (" [9] - Salir")
	print()
	print()

 

 

while True:

	

	menu()

	opcionMenu = input("Inserte el numero de una opcion >> ")

 

	if opcionMenu=="1":
		os.system("cls")
		print()
		print(""".______      __    _  _    
|   _  \    / /   | || |   
|  |_)  |  / /_   | || |_  
|   _  <  | '_ \  |__   _| 
|  |_)  | | (_) |    | |   
|______/   \___/     |_|   
                           """)
		print()
		print()
		print(" Diseñado por Eltotiz")
		print("  github.com/Eltotiz")
		print()
		print()
		mensaje = input("Inserte texto que quiera ser codificado a b64 >> ")
		print()
		print()
		message_bytes = mensaje.encode('ascii')
		base64_bytes = base64.b64encode(message_bytes)
		base64_message = base64_bytes.decode('ascii')
		print(base64_message)
		print()
		print()
		input("Pulsa enter para volver al menu.")

	elif opcionMenu=="2":
		print ("")
		os.system("cls")
		print()
		print(""".______      __    _  _    
|   _  \    / /   | || |   
|  |_)  |  / /_   | || |_  
|   _  <  | '_ \  |__   _| 
|  |_)  | | (_) |    | |   
|______/   \___/     |_|   
                           """)
		print()
		print()
		print(" Diseñado por Eltotiz")
		print("  github.com/Eltotiz")
		print()
		print()

		mensaje2 = input("Inserte el texto que quiere ser de-codificado de b64 >> ")
		print()
		print()
		base64_bytes = mensaje2.encode('ascii')
		message_bytes = base64.b64decode(base64_bytes)
		message = message_bytes.decode('ascii')
		print(message)
		print()
		print()
		input("Pulsa enter para volver al menu.")
	elif opcionMenu=="9":
		print()
		print()
		print("Gracias por usar nuestro script! :)")
		break

	else:

		print ("")

		input("No has pulsado ninguna opción correcta. Preciona enter para volver.")
