if __name__ == '__main__':
	km = float()
	total = float()
	iva = float()
	print("Digite km recorridos")
	km = float(input())
	if km<=300:
		total = 50000
	else:
		if km>300 and km<=1000:
			total = 50000+(km-300)*70000
		else:
			total = 50000+(km-300)*150000
	print("El monto a pagar es de ",total)