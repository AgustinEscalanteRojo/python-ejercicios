## Error Types ##

# SyntaxError
#print "Hola comunidad" # Error
print ("Hola comunidad")

# NameError
#print(language) # Error

language = "Spanish"
print(language) 

# IndexError
my_list = ["Python", "Swift", "Kotlin", "Dart", "Javascript"]
print(my_list[0])
print(my_list[4])
print(my_list[-1])
#print(my_list[5]) # Error

# ModulerNotFoundError
#import maths # Error
import math

# AttributeError
#print(math.PI) # Error
print(math.pi)

# KeyError
my_dict = {"Nombre": "Brais", "Apellido": "Moure", "Edad": 35, 1: "Python"}
print(my_dict["Edad"])
#print(my_dict["Apelido"]) # Error
print(my_dict["Apellido"])

# TypeError
my_list = ["Python", "Swift", "Kotlin", "Dart", "Javascript"]
#print(my_list["Nombre"])
print(my_list[0])

# ImportError
#from math import PI # Error
from math import pi
print(pi)

# ValueError
#my_int = int("10 Años")  #Error
my_int = int("10") 
print(type(my_int))

# ZeroDivisionError
#print(4/0) #Error
print(4/2)




