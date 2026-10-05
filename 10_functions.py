### Functions ### 

def my_function ():
    print("Esto es una función")

my_function()

def sum_two_values (first_value: int, second_value):
    print(first_value + second_value)

sum_two_values(5, 7)
sum_two_values(54754, 71231)
sum_two_values("5", "7")
sum_two_values(1.4, 5.2)

def sum_two_values_with_return (first_value: int, second_value):
    return first_value + second_value

my_result = sum_two_values_with_return(1.4, 5.2)
print(my_result)

my_result = sum_two_values(10, 5)
print(my_result)

def print_name(name, surname):
    print(f"{name} {surname}")

print_name(surname="Moure", name="Brais")

def print_name_with_default (name, surname, alias = "Sin alias"):
    print(f"{name} {surname} {alias}")

print_name_with_default ("Moure", "Brais", "MoureDev")

def print_upper_texts(*texts):
    for text in texts:
        print(text.upper())

print_upper_texts("Hola", "Python", "¿Que tal?")
print_upper_texts("Hola")