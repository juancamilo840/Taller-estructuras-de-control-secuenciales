if __name__ == '__main__':
	nivel = float()
	edad = int()
	anemia = str()
	print("Ingresa el nivel de hemoglobina")
	nivel = float(input())
	print("Ingresa la edad")
	edad = int(input())
	anemia = "Negativo"
	if edad<=1 and nivel<13:
		anemia = "Positivo"
	if edad>1 and edad<=6 and nivel<10:
		anemia = "Positivo"
	if edad>6 and edad<=12 and nivel<11:
		anemia = "Positivo"
	if edad>12 and edad<=60 and nivel<11.5:
		anemia = "Positivo"
	if edad>60 and edad<=120 and nivel<12.6:
		anemia = "Positivo"
	if edad>120 and edad<=180 and nivel<13:
		anemia = "Positivo"
	if edad>180:
		print("Ingresa el sexo: 1 = Mujer, 2 = Hombre")
		sexo = input()
	if sexo==1 or sexo==2:
		if nivel<12: