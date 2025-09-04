#variables
name = "Jaime"
print(name)


#constants
#para crear una constante se usa mayusculas, esto no quita que sea modificable sino que es una manera de identificar entre programadores que es una constante
#ejemplo
PI = 3.1416
SECONDS_IN_A_HOUR = 3600
number1 = 3
number2 = number1
number3 = 5

#id permite saber que tipo de identificador tiene la variable
print(id(name))
print(id(PI))
print(id(number1))
print(id(number2))#al salvar el mismo valor que number1, number2 tiene el mismo id que number1
print(id(number3))#al tener un valor diferente, number3 tiene un id diferente