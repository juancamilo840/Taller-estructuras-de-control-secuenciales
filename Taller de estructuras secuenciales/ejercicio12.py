	print("Ingrese la nota del examen de matematicas")
	em = float(input())
	print("Ingrese las tres calificaciones de matematicas")
	nm1 = float(input())
	nm2 = float(input())
	nm3 = float(input())
	print("Ingrese la nota del examen de fisica")
	ef = float(input())
	print("Ingrese las dos calificaciones de fisica")
	nf1 = float(input())
	nf2 = float(input())
	nf3 = input()
	print("Ingrese la nota del examen de quimica")
	eq = float(input())
	print("Ingrese las tres calificaciones de quimica")
	nq1 = float(input())
	nq2 = float(input())
	nq3 = float(input())
	pem = em*0.90
	pnm = (nm1+nm2+nm3)/3*0.10
	pm = pem+pnm
	pef = ef*0.80
	pnf = (nf1+nf2)/2*0.20
	pf = pef+pnf
	peq = eq*0.85
	pnq = (nq1+nq2+nq3)/3*0.15
	pq = peq+pnq
	print("La nota de matematicas: ",pm)
	print("La nota de fisica: ",pf)
	print("La nota de quimica: ",pq)