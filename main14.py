if __name__ == '__main__':
	print("Ingresa el valor de consumo en kilowatts:", end="")
	consumo_en_kilowatts = float(input())
	print("Ingresa el valor de costo por kilowatt:", end="")
	costo_por_kilowatt = float(input())
	pago = consumo_en_kilowatts*costo_por_kilowatt
	print("Valor de pago: ",pago)