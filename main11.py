"""
Entradas
temperatura-->float-->t
salidas
deporte-->str-->d
"""
t=float(input("Digite temperatura: "))
d=""#str
if(t>85):
  d="Natacion"
elif(t>=70 and t<=85):
  d="Tenis"
elif(t>=32 and t<=70):
  d="Golf"
elif(t>=10 and t<=32):
  d="Esqui"
elif(t>=10):
  d="Marcha"
print(d)