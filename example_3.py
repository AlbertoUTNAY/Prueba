'''
print("Concersiones de tipos de datos")
int_a = 20
print(int_a,type(int_a))

float_a = float(int_a)
print(float_a,type(float_a))

string_a = str (int_a)
print(string_a,type(string_a))

complex_a = complex(int_a)
print(complex_a,type(complex_a))

bool_a = bool(int_a)
print(bool_a,type(bool_a))
'''

print("Operaciones")
a = 5
b = 10
print(a - b)

# Operaciones de comparacion
print( a > b)
print( a == b)
print( a != b)
print( a <= b)
print( a >= b)
 
 # Operacions Logicas
print("Operaciones Logicas")

c = True
d = False
print(c or d)
print((a > 10) and (a > b))

print("Operaciones de asignación")
x  = 5
print(x)
x +=10  # x = x + 10
print(x)
x **=2 # x = x * x
print(x) 

print("Membresia operatos")
list1 = [8, 20, 19, 16]
print(8 not in list1)

print("Indexacion")
list1=[80,20,18,19,17]
list1="Python"
print(list1[0])
print(list1[0:4])
print(list1[-5:-1])
