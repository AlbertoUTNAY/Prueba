print("Example 2")

print("Datos numericos")
'''
a = 5   # Int
b = 5.3 # Float
c = 5 + 2j #Complex

print(a, b, c)

print(type(a))
print(type(b))
print(type(c))

print("Datos tipo secuencias")
string_1 = "Casa"
string_2 ='Auto'
string_3 = '''
#Linea 1
#Linea 2
'''
string_4="Hola mundo           3"

print(string_1, string_1.upper())
print(string_2, string_1.lower())
print(string_4, string_4.strip(),string_1) # elimina espacios antes y despues de la cadena
print(string_4, string_4.split()) # elimina espacios antes y despues de la cadena
print(string_2)
print(string_3)

print(string_1 + string_2) #Concatena
string_5=string_1 + " " + string_2
print(string_5) #Concatena


name = "Alberto"
age = 50
string_6="Hola {}, tienes {} años".format(name,age)
string_7=f"Hola {name}, tienes {age} años"
print(string_6)

string_9 = "Hola a \ntodos"
print(string_9)

print("Datos tipo sequencias_ Listas")

list1 = [5, 8, 9, 8, 10, 8]
print(list1)

list1[3] = 55
print(list1)

list2 = [True, "Auto", 3.5, 5, 8, 10, 9, 2, 10]
print(list2)

print(len(list1)) #numero de elementos
print(len(list2))

print(list2.index(10))# posicion del elemento, contando desde el 0
list1.sort() # Ordena la lista en orden ascendente
print(list1)
list1.pop(0) # Elimina el elemento de la posicion pop(0)
print(list1)

list1.pop(list1.index(8))
print(list1)

list1.reverse() # ordena en forma descendente
print(list1)

list1.append(8) # Agrega un elemento (8) a list1 en la ultima posicion
print(list1)

list1.insert(3, "Auto") #INserta un elemento en la poscicion deseada
print(list1)

print(list1.count(9))
print(list2.count(10))

list1.remove("Auto") #Elimina toda las variables ("Auto")
print(list1)

del list1[0]
print(list1)

'''

print("Tuplas")
tupla1 = (20, 80, 60)
print(tupla1,type(tupla1))

tupla2=("Car", 3.5, 8)#no se pueden camnbiar los elementos con instruccion, por se inmutable
print(tupla2[0])
 

print("Datos Mapping")
dict1 ={"a1":10, "b":3.5, "key3":5, "a":0}
print(dict1)
print(dict1["b"])
print(len(dict1))

del dict1["a"]
print(dict1)

dict1["key3"]="Hoja"
print(dict1)

print(dict1.keys())
print(type(dict1.keys()))


list_2 = list(dict1.keys())
print(list_2)
print(type(list_2))

set_1={8, 9, 10 ,11}
set_2 = frozenset({9, 20, 17})
print(set_1,type(set_1))

set_1.add(15)
print(set_1,type(set_1))

#set_2.add(15)          no se pueden agregar elementos con el FROZENSEN
#print(set_2,type(set_2))


print("Tipos Booleano")
a = True
b=False
print(a, b)

