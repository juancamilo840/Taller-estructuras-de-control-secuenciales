if __name__ == '__main__':
	print("Ingresa el valor de monto de la compra:", end="")
	monto_de_la_compra = float(input())
	descuento = 0
	if monto_de_la_compra>50000 and monto_de_la_compra<=100000:
		descuento = monto_de_la_compra*0.05
	if monto_de_la_compra>100000 and monto_de_la_compra<=700000:
		descuento = monto_de_la_compra*0.11
	if monto_de_la_compra>700000 and monto_de_la_compra<=1500000:
		descuento = monto_de_la_compra*0.18
	if monto_de_la_compra>1500000:
		descuento = monto_de_la_compra*0.25
	print("Valor de descuento: ",descuento)
	print("")