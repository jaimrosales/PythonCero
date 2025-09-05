#diccionarios
#un diccionario es una coleccion de datos que almacena pares de clave y valor
#se definen con llaves {}

#el valor puede ser de cualquier tipo de dato
#un diccionario puede contener otros DICCIONARIOS, listas o tuplas

#los diccionarios son mutables, se pueden modificar, agregar o eliminar elementos
#los diccionarios no permiten claves duplicadas, cada clave debe ser unica
#los diccionarios no mantienen un orden, a partir de Python 3.7 si mantienen el orden de insercion
#se accede a los elementos del diccionario mediante su clave
#se pueden recorrer los diccionarios con un ciclo for
#se pueden crear diccionarios vacios

#definicion de un diccionario
#las claves deben de estar entre comillas
#cada clave esta separada de su valor por dos puntos :
#cada par clave-valor esta separado por una coma ,

usuario = {
    "nombre": "jaime",
    "apellido": "Rosales",
    "edad": 26,
    "ciudad": "Austin ",
    "es_admin": True,
    "hobbies": ["running", "musica", "anime"],
    "direccion": {
        "calle": "Calle ross 5501  ",
        "apto": "Apto 425",
        "codigo_postal": "78176"

    }
}

print(usuario)
print(type(usuario)) #<class 'dict'>
#acceder a un elemento del diccionario
print(usuario["nombre"]) #jaime
print(usuario["edad"]) #26
print(usuario["hobbies"]) #['running', 'musica', 'anime']
print(usuario["direccion"]) #{'calle': 'Calle ross 5501  ', 'apto': 'Apto 425', 'codigo_postal': '78176'}
print(usuario["direccion"]["calle"]) #Calle ross 5501  
#modificar un elemento del diccionario
usuario["edad"] = 27
print(usuario["edad"]) #27
#agregar un elemento al diccionario
usuario["telefono"] = "123-456-7890"
print(usuario["telefono"]) #123-456-7890
#eliminar un elemento del diccionario  
del usuario["ciudad"]
print(usuario)
#{'nombre': 'jaime', 'apellido': 'Rosales', 'edad': 27, 'es_admin': True, 'hobbies': ['running', 'musica', 'anime'], 'direccion': {'calle': 'Calle ross 5501  ', 'apto': 'Apto 425', 'codigo_postal': '78176'}, 'telefono': '123-456-7890'}
#longitud del diccionario
print(len(usuario)) #7
#recorrer un diccionario con un ciclo for
for clave in usuario:
    print(clave, ":", usuario[clave])
#nombre : jaime
#apellido : Rosales
#edad : 27
#es_admin : True
#hobbies : ['running', 'musica', 'anime']
#direccion : {'calle': 'Calle ross 5501  ', 'apto': 'Apto 425', 'codigo_postal': '78176'}
#telefono : 123-456-7890
#crear un diccionario vacio
producto = {}
print(producto) #{}
#agregar elementos al diccionario vacio
producto["nombre"] = "Laptop"
producto["marca"] = "Dell"
producto["precio"] = 800.00
producto["en_stock"] = True
print(producto) #{'nombre': 'Laptop', 'marca': 'Dell', 'precio': 800.0, 'en_stock': True}
print(len(producto)) #4 longitud del diccionario
print(len(usuario["direccion"])) #3 longitud del diccionario anidado
print(len(usuario["hobbies"])) #3 longitud de la lista dentro del diccionario
#verificar si una clave existe en el diccionario
print("nombre" in producto) #True
print("color" in producto) #False
#obtener todas las claves del diccionario
print(producto.keys()) #dict_keys(['nombre', 'marca', 'precio', 'en_stock'])
#obtener todos los valores del diccionario  
print(producto.values()) #dict_values(['Laptop', 'Dell', 800.0, True])
#obtener todos los pares clave-valor del diccionario
print(producto.items()) #dict_items([('nombre', 'Laptop'), ('marca', 'Dell'), ('precio', 800.0), ('en_stock', True)])
#limpiar un diccionario
producto.clear()
print(producto) #{}
#eliminar un diccionario
del producto
# print(producto) #NameError: name 'producto' is not defined


#otra forma de crear un diccionario
persona = dict(nombre="Carlos", apellido="Lara", edad=30)   #se usa la funcion dict() el cual es el constructor de diccionarios 
print(persona) #{'nombre': 'Carlos', 'apellido': 'Lara', '



