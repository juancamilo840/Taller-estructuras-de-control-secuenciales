if __name__ == '__main__':
	print("[Resolución de ecuación cuadrática ax2 + bx + c = 0]")
	print("Introduzca los valores de parámetros")
	a = input()
	b = input()
	c = input()
  d = b ^ 2 - 4 * a * c : e = 2 * a
	if d==0:
		print("x1 = x2 =",-b/e)
	else:
		if d>0:
			print("x1 =",(-b+(d))/e)
			print("x2 =",(-b-(d))/e)
		else:
			print("x1 =",-b/e,"+",(-d)/e,"i")
			print("x2 =",-b/e,"-",(-d)/e,"i")
