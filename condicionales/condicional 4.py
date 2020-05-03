print("Programa de becas 2017")

distancia = int (input("introduce la distancia : "))
hermanos = int (input("cantidad de hermanos: "))
salario = int (input("Salario familiar anual: "))

if distancia < 40 and hermanos < 2 and salario < 20000:
    print("Derecho a beca")
else:
    print("Beca denegada")

    
