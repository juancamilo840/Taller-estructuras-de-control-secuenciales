	# /Ingresar un valor en chelines,luego mostrar su equivalente en pesetas
	# /Dato1: 100 chelines es 956.871 pesetas
	# /Ingresar un valor en dracmas,luego mostrar su equivalente en francos
	# /Dato2: 100 dracmas es 201.1 francos
	# /Ingresar un valor en pesetas,luego mostrar su equivalente en dolares
	# /Dato3: 122.499 pesetas es 1 dolares
	# /Ingresar un valor en pesetas,luego mostrar su equivalente en liras
	# /Dato4: 9.289 pesetas es 100 liras
	chelines = float()
	pesetas = float()
	dracmas = float()
	francos = float()
	dolares = float()
	liras = float()
	print("Ingrese la cantidad de chelines")
	chelines = float(input())
	print("Ingrese la cantidad de dracmas")
	dracmas = float(input())
	print("Ingrese la cantidad de pesetas")
	pesetas = float(input())
	print("Ingrese la cantidad de pesetas")
	pesetas = float(input())
	pesetas = chelines*956.871
	francos = dracmas*201.1
	dolares = pesetas*1
	liras = pesetas*100
	print("La cantidad de ",chelines,"chelines a pesetas es igual a: ",pesetas,"pesetas")
	print("La cantidad de ",dracmas,"dracmas a francos es igual a: ",francos,"francos")
	print("La cantidad de ",pesetas,"pesetas a dolares es igual a: ",dolares,"dolares")
	print("La cantidad de ",pesetas,"pesetas a liras es igual a: ",liras,"liras")