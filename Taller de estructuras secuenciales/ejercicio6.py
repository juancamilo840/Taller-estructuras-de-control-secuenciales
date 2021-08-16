	print("Ingrese el numero de hombres")
	nmh = float(input())
	print("Ingrese el numero de mujeres")
	nmm = float(input())
	total_alumnos = nmh+nmm
	ph = nmh*100/total_alumnos
	pm = nmm*100/total_alumnos
	print("El porcentaje de hombres es:",ph,"El porcentaje de mujeres es: ",pm)