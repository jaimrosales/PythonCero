
#if
condicion = 5
comparativo = 10
if condicion <= comparativo:
 print (str(condicion) + " es menor a " + str(comparativo))
else: print(str(condicion) + " es mayor a " + str(comparativo))

if  not condicion :  print (condicion)
    
elif comparativo :  
    print (comparativo)
    if condicion : print (condicion)


#while
# contador = 0
# while contador < comparativo:
#     print(contador)
#     contador += 1

# print("adios")

#for 
# for x in range (comparativo):
#     print(x)

# for item in range(1, comparativo + 2):
#    print(item)
lenguajes = ["python","Go", "javascript","Rust+"]
frameworks = ["dyango", "Flask","FastApi", "Pyramid"]
# for y in lenguajes: 
#    if y == "Go": print("tu lenguaje va viene o vuela")
#    else: print(y)

#continue
#permite dar skip a una posicion en un ciclo

#break 
#permite salir (cancela) del ciclo

#else
#dentro de los ciclos, ejecuta una porcion del codigo cuando termina un ciclo, similar al defer en Go

for f in frameworks:
   if f == "Flask": 
        print("estas usando Flask") 
        continue
   print(f)
else:
   print("estes en donde estes, al final siempre te encontrare") 
for f in frameworks:
   if f == "FastApi":
      print("encontraste el framework")
      break
   print(f)


   
   






