if __name__ == '__main__':
	print("Ingresa el valor de cantidad en pesos:", end="")
	cantidad_de_pesos = input()
	monedas_de_1 = cantidad_de_pesos
	billetes_de_100000 = (monedas_de_1-monedas_de_1%500)/500
	monedas_de_1 = monedas_de_1%500
	billetes_de_50000 = (monedas_de_1-monedas_de_1%200)/200
	monedas_de_1 = monedas_de_1%200
	billetes_de_20000 = (monedas_de_1-monedas_de_1%100)/100
	monedas_de_1 = monedas_de_1%100
	billetes_de_10000 = (monedas_de_1-monedas_de_1%50)/50
	monedas_de_1 = monedas_de_1%50
	billetes_de_5000 = (monedas_de_1-monedas_de_1%20)/20
	monedas_de_1 = monedas_de_1%20
	billetes_de_2000 = (monedas_de_1-monedas_de_1%10)/10
	monedas_de_1 = monedas_de_1%10
	billetes_de_1000 = (monedas_de_1-monedas_de_1%5)/5
	monedas_de_1 = monedas_de_1%5
	monedas_de_2 = (monedas_de_1-monedas_de_1%2)/2
	monedas_de_1 = monedas_de_1%2
	print("Valor de billetes de 100000: ",billetes_de_100000)
	print("Valor de billetes de 50000: ",billetes_de_50000)
	print("Valor de billetes de 20000: ",billetes_de_20000)
	print("Valor de billetes de 10000: ",billetes_de_10000)
	print("Valor de billetes de 5000: ",billetes_de_5000)
	print("Valor de billetes de 2000: ",billetes_de_2000)
	print("Valor de billetes de 1000: ",billetes_de_1000)
	print("Valor de monedas de 1: ",monedas_de_1)
	print("Valor de monedas de 2: ",monedas_de_2)
