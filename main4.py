if __name__ == '__main__':
	n = int()
	costo = float()
	total = float()
	inversion = float()
	credito = float()
	interes = float()
	print("Ingrese el numero de piezas a comprar")
	n = int(input())
	print("Ingrese el costo de la pieza")
	costo = float(input())
	total = n*costo
	if total>5000000:
		inversion = total*.55
		banco = total*.30
		credito = total*.15
	else:
		inversion = total*.70
		banco = 0
		credito = total*.30
	interes = credito*.20
	print("la inversion es de: $",inversion)
	print("El prestamo del banco es de:$",banco)
	print("El credito a pagar es: $",credito)
	print("El interes por el credito es:$",interes)
