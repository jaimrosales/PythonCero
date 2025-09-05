#funcion se declaran con def = definicio

# def fibonacci():        #define la funcion
#   #  """ esta es una funcion que nos devuelve la serie de fibonacci"""
#     return "serie de fibonacci"

# fibonacci() #invoca la funcion
# print (fibonacci())

# def suma (suma1,suma2):
#     resultado = suma1 + suma2
#     return resultado

# print (suma(20,45))

# def operaciones (suma1,suma2):
#     sumaResultado = suma1 + suma2
#     restaResultado = suma1 - suma2
#     multiResultado = suma1 * suma2
#     divResultado = suma1 / suma2
#     return sumaResultado, restaResultado, multiResultado, divResultado
# op = operaciones(20,45)
# for y in op:
#     print(y)


"""
Funcion: siempre devuelve un valor
procedimiento: no devuelve un valor
scope: es el alcance que tiene una variable dentro del codigo
"""
name = "kevin" 
def func():
    global name
    name = name +"hola"
    print(name)


#args y Kargs
def funcion(n1,n2,n3,n4,n5,n6):
    return n1+n2+n3+n4+n5+n6
suma = funcion(1,2,3,4,5,6)

def funcion_args(*args):
    for item in args:
        print(args)

# funcion_args (1,2,3,"fuoe",3,4,5,"pipipipi")

#kars #por lo general se usa cuando se quiere recibir un diccionario

days = {"dia1": "martes","dia2":"martes"}
def func(**kargs):
    print(kargs)


