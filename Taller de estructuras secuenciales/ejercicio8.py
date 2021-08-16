	# En funcion de las longitudes de sus lados
	# Entradas L1, L2, L3: Enteros:longitudes de los lados del triangulo
	# Salidas El Area del triangulo definido por L1,L2,L3
	# variable SP:Real
	print("Introduzca la Longitud de lado 1 del triangulo:")
	l1 = float(input())
	print("Introduzca la longitud de lado 2 del triangulo:")
	l2 = float(input())
	print("Introduzca la Longitud de lado 3 del triangulo:")
	l3 = float(input())
	sp = (l1+l2+l3)/2
	area = sqrt(sp*(sp-l1)*(sp-l2)*(sp-l3))
	print("El area del triangulo es: ",area)