	print("Ingrese su sueldo base")
	sb = float(input())
	print("Ingrese valor de la venta 1")
	v1 = float(input())
	print("Ingrese venta 2")
	v2 = float(input())
	print("Ingrese venta 3")
	v3 = input()
	tot_ventas = v1+v2+3
	com = tot_ventas*0.10
	tpag = sb+com
	print("Su sueldo es:",sb,"Total a pagar es: ",tpag)