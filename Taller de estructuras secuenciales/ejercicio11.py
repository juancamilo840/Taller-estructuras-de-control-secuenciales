	c = int()
	t = int()
	he = int()
	txhe = float()
	sb = float()
	pf = float()
	ph = float()
	ca = float()
	sn = float()
	desc = float()
	cxhe = float()
	print("Ingrese la cantidad de horas")
	c = int(input())
	print("Ingrese la tarifa")
	t = int(input())
	if c>40:
		he = c-40
		txhe = t*0.25
		cxhe = he*txhe
		sb = (c*t)+cxhe
		print("Horas Extras: $",cxhe)
	else:
		sb = c*t
	if sb<603.000:
		desc = pf*0.05
		desc = ph*0.02
		desc = ca*0.07
		sn = pf-ph-ca-desc
		print("Descuento: $",desc)
	else:
		if sb>603.000 and sb<603.000:
			sn = sb-desc
			print("Descuento: $",desc)
		else:
			sn = sb-desc
			print("Descuento: $",desc)
	print("Su sueldo neto es: $",sn)