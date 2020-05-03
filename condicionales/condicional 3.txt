edad = 7

if 0 <edad < 100:
    print("edad correcta")
else:
    print("edad incorrecta")


salario_presidente = int(input("introduce salario presi: "))
salario_director = int(input("introduce salario Director: "))
salario_gerente = int(input("introduce salario Gerente: "))
salario_coordinador = int(input("introduce salario Coordinador: "))
#concatenacion de los simbolos 
if salario_coordinador < salario_gerente < salario_director < salario_presidente:
    print("todo funciona bien")
else :
    print ("Algo fallo con los sueldos")

