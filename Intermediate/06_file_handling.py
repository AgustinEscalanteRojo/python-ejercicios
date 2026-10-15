## File Handling ##

import os

# .txt file
txt_file = open("Intermediate/my_file.txt", "w+") # Leer, escribir y sobreescribir si ya existe

txt_file.write("Mi nombre es Agustin\nMi apellido es Moure\n35años\nY mi lenguaje preferido es Python")

#print(txt_file.read())
print(txt_file.read(10))  # Lee 10 caracteres
print(txt_file.readline()) # Lee linea por linea
print(txt_file.readlines()) # Lee todas las lineas
for line in txt_file.readlines():
    print(line)

txt_file.write("\nAunque tambien me gusta Javascript")
print(txt_file.readline())

txt_file.close()

with open("Intermediate/my_file.txt", "a") as my_other_file:
    my_other_file.write("\nY Swift")

#os.remove("Intermediate/my_file.txt")  # Elimina el archivo

# .josn file

import json 

json_file = open("Intermediate/my_file.json", "w+")

json_test = {
    "name": "Brais", 
    "surname": "Moure", 
    "age": 35, 
    "language": ["Python", "Swift", "Kotlin"],
    "website": "https://moure.dev"}

json.dump(json_test, json_file, indent = 2)

json_file.close()

with open("Intermediate/my_file.json", "r") as my_other_file:
    for line in my_other_file.readlines():
        print(line)

json_dict = json.load(open("Intermediate/my_file.json"))
print(json_dict)
print(type(json_dict))
print(json_dict["name"])

# .csv file

import csv

csv_file = open("Intermediate/my_file.csv", "w+")



with open("Intermediate/my_file.csv", "r") as my_other_file:
    for line in my_other_file.readlines():
        print(line)

# .xlsx file
#import xlrd # debe instalarse el módulo

# .xml file

import xml

