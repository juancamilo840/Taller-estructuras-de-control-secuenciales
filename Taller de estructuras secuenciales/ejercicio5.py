	print("Ingrese su primera calificacion")
	calif1 = float(input())
	print("Ingrese su segunda calificacion")
	calif2 = float(input())
	print("Ingrese su tercera calificacion")
	calif3 = float(input())
	print("Ingrese su calificacion del examen final")
	examf = float(input())
	print("Ingrese la calificacion del trabajo final")
	trabf = float(input())
	promedio = (calif1+calif2+calif3)/3
	parcial = promedio*0.55
	pef = examf*0.30
	ptf = trabf*0.15
	calif = parcial+pef+pft
	print("Su calificacion final es: ",calif)