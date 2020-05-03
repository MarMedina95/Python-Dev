
def evaluacion(nota):
    valor = "aprobado"
    if nota < 5:
        valor = "reprobado"
    return valor

print ("introduzca la calificacion del alumno")
grade = input() # todo dato que se introduzca con input() se le considera string
# int(grade) convierte el dato a entero
print(evaluacion(int(grade)))
