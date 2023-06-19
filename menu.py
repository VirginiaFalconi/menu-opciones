import mysql.connector

conexion = mysql.connector.connect(user = 'root', password = '', 
                                   host = 'localhost',
                                   database = 'normativa',
                                   port = '3306')

print(conexion)



def mostrar_menu():
    print("---- MENÚ ----")
    print("1. Agregar Registro: ")
    print("2. Mostrar Registro: ")
    print("3. Actualizar Registro: ")
    print("4. Eliminar Registro: ")
    print("5. Salir")
    print("--------------")

while True:

    mostrar_menu()
    opcion = input("Ingrese la opción deseada: ")

    if opcion == "1":
        print("Mostrar registros")

    elif opcion == "2":
        print("Ingresar un registro nuevo")
       

    elif opcion == "3":
        print("Actualizar registro")
       
    elif opcion == "4":
        print("Borrar un registro")
       
    elif opcion == "5":
        print("Gracias por usar nuestra base de datos")
        break
 
    
