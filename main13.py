if __name__ == '__main__':
	dia = int()
	mes = int()
	c = int()
	signo = str()
	print("Ingresa el mes de nacimiento")
	mes = int(input())
	print("Ingresa el dia de nacimiento")
	dia = int(input())
	c = 0
	if (mes==12 and (dia>=22 and dia<=31)) or (mes==1 and dia<=20):
		signo = "Capricornio"
		c = 1
	if (mes==1 and (dia>=21 and dia<=31)) or (mes==2 and dia<=19):
		signo = "Acuario"
		c = 1
	if (mes==2 and (dia>=20 and dia<=29)) or (mes==3 and dia<=20):
		signo = "Picis"
		c = 1
	if (mes==3 and (dia>=21 and dia<=31)) or (mes==4 and dia<=20):
		signo = "Aries"
		c = 1
	if (mes==4 and (dia>=21 and dia<=30)) or (mes==5 and dia<=20):
		signo = "Tauro"
		c = 1
	if (mes==5 and (dia>=1 and dia<=31)) or (mes==6 and dia<=21):
		signo = "Geminis"
		c = 1
	if (mes==6 and (dia>=22 and dia<=30)) or (mes==7 and dia<=22):
		signo = "Cancer"
		c = 1
	if (mes==7 and (dia>=23 and dia<=31)) or (mes==8 and dia<=22):
		signo = "Leo"
		c = 1
	if (mes==8 and (dia>=23 and dia<=31)) or (mes==9 and dia<=22):
		signo = "Virgo"
		c = 1
	if (mes==9 and (dia>=23 and dia<=30)) or (mes==10 and dia<=22):
		signo = "Libra"
		c = 1
	if (mes==10 and (dia>=23 and dia<=31)) or (mes==11 and dia<=22):
		signo = "Escorpion"
		c = 1
	if (mes==11 and (dia>=23 and dia<=30)) or (mes==12 and dia<=21):
		signo = "Sagitario"
		c = 1
	if c==1:
		print("Tu signo del zodiaco es: ",signo)
	else:
		print("El signo del zodiaco no existe")