	nom = str()
	pm = float()
	ht = float()
	isr = float()
	sb = float()
	st = float()
	print("Ingrese el nombre del trabajador ")
	nom = input()
	print("Ingrese la cantidad de horas trabajadas")
	ht = float(input())
	print("Ingrese el precio por hora")
	ph = float(input())
	sb = ht+ph
	isr = sb*0.20
	st = sb-isr
	print("Datos para el empleado: ",nom)
	print("El sueldo bruto es: ",sb)
	print("EL descuento de impuesto es: ",isr)
	print("EL salario a pagar es: ",st)