miLista = ["uno", "dos", "tres", "cuatro"]
#imprimir la lista completa sin un for
print(miLista[:])
print(miLista[2])
#nota: deja poner numeros negativos dentro de los corchetes, pero el conteo
# de la lista lo hace a la inversa

print(miLista[0:3]) # permite imprimir un rango de los elementos de la lista
                    # en este caso el cero viene incluido
                    # pero el 3 se excluye

#agregar un elemento a la lista, pero simepre lo inserta al final de la lista
miLista.append("cinco")
print(miLista[:])

#para insertar un dato en un lugar en especifico
miLista.insert(2,"seis")
print(miLista[:])

#sirve para concatenar una lista con otra o para agregar varios elementos a una
miLista.extend(["sandra","ana"])
print(miLista[:])

#sabes el indice de un elemento en una lista
print(miLista.index("cinco"))

#saber si un elemento esta en la lista
