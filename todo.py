import os
runPrograma = True
todolist = []


#funcion para mostrar las opciones del menu
def showMenuOptions():
    print("")
    print("Por favor seleccione una opcion")
    print("")
    print("1- Crear una tarea")
    print("2- Marcar como realizada una tarea")
    print("3- Borrar una tarea")
    print("4- Salir")

#funcion para mostrar todas las tareas
def showTodoList():
    print("")
    print("")
    print("*********************************************")
    for y in todolist:
        print(f"{todolist.index(y)+1}-   {y} ")
    print("*********************************************")
    print("")

#funcion para guardar tarea en la lista
def createToDo():
    os.system("cls")#limpiamos pantalla
    global todolist
    print("crear una nueva tarea")
    todo = input("por favor ingrese el nombre de la tarea:   ")
    todolist.append(todo)
    print("")
    print("la tarea ah sido creada")
    #mostrar la lista de tareas
    showTodoList()

#funcion para marcar una tarea como realizada
def updateToDo():
    global todolist
    print("Se actualizara una tarea")
    todoID = int(input("indique el indice numerico de la tarea a marcar como realizada:  "))
    todolist[todoID-1]=  todolist[todoID-1] + "\t✅"
    showTodoList()

#funcion para eliminar una tarea
def delTodo():
    global todolist
    print("Se eliminara una tarea")
    todoID = int(input("indique el indice numerico de la tarea a eliminar:  "))
    del todolist[todoID-1]
    showTodoList()


def main():
    global runPrograma
    print(" .: Welcome to a python TO-DO list :.")
    flag =True
    while runPrograma:
        while flag:
            showMenuOptions()#se muestra el menu
            option = int(input("Ingresa el numero de la opcion: "))#se escoge la opcion
            match option:
                case 1: createToDo()
                case 2: updateToDo()
                case 3: delTodo()
                case 4: 
                    print("Adios")
                    runPrograma = False
                    flag = False
                case _: print("Opcion no reconocida")

        

if __name__ == "__main__": #esta configuracion es comunmente usada en python evalua si el archivo en el cual se trabaja es el principal
    main()

