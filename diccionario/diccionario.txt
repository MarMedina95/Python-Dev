#DICCIONARIOS
#parecido a las listas y las tuplas
#se crea asociacion a clave:valor, es decir, que a cada valor que se almacena
#      en un diccionario se le asigna una clave unica
#se pueden almacenar todo tipo de datos
# no importa el orden debido a que tienen una clave unica

miDiccionario = {"alemania":"berlin", "francia":"paris", "UK":"londres", "españa":"Madrid"}

#acceder a un elemento o valor del diccionario
print(miDiccionario["francia"])
#ver todo el diccionario
print(miDiccionario)

#agregar un elemento al diccionario
miDiccionario["Italia"] = "Mexico"
print(miDiccionario)

#en un diccionario no puede haber dos claves iguales

#eliminar un valor
del miDiccionario["alemania"]
print(miDiccionario)

 #juntar una lista con un diccionario

miLista = ["españa","francia","UK","alemania"]
miDic = {miLista[0]:"madrid", miLista[1]:"paris",miLista[2]:"londres",miLista[3]:"berlin"}
print(miDic)

#guardar una lista en un diccionario
miDic2 = {23:"jordan", "nombre":"michael","equipo":"chicago","anillos":[1992,1995,1997,1994]}
print(miDic2["anillos"])

#agregar un diccionario dentro de otro
miDic3 = {23:"jordan", "nombre":"michael","equipo":"chicago","anillos":{"temporadas":[1992,1995,1997,1994]}}
print(miDic3["anillos"])
print("-----------------------------------------------------------------------------------------")
print("-----------------------------------------------------------------------------------------")

#metodo key
print(miDic3.keys())
#metodo value
print(miDic3.values())
#metodo lenght
print(len(miDic3))
print(miDic3)

