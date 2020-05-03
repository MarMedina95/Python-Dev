#tuplas
#son listas que no se pueden modificar, inmutables
#se puede extraer info de ella, pero es una tupla nueva
#no tiene index
# se diferencias de las listas porque su sintaxis va con parentesis no corchetes

miTupla = ("mar", "hola","sol",3)
#me dice el elemento en esa posicion de la tupla
print(miTupla[2])
print(miTupla)

#convertir una tupla en una lista
milista=list(miTupla)
print(milista)

#convertir una lista en tupla
miLista2 = ["mar1", "hola1","sol1",4]
miTupla2 =tuple(miLista2)
print(miTupla2)

#nos indica que un elemento pertenece a la tupla
print ("mar1" in miTupla2)

#cuantos elementos hay en la tupla de acuerdo al que andamos buscando
print(miTupla2.count(4))

#saber la longitud de la tupla, cuantos elementos hay
print(len(miTupla2))

#tupla unitaria
tuplaUnitaria = ("mar",) #la coma es forzosa
print(len(tuplaUnitaria))

#desenpaquetado de tuplas
miTup = ("Marian",24,2,1995)
nombre,dia,mes,year = miTup #acomoda los datos en orden en las variables

print(nombre)
print(dia)
print(mes)
print(year)
