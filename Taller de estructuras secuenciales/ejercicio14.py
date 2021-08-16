	# variables: CE,COSTO,PAGO
	ce = float()
	costo = float()
	pago = float()
	print("Ingrese el numero de consumo de energia electrica en kilowats:")
	ce = float(input())
	print("Ingrese el costo por kilowats: ")
	costo = float(input())
	pago = ce*costo
	print("total a pagar en 1 mes es: ",pago)
