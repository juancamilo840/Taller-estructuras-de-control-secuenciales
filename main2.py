if __name__ == '__main__':
	print("ingrese su sueldo")
	sueldo = float(input())
	if sueldo<=900_000:
		aumento = sueldo*0.1
		print("el 15% es :",aumento)
		sueldo = sueldo+aumento
		print("el sueldo es:",sueldo)