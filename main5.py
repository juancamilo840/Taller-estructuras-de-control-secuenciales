if __name__ == '__main__':
	sueldo = 1500
	print("Ventas en Bs. realizadas por departamento 1:")
	vdep1 = input()
	print("Ventas en Bs. realizadas por departamento 2:")
	vdep2 = input()
	print("Ventas en Bs. realizadas por departamento 3:")
	vdep3 = input()
	vt = vdep1+vdep2+vdep3
	p33 = vt*33/100
	if (vdep1>p33):
		sdep1 = sueldo+sueldo*20/100
	else:
		sdep1 = sueldo
	if (vdep2>p33):
		sdep2 = sueldo+sueldo*20/100
	else:
		sdep2 = sueldo
	if (vdep3>p33):
		sdep3 = sueldo+sueldo*20/100
	else:
		sdep3 = sueldo
	print("Los vendedores del dep 1 recibiran un pago de :",sdep1," Bs.")
	print("Los vendedores del dep 2 recibiran un pago de :",sdep2," Bs.")
	print("Los vendedores del dep 3 recibiran un pago de :",sdep3," Bs.")
