	numero_billetes = 8
	total = numero_billetes
	billetes = [float() for ind0 in range(numero_billetes)]
	billetes[0] = 50.000
	billetes[1] = 20.000
	billetes[2] = 10.000
	billetes[3] = 5.000
	billetes[4] = 2.000
	billetes[5] = 1.000
	billetes[6] = 500
	billetes[7] = 100
	cantidad_bill_mon = [str() for ind0 in range(total)]
	indice_billetes = 0
	print("Dame una cantidad de billetes mayor a 0")
	cantidad = float(input())
	if cantidad>1:
		cantidad_entera = int(cantidad)
		cantidad_decimal = int((cantidad-cantidad_entera)*100)
		for i in range(total):
	else:
		print("La cantidad de billetes mayor a 0")
