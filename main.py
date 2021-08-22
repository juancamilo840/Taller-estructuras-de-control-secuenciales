if __name__ == '__main__':
	print("Escribe la cantidad invertida")
	cantidad = float(input())
	print("Escribe la tasa de interes")
	tasa = float(input())
	intereses = cantidad*tasa
	if intereses>100000:
		print("Los intereses ganados son $",intereses," superan los $100000")
	else:
		print("Los intereses ganados son $",intereses," no superan los $10000")
	print("El sado total en la cuenta es: ",cantidad+intereses)