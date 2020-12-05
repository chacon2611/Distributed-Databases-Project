import mysql.connector as mariadb
import sys
import json
from mysql.connector import Error
from mysql.connector import errorcode
import os

#--------------------------CONEXION------------------------#

with open('credentialsMonte.json') as file:
    credentialsMonte = json.load(file)
    user = credentialsMonte["credentials"][0]["user"]
    password = credentialsMonte["credentials"][0]["password"]
    host = credentialsMonte["credentials"][0]["host"]
    port = credentialsMonte["credentials"][0]["port"]
    nameDB = credentialsMonte["credentials"][0]["database"]
try:
    conn = mariadb.connect(user = user,password = password,host=host, port = port, database = nameDB)
    cursor = conn.cursor()

except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

#--------------------------CONEXION------------------------#

def insertarC():
    idCliente = input("id: ")
    nombreCliente = input("Nombre: ")
    apellido1Cliente = input("Apellido Paterno: ")
    apellido2Cliente = input("Apellido Materno: ")
    rfcCliente = input("RFC: ")
    
    query = f"INSERT INTO Clientes(id,nombre,apellidoPaterno,apellidoMaterno,RFC) VALUES ('{idCliente}','{nombreCliente}','{apellido1Cliente}','{apellido2Cliente}','{rfcCliente}')"
    
    cursor.execute(query)
    print(f"{cursor.rowcount} details inserted") 
    conn.commit()
    #cursor.close()

def borrarC():
    idBorrar = input("Inserte el id a borrar: ")
    query = f"DELETE FROM Clientes WHERE id = ('{idBorrar}')"
    
    cursor.execute(query)
    print(f"{cursor.rowcount} details deleted") 
    conn.commit()

def modC():
    idModificar = input("Inserte el id del cliente a modificar: ")
    
    print("Que quieres modificar?")
    print("1. Nombre")
    print("2. Apellido paterno")
    print("3. Apellido materno")
    print("4. RFC")
    
    opcionModificar = input("Elige con un numero el dato a modificar: ")
    
    if opcionModificar == "1":
        nuevoNombre = input("Inserte el nuevo nombre: ")
        query = f"UPDATE Clientes SET nombre = ('{nuevoNombre}') WHERE id = ('{idModificar}')"
        cursor.execute(query)
        conn.commit()
        print(f"{cursor.rowcount} details affected")
    elif opcionModificar == "2":
        nuevoApellidoP = input("Inserte el nuevo apellido paterno: ")
        query = f"UPDATE Clientes SET apellidoPaterno = ('{nuevoApellidoP}') WHERE id = ('{idModificar}')"
        cursor.execute(query)
        conn.commit()
        print(f"{cursor.rowcount} details affected")
    elif opcionModificar == "3":
        nuevoApellidoM = input("Inserte el nuevo apellido materno: ")
        query = f"UPDATE Clientes SET apellidoMaterno = ('{nuevoApellidoM}') WHERE id = ('{idModificar}')"
        cursor.execute(query)
        conn.commit()
        print(f"{cursor.rowcount} details affected")
    elif opcionModificar == "4":
        nuevoRFC = input("Inserte el nuevo RFC: ")
        query = f"UPDATE Clientes SET RFC = ('{nuevoRFC}') WHERE id = ('{idModificar}')"
        cursor.execute(query)
        conn.commit()
        print(f"{cursor.rowcount} details affected")
    else:
        print("Ese stributo no existe! :( ")
        modC()
        
def insertarD():
    idDireccion = input("id: ")
    calleD = input("Calle: ")
    numeroD = input("Numero: ")
    coloniaD = input("Colonia: ")
    estadoD = input("Estado: ")
    cpD = input("CP: ")
    id_clienteD =input("id del Cliente: ")
    
    query = f"INSERT INTO Direcciones(id,calle,numero,colonia,estado,CP,id_cliente) VALUES ('{idDireccion}','{calleD}','{numeroD}','{coloniaD}','{estadoD}','{cpD}','{id_clienteD}')"
    
    cursor.execute(query)
    print(f"{cursor.rowcount} details inserted") 
    conn.commit()

def borrarD():
    idBorrar = input("Inserte el id a borrar: ")
    query = f"DELETE FROM Direcciones WHERE id = ('{idBorrar}')"
    
    cursor.execute(query)
    print(f"{cursor.rowcount} details deleted") 
    conn.commit()

def modD():
    idModificar = input("Inserte el id de la direccion a modificar: ")
    
    print("Que quieres modificar?")
    print("1. Calle")
    print("2. Numero")
    print("3. Colonia")
    print("4. Estado")
    print("5. CP")
    
    opcionModificar = input("Elige con un numero el dato a modificar: ")
    
    if opcionModificar == "1":
        nuevaCalle = input("Inserte la nueva calle: ")
        query = f"UPDATE Direcciones SET calle = ('{nuevaCalle}') WHERE id = ('{idModificar}')"
        cursor.execute(query)
        conn.commit()
        print(f"{cursor.rowcount} details affected")
    elif opcionModificar == "2":
        nuevoNumero = input("Inserte el nuevo numero: ")
        query = f"UPDATE Direcciones SET numero = ('{nuevoNumero}') WHERE id = ('{idModificar}')"
        cursor.execute(query)
        conn.commit()
        print(f"{cursor.rowcount} details affected")
    elif opcionModificar == "3":
        nuevaColonia= input("Inserte la nueva colonia: ")
        query = f"UPDATE Direcciones SET colonia = ('{nuevaColonia}') WHERE id = ('{idModificar}')"
        cursor.execute(query)
        conn.commit()
        print(f"{cursor.rowcount} details affected")
    elif opcionModificar == "4":
        nuevoEstado = input("Inserte el nuevo Estado: ")
        query = f"UPDATE Direcciones SET estado = ('{nuevoEstado}') WHERE id = ('{idModificar}')"
        cursor.execute(query)
        conn.commit()
        print(f"{cursor.rowcount} details affected")
    elif opcionModificar == "5":
        nuevoCP = input("Inserte el nuevo CP: ")
        query = f"UPDATE Direcciones SET CP = ('{nuevoCP}') WHERE id = ('{idModificar}')"
        cursor.execute(query)
        conn.commit()
        print(f"{cursor.rowcount} details affected")
    else:
        print("Esa funcion no existe! :(")
        modD()
    
def insertarCliente():
    insertarC()
    print("¿Deseas insertar otro cliente?")
    print("1. Si")
    print("2. No\n")
    otraop = input("Dime con un numero la opcion a elegir:")
    if otraop=="1":
        insertarCliente()
    elif otraop=="2":
        MenuClientes()
        
def borrarCliente():
    borrarC()
    print("¿Deseas borrar otro cliente?")
    print("1. Si")
    print("2. No\n")
    otraop = input("Dime con un numero la opcion a elegir:")
    if otraop=="1":
        borrarCliente()
    elif otraop=="2":
        MenuClientes()

def modCliente():
    modC()
    print("¿Desea modificar otro cliente?")
    print("1. Si")
    print("2. No\n")
    otraop = input("Dime con un numero la opcion a elegir:")
    if otraop=="1":
        modCliente()
    elif otraop=="2":
        MenuClientes()

def insertardir():
    insertarD()
    print("¿Deseas insertar otra direccion?")
    print("1. Si")
    print("2. No\n")
    otraop = input("Dime con un numero la opcion a elegir:")
    if otraop=="1":
        insertardir()
    elif otraop=="2":
        MenuDirecciones()
        
def borrardir():
    borrarD()
    print("¿Deseas borrar otra direccion?")
    print("1. Si")
    print("2. No\n")
    otraop = input("Dime con un numero la opcion a elegir:")
    if otraop=="1":
        borrardir()
    elif otraop=="2":
        MenuDirecciones()

def moddir():
    modD()
    print("¿Desea modificar otra direccion?")
    print("1. Si")
    print("2. No\n")
    otraop = input("Dime con un numero la opcion a elegir:")
    if otraop=="1":
        moddir()
    elif otraop=="2":
        MenuDirecciones()

def buscarCxD():
    print("De que atributo de +Direcciones+ quieres buscar cliente(s)\n")
    
    print("1. id")
    print("2. Calle")
    print("3. Numero")
    print("4. Colonia")
    print("5. Estado")
    print("6. CP")
    print("7. Regresar\n")
    
    opcionBusqueda = input("Inserte el atributo por el cual quiere realizar su busqueda: ")
    
    if opcionBusqueda=="1":
        buscar=input("Incerte el id de la direccion")
        query=f"SELECT Clientes.id, Clientes.nombre,Clientes.apellidoPaterno,Clientes.apellidoMaterno,Clientes.RFC FROM Clientes INNER JOIN Direcciones ON Clientes.id=Direcciones.id_cliente WHERE Direcciones.id_cliente='{buscar}'"
        cursor.execute(query)
        print("Clientes asociados a la direccion con id","*",buscar,"*")
        filas = cursor.fetchall()
        num_fields = len(cursor.description)
        field_names = [i[0] for i in cursor.description]
        print(field_names)
        for fila in filas:
            print(fila)
    elif opcionBusqueda=="2":
        buscar=input("Incerte el nombre de la calle:")
        query=f"SELECT Clientes.id, Clientes.nombre,Clientes.apellidoPaterno,Clientes.apellidoMaterno,Clientes.RFC FROM Clientes INNER JOIN Direcciones ON Clientes.id=Direcciones.id_cliente WHERE Direcciones.calle='{buscar}'"
        cursor.execute(query)
        filas = cursor.fetchall()
        num_fields = len(cursor.description)
        field_names = [i[0] for i in cursor.description]
        print("\nClientes asociados a la direccion con la calle","*",buscar,"*")
        print(field_names)
        for fila in filas:
            print(fila)
    elif opcionBusqueda=="3":
        buscar=input("Inserte el numero de la casa:")
        query=f"SELECT Clientes.id, Clientes.nombre,Clientes.apellidoPaterno,Clientes.apellidoMaterno,Clientes.RFC FROM Clientes INNER JOIN Direcciones ON Clientes.id=Direcciones.id_cliente WHERE Direcciones.numero='{buscar}'"
        cursor.execute(query)
        filas = cursor.fetchall()
        num_fields = len(cursor.description)
        field_names = [i[0] for i in cursor.description]
        print("\nClientes asociados a la direccion con el numero","*",buscar,"*")
        print(field_names)
        for fila in filas:
            print(fila)
    elif opcionBusqueda=="4":
        buscar=input("Inserte el nombre de la colonia:")
        query=f"SELECT Clientes.id, Clientes.nombre,Clientes.apellidoPaterno,Clientes.apellidoMaterno,Clientes.RFC FROM Clientes INNER JOIN Direcciones ON Clientes.id=Direcciones.id_cliente WHERE Direcciones.colonia='{buscar}'"
        cursor.execute(query)
        filas = cursor.fetchall()
        num_fields = len(cursor.description)
        field_names = [i[0] for i in cursor.description]
        print("\nClientes asociados a la direccion con la colonia","*",buscar,"*")
        print(field_names)
        for fila in filas:
            print(fila)
    elif opcionBusqueda=="5":
        buscar=input("Inserte el nombre del estado:")
        query=f"SELECT Clientes.id, Clientes.nombre,Clientes.apellidoPaterno,Clientes.apellidoMaterno,Clientes.RFC FROM Clientes INNER JOIN Direcciones ON Clientes.id=Direcciones.id_cliente WHERE Direcciones.estado='{buscar}'"
        cursor.execute(query)
        filas = cursor.fetchall()
        num_fields = len(cursor.description)
        field_names = [i[0] for i in cursor.description]
        print("\nClientes asociados a la direccion con el estado","*",buscar,"*")
        print(field_names)
        for fila in filas:
            print(fila)
    elif opcionBusqueda=="6":
        buscar=input("Inserte el CP:")
        query=f"SELECT Clientes.id, Clientes.nombre,Clientes.apellidoPaterno,Clientes.apellidoMaterno,Clientes.RFC FROM Clientes INNER JOIN Direcciones ON Clientes.id=Direcciones.id_cliente WHERE Direcciones.CP='{buscar}'"
        cursor.execute(query)
        filas = cursor.fetchall()
        num_fields = len(cursor.description)
        field_names = [i[0] for i in cursor.description]
        print("\nClientes asociados a la direccion con el CP","*",buscar,"*")
        print(field_names)
        for fila in filas:
            print(fila)
    elif opcionBusqueda=="7":
        MenuBusquedasC()
    else:
        print("\nEsa opcion no existe! :(\n")
        buscarCxD()
        
        
def MenuBusquedasC():
    
    print("1. id")
    print("2. Nombre")
    print("3. Apellido Paterno")
    print("4. Apellido Materno")
    print("5. RFC")
    print("6. Por Direccion")
    print("7. Regresar")
    
    opcionBusqueda = input("Inserte el atributo por el cual quiere realizar su busqueda: ")
    
    if opcionBusqueda=="1":
        buscar= input("Inserte el id a buscar: ")
        query=f"SELECT * FROM Clientes WHERE id LIKE ('%{buscar}%')"
        cursor.execute(query)
        filas = cursor.fetchall()
        num_fields = len(cursor.description)
        field_names = [i[0] for i in cursor.description]
        print(field_names)
        for fila in filas:
            print(fila)
    elif opcionBusqueda=="2":
        buscar= input("Inserte el Nombre a buscar: ")
        query=f"SELECT * FROM Clientes WHERE nombre LIKE ('%{buscar}%')"
        cursor.execute(query)
        filas = cursor.fetchall()
        num_fields = len(cursor.description)
        field_names = [i[0] for i in cursor.description]
        print(field_names)
        for fila in filas:
            print(fila)
    elif opcionBusqueda=="3":
        buscar= input("Inserte el Apellido Paterno a buscar: ")
        query=f"SELECT * FROM Clientes WHERE apellidoPaterno LIKE ('%{buscar}%')"
        cursor.execute(query)
        filas = cursor.fetchall()
        num_fields = len(cursor.description)
        field_names = [i[0] for i in cursor.description]
        print(field_names)
        for fila in filas:
            print(fila)
    elif opcionBusqueda=="4":
        buscar= input("Inserte el Apellido Materno a buscar: ")
        query=f"SELECT * FROM Clientes WHERE apellidoMaterno LIKE ('%{buscar}%')"
        cursor.execute(query)
        filas = cursor.fetchall()
        num_fields = len(cursor.description)
        field_names = [i[0] for i in cursor.description]
        print(field_names)
        for fila in filas:
            print(fila)
    elif opcionBusqueda=="5":
        buscar= input("Inserte el RFC a buscar: ")
        query=f"SELECT * FROM Clientes WHERE RFC LIKE ('%{buscar}%')"
        cursor.execute(query)
        filas = cursor.fetchall()
        num_fields = len(cursor.description)
        field_names = [i[0] for i in cursor.description]
        print(field_names)
        for fila in filas:
            print(fila)
    elif opcionBusqueda=="6":
        buscarCxD()
    elif opcionBusqueda=="7":
        MenuClientes()
    else:
        print("\nEsa opcion no existe! :(\n")
        busquedasC()
    
def busquedasC():
    MenuBusquedasC()
    print("\n¿Desea realizar otra busqueda?")
    print("1. Si")
    print("2. No\n")
    otraop= input("Dime con un numero la opcion a elegir:")
    if otraop=="1":
        busquedasC()
    elif otraop=="2":
        MenuClientes()

def MenuBusquedasD():
    
    print("1. id")
    print("2. Calle")
    print("3. Numero")
    print("4. Colonia")
    print("5. Estado")
    print("6. CP")
    print("7. Regresar")
    
    opcionBusqueda = input("Inserte el atributo por el cual quiere realizar su busqueda: ")
    
    if opcionBusqueda=="1":
        buscar= input("Inserte el id a buscar: ")
        query=f"SELECT * FROM Direcciones WHERE id LIKE ('%{buscar}%')"
        cursor.execute(query)
        filas = cursor.fetchall()
        num_fields = len(cursor.description)
        field_names = [i[0] for i in cursor.description]
        print(field_names)
        for fila in filas:
            print(fila)
    elif opcionBusqueda=="2":
        buscar= input("Inserte la calle a buscar: ")
        query=f"SELECT * FROM Direcciones WHERE calle LIKE ('%{buscar}%')"
        cursor.execute(query)
        filas = cursor.fetchall()
        num_fields = len(cursor.description)
        field_names = [i[0] for i in cursor.description]
        print(field_names)
        for fila in filas:
            print(fila)
    elif opcionBusqueda=="3":
        buscar= input("Inserte el numero a buscar: ")
        query=f"SELECT * FROM Direcciones WHERE numero LIKE ('%{buscar}%')"
        cursor.execute(query)
        filas = cursor.fetchall()
        num_fields = len(cursor.description)
        field_names = [i[0] for i in cursor.description]
        print(field_names)
        for fila in filas:
            print(fila)
    elif opcionBusqueda=="4":
        buscar= input("Inserte la colonia a buscar: ")
        query=f"SELECT * FROM Direcciones WHERE colonia LIKE ('%{buscar}%')"
        cursor.execute(query)
        filas = cursor.fetchall()
        num_fields = len(cursor.description)
        field_names = [i[0] for i in cursor.description]
        print(field_names)
        for fila in filas:
            print(fila)
    elif opcionBusqueda=="5":
        buscar= input("Inserte el Estado a buscar: ")
        query=f"SELECT * FROM Direcciones WHERE estado LIKE ('%{buscar}%')"
        cursor.execute(query)
        filas = cursor.fetchall()
        num_fields = len(cursor.description)
        field_names = [i[0] for i in cursor.description]
        print(field_names)
        for fila in filas:
            print(fila)
    elif opcionBusqueda=="6":
        buscar= input("Inserte el CP a buscar: ")
        query=f"SELECT * FROM Direcciones WHERE CP LIKE ('%{buscar}%')"
        cursor.execute(query)
        filas = cursor.fetchall()
        num_fields = len(cursor.description)
        field_names = [i[0] for i in cursor.description]
        print(field_names)
        for fila in filas:
            print(fila)
    elif opcionBusqueda=="7":
        MenuClientes()
    else:
        print("\nEsa opcion no existe! :(\n")
        busquedasD()

def busquedasD():
    MenuBusquedasD()
    print("\n¿Desea realizar otra busqueda?")
    print("1. Si")
    print("2. No\n")
    otraop= input("Dime con un numero la opcion a elegir:")
    if otraop=="1":
        busquedasD()
    elif otraop=="2":
        MenuDirecciones()

def buscarCxDGlobal():
    print("De que atributo de +Direcciones+ quieres buscar cliente(s) en las bases\n")
    
    print("1. id")
    print("2. Calle")
    print("3. Numero")
    print("4. Colonia")
    print("5. Estado")
    print("6. CP")
    print("7. Regresar\n")
    
    opcionBusqueda = input("Inserte el atributo por el cual quiere realizar su busqueda: ")
    if opcionBusqueda=="1":
        buscar=input("Incerte el id de la direccion")
        query=f"SELECT SucursalMorelia.Clientes.id,SucursalMorelia.Clientes.nombre,SucursalMorelia.Clientes.apellidoPaterno,SucursalMorelia.Clientes.apellidoMaterno,SucursalMorelia.Clientes.RFC FROM SucursalMorelia.Clientes INNER JOIN SucursalMorelia.Direcciones ON SucursalMorelia.Clientes.id=SucursalMorelia.Direcciones.id_cliente WHERE SucursalMorelia.Direcciones.id='{buscar}' UNION SELECT SucursalMonterrey.Clientes.id,SucursalMonterrey.Clientes.nombre,SucursalMonterrey.Clientes.apellidoPaterno,SucursalMonterrey.Clientes.apellidoMaterno,SucursalMonterrey.Clientes.RFC FROM SucursalMonterrey.Clientes INNER JOIN SucursalMonterrey.Direcciones ON SucursalMonterrey.Clientes.id=SucursalMonterrey.Direcciones.id_cliente WHERE SucursalMonterrey.Direcciones.id='{buscar}'"
        cursor.execute(query)
        print("Clientes asociados a la direccion con id","*",buscar,"*")
        filas = cursor.fetchall()
        num_fields = len(cursor.description)
        field_names = [i[0] for i in cursor.description]
        print(field_names)
        for fila in filas:
            print(fila)
    elif opcionBusqueda=="2":
        buscar=input("Incerte el nombre de la calle:")
        query=f"SELECT SucursalMorelia.Clientes.id,SucursalMorelia.Clientes.nombre,SucursalMorelia.Clientes.apellidoPaterno,SucursalMorelia.Clientes.apellidoMaterno,SucursalMorelia.Clientes.RFC FROM SucursalMorelia.Clientes INNER JOIN SucursalMorelia.Direcciones ON SucursalMorelia.Clientes.id=SucursalMorelia.Direcciones.id_cliente WHERE SucursalMorelia.Direcciones.calle='{buscar}' UNION SELECT SucursalMonterrey.Clientes.id,SucursalMonterrey.Clientes.nombre,SucursalMonterrey.Clientes.apellidoPaterno,SucursalMonterrey.Clientes.apellidoMaterno,SucursalMonterrey.Clientes.RFC FROM SucursalMonterrey.Clientes INNER JOIN SucursalMonterrey.Direcciones ON SucursalMonterrey.Clientes.id=SucursalMonterrey.Direcciones.id_cliente WHERE SucursalMonterrey.Direcciones.calle='{buscar}'"
        cursor.execute(query)
        filas = cursor.fetchall()
        num_fields = len(cursor.description)
        field_names = [i[0] for i in cursor.description]
        print("\nClientes asociados a la direccion con la calle","*",buscar,"*")
        print(field_names)
        for fila in filas:
            print(fila)
    elif opcionBusqueda=="3":
        buscar=input("Inserte el numero de la casa:")
        query=f"SELECT SucursalMorelia.Clientes.id,SucursalMorelia.Clientes.nombre,SucursalMorelia.Clientes.apellidoPaterno,SucursalMorelia.Clientes.apellidoMaterno,SucursalMorelia.Clientes.RFC FROM SucursalMorelia.Clientes INNER JOIN SucursalMorelia.Direcciones ON SucursalMorelia.Clientes.id=SucursalMorelia.Direcciones.id_cliente WHERE SucursalMorelia.Direcciones.numero='{buscar}' UNION SELECT SucursalMonterrey.Clientes.id,SucursalMonterrey.Clientes.nombre,SucursalMonterrey.Clientes.apellidoPaterno,SucursalMonterrey.Clientes.apellidoMaterno,SucursalMonterrey.Clientes.RFC FROM SucursalMonterrey.Clientes INNER JOIN SucursalMonterrey.Direcciones ON SucursalMonterrey.Clientes.id=SucursalMonterrey.Direcciones.id_cliente WHERE SucursalMonterrey.Direcciones.numero='{buscar}'"
        cursor.execute(query)
        filas = cursor.fetchall()
        num_fields = len(cursor.description)
        field_names = [i[0] for i in cursor.description]
        print("\nClientes asociados a la direccion con el numero","*",buscar,"*")
        print(field_names)
        for fila in filas:
            print(fila)
    elif opcionBusqueda=="4":
        buscar=input("Inserte el nombre de la colonia:")
        query=f"SELECT SucursalMorelia.Clientes.id,SucursalMorelia.Clientes.nombre,SucursalMorelia.Clientes.apellidoPaterno,SucursalMorelia.Clientes.apellidoMaterno,SucursalMorelia.Clientes.RFC FROM SucursalMorelia.Clientes INNER JOIN SucursalMorelia.Direcciones ON SucursalMorelia.Clientes.id=SucursalMorelia.Direcciones.id_cliente WHERE SucursalMorelia.Direcciones.colonia='{buscar}' UNION SELECT SucursalMonterrey.Clientes.id,SucursalMonterrey.Clientes.nombre,SucursalMonterrey.Clientes.apellidoPaterno,SucursalMonterrey.Clientes.apellidoMaterno,SucursalMonterrey.Clientes.RFC FROM SucursalMonterrey.Clientes INNER JOIN SucursalMonterrey.Direcciones ON SucursalMonterrey.Clientes.id=SucursalMonterrey.Direcciones.id_cliente WHERE SucursalMonterrey.Direcciones.colonia='{buscar}'"
        cursor.execute(query)
        filas = cursor.fetchall()
        num_fields = len(cursor.description)
        field_names = [i[0] for i in cursor.description]
        print("\nClientes asociados a la direccion con la colonia","*",buscar,"*")
        print(field_names)
        for fila in filas:
            print(fila)
    elif opcionBusqueda=="5":
        buscar=input("Inserte el nombre del estado:")
        query=f"SELECT SucursalMorelia.Clientes.id,SucursalMorelia.Clientes.nombre,SucursalMorelia.Clientes.apellidoPaterno,SucursalMorelia.Clientes.apellidoMaterno,SucursalMorelia.Clientes.RFC FROM SucursalMorelia.Clientes INNER JOIN SucursalMorelia.Direcciones ON SucursalMorelia.Clientes.id=SucursalMorelia.Direcciones.id_cliente WHERE SucursalMorelia.Direcciones.estado='{buscar}' UNION SELECT SucursalMonterrey.Clientes.id,SucursalMonterrey.Clientes.nombre,SucursalMonterrey.Clientes.apellidoPaterno,SucursalMonterrey.Clientes.apellidoMaterno,SucursalMonterrey.Clientes.RFC FROM SucursalMonterrey.Clientes INNER JOIN SucursalMonterrey.Direcciones ON SucursalMonterrey.Clientes.id=SucursalMonterrey.Direcciones.id_cliente WHERE SucursalMonterrey.Direcciones.estado='{buscar}'"
        cursor.execute(query)
        filas = cursor.fetchall()
        num_fields = len(cursor.description)
        field_names = [i[0] for i in cursor.description]
        print("\nClientes asociados a la direccion con el estado","*",buscar,"*")
        print(field_names)
        for fila in filas:
            print(fila)
    elif opcionBusqueda=="6":
        buscar=input("Inserte el CP:")
        query=f"SELECT SucursalMorelia.Clientes.id,SucursalMorelia.Clientes.nombre,SucursalMorelia.Clientes.apellidoPaterno,SucursalMorelia.Clientes.apellidoMaterno,SucursalMorelia.Clientes.RFC FROM SucursalMorelia.Clientes INNER JOIN SucursalMorelia.Direcciones ON SucursalMorelia.Clientes.id=SucursalMorelia.Direcciones.id_cliente WHERE SucursalMorelia.Direcciones.CP='{buscar}' UNION SELECT SucursalMonterrey.Clientes.id,SucursalMonterrey.Clientes.nombre,SucursalMonterrey.Clientes.apellidoPaterno,SucursalMonterrey.Clientes.apellidoMaterno,SucursalMonterrey.Clientes.RFC FROM SucursalMonterrey.Clientes INNER JOIN SucursalMonterrey.Direcciones ON SucursalMonterrey.Clientes.id=SucursalMonterrey.Direcciones.id_cliente WHERE SucursalMonterrey.Direcciones.CP='{buscar}'"
        cursor.execute(query)
        filas = cursor.fetchall()
        num_fields = len(cursor.description)
        field_names = [i[0] for i in cursor.description]
        print("\nClientes asociados a la direccion con el CP","*",buscar,"*")
        print(field_names)
        for fila in filas:
            print(fila)
    elif opcionBusqueda=="7":
        MenuBusquedasGlobalesC()
    else:
        print("\nEsa opcion no existe! :(\n")
        buscarCxD()
    

def MenuBusquedasGlobalesC():
    print("Atributos por los cuales puede realizar su busqueda:\n")
    
    print("1. id")
    print("2. Nombre")
    print("3. Apellido Paterno")
    print("4. Apellido Materno")
    print("5. RFC")
    print("6. Por direccion")
    print("7. Regresar")
    
    opcionBusqueda = input("Inserte el atributo por el cual quiere realizar su busqueda global: ")
    
    if opcionBusqueda == "1":
        buscarg=input("Inserte el id a buscar: ")
        query=f"SELECT * FROM SucursalMorelia.Clientes WHERE SucursalMorelia.Clientes.id LIKE '{buscarg}' UNION SELECT * FROM SucursalMonterrey.Clientes WHERE SucursalMonterrey.Clientes.id LIKE '{buscarg}'"
        cursor.execute(query)
        filas = cursor.fetchall()
        num_fields = len(cursor.description)
        field_names = [i[0] for i in cursor.description]
        print(field_names)
        for fila in filas:
            print(fila)
    elif opcionBusqueda == "2":
        buscarg=input("Inserte el nombre a buscar: ")
        query=f"SELECT * FROM SucursalMorelia.Clientes WHERE SucursalMorelia.Clientes.nombre='{buscarg}' UNION SELECT * FROM SucursalMonterrey.Clientes WHERE SucursalMonterrey.Clientes.nombre='{buscarg}'"
        cursor.execute(query)
        filas = cursor.fetchall()
        num_fields = len(cursor.description)
        field_names = [i[0] for i in cursor.description]
        print(field_names)
        for fila in filas:
            print(fila)
    elif opcionBusqueda == "3":
        buscarg=input("Inserte el apellido paterno a buscar: ")
        query=f"SELECT * FROM SucursalMorelia.Clientes WHERE SucursalMorelia.Clientes.apellidoPaterno='{buscarg}' UNION SELECT * FROM SucursalMonterrey.Clientes WHERE SucursalMonterrey.Clientes.apellidoPaterno='{buscarg}'"
        cursor.execute(query)
        filas = cursor.fetchall()
        num_fields = len(cursor.description)
        field_names = [i[0] for i in cursor.description]
        print(field_names)
        for fila in filas:
            print(fila)
    elif opcionBusqueda == "4":
        buscarg=input("Inserte el apellido materno a buscar: ")
        query=f"SELECT * FROM SucursalMorelia.Clientes WHERE SucursalMorelia.Clientes.apellidoMaterno='{buscarg}' UNION SELECT * FROM SucursalMonterrey.Clientes WHERE SucursalMonterrey.Clientes.apellidoMaterno='{buscarg}'"
        cursor.execute(query)
        filas = cursor.fetchall()
        num_fields = len(cursor.description)
        field_names = [i[0] for i in cursor.description]
        print(field_names)
        for fila in filas:
            print(fila)
    elif opcionBusqueda == "5":
        buscarg=input("Inserte el RFC a buscar: ")
        query=f"SELECT * FROM SucursalMorelia.Clientes WHERE SucursalMorelia.Clientes.RFC='{buscarg}' UNION SELECT * FROM SucursalMonterrey.Clientes WHERE SucursalMonterrey.Clientes.RFC='{buscarg}'"
        cursor.execute(query)
        filas = cursor.fetchall()
        num_fields = len(cursor.description)
        field_names = [i[0] for i in cursor.description]
        print(field_names)
        for fila in filas:
            print(fila)
    elif opcionBusqueda == "6":
        buscarCxDGlobal()
    elif opcionBusqueda=="7":
        MenuClientes()
        
    else:
        print("\nEsa opcion no existe! :(\n")
        busquedasGlobalesC()

def MenuBusquedasGlobalesD():
    print("Atributos por los cuales puede realizar su busqueda:\n")
    
    print("1. id")
    print("2. Calle")
    print("3. Numero")
    print("4. Colonia")
    print("5. Estado")
    print("6. CP")
    
    opcionBusqueda = input("Inserte el atributo por el cual quiere realizar su busqueda global: ")
    
    if opcionBusqueda == "1":
        buscarg=input("Inserte el id a buscar: ")
        query=f"SELECT * FROM SucursalMorelia.Direcciones WHERE SucursalMorelia.Direcciones.id LIKE '{buscarg}' UNION SELECT * FROM SucursalMonterrey.Direcciones WHERE SucursalMonterrey.Direcciones.id LIKE '{buscarg}'"
        cursor.execute(query)
        filas = cursor.fetchall()
        num_fields = len(cursor.description)
        field_names = [i[0] for i in cursor.description]
        print(field_names)
        for fila in filas:
            print(fila)
    elif opcionBusqueda == "2":
        buscarg=input("Inserte la calle a buscar: ")
        query=f"SELECT * FROM SucursalMorelia.Direcciones WHERE SucursalMorelia.Direcciones.calle='{buscarg}' UNION SELECT * FROM SucursalMonterrey.Direcciones WHERE SucursalMonterrey.Direcciones.calle='{buscarg}'"
        cursor.execute(query)
        filas = cursor.fetchall()
        num_fields = len(cursor.description)
        field_names = [i[0] for i in cursor.description]
        print(field_names)
        for fila in filas:
            print(fila)
    elif opcionBusqueda == "3":
        buscarg=input("Inserte el numero a buscar: ")
        query=f"SELECT * FROM SucursalMorelia.Direcciones WHERE SucursalMorelia.Direcciones.numero='{buscarg}' UNION SELECT * FROM SucursalMonterrey.Direcciones WHERE SucursalMonterrey.Direcciones.numero='{buscarg}'"
        cursor.execute(query)
        filas = cursor.fetchall()
        num_fields = len(cursor.description)
        field_names = [i[0] for i in cursor.description]
        print(field_names)
        for fila in filas:
            print(fila)
    elif opcionBusqueda == "4":
        buscarg=input("Inserte la colonia a buscar: ")
        query=f"SELECT * FROM SucursalMorelia.Direcciones WHERE SucursalMorelia.Direcciones.colonia='{buscarg}' UNION SELECT * FROM SucursalMonterrey.Direcciones WHERE SucursalMonterrey.Direcciones.colonia='{buscarg}'"
        cursor.execute(query)
        filas = cursor.fetchall()
        num_fields = len(cursor.description)
        field_names = [i[0] for i in cursor.description]
        print(field_names)
        for fila in filas:
            print(fila)
    elif opcionBusqueda == "5":
        buscarg=input("Inserte el estado a buscar: ")
        query=f"SELECT * FROM SucursalMorelia.Direcciones WHERE SucursalMorelia.Direcciones.estado='{buscarg}' UNION SELECT * FROM SucursalMonterrey.Direcciones WHERE SucursalMonterrey.Direcciones.estado='{buscarg}'"
        cursor.execute(query)
        filas = cursor.fetchall()
        num_fields = len(cursor.description)
        field_names = [i[0] for i in cursor.description]
        print(field_names)
        for fila in filas:
            print(fila)
    elif opcionBusqueda == "6":
        buscarg=input("Inserte el CP a buscar: ")
        query=f"SELECT * FROM SucursalMorelia.Direcciones WHERE SucursalMorelia.Direcciones.CP='{buscarg}' UNION SELECT * FROM SucursalMonterrey.Direcciones WHERE SucursalMonterrey.Direcciones.CP='{buscarg}'"
        cursor.execute(query)
        filas = cursor.fetchall()
        num_fields = len(cursor.description)
        field_names = [i[0] for i in cursor.description]
        print(field_names)
        for fila in filas:
            print(fila)
    else:
        print("\nEsa opcion no existe! :(\n")
        busquedasGlobalesD()

def busquedasGlobalesC():
    MenuBusquedasGlobalesC()
    print("\n¿Desea realizar otra busqueda?")
    print("1. Si")
    print("2. No\n")
    otraop= input("Dime con un numero la opcion a elegir:")
    if otraop=="1":
        busquedasGlobalesC()
    elif otraop=="2":
        MenuClientes()

def busquedasGlobalesD():
    MenuBusquedasGlobalesD()
    print("\n¿Desea realizar otra busqueda?")
    print("1. Si")
    print("2. No\n")
    otraop= input("Dime con un numero la opcion a elegir:")
    if otraop=="1":
        busquedasGlobalesD()
    elif otraop=="2":
        MenuDirecciones()

def MenuClientes():
    print("\nMenu Clientes de Monterrey:")
    print("1. Mostrar clientes")
    print("2. Insertar clientes")
    print("3. Eliminar clientes")
    print("4. Modificar clientes")
    print("5. Buscar")
    print("6. Mostrar todos los clientes de las bases de datos")
    print("7. Busquedas Globales")
    print("8. Regresar al menu principal\n")
    opcionMenu = input("Dame la opcion que desees: ")
            
    if opcionMenu == "1":
        query = "SELECT * FROM Clientes"
        cursor.execute(query)
        filas = cursor.fetchall()
        num_fields = len(cursor.description)
        field_names = [i[0] for i in cursor.description]
        print(field_names)
        for fila in filas:
            print(fila)
        print("¿Deseas reliazar alguna otra operacion?")
        print("1. Si")
        print("2. No\n")
        otraop = input("Dime con un numero la opcion a elegir: ")
        if otraop=="1":
            MenuClientes()
        else:
            print("Adios")
    elif opcionMenu == "2":
        insertarCliente()
    elif opcionMenu == "3":
        borrarCliente()
    elif opcionMenu == "4":
        modCliente()
    elif opcionMenu == "5":
        busquedasC()
    elif opcionMenu == "6":
        query="SELECT * FROM SucursalMorelia.Clientes UNION SELECT * FROM SucursalMonterrey.Clientes"
        cursor.execute(query)
        filas = cursor.fetchall()
        num_fields = len(cursor.description)
        field_names = [i[0] for i in cursor.description]
        print(field_names)
        for fila in filas:
            print(fila)
        print("\n¿Deseas reliazar alguna otra operacion?")
        print("1. Si")
        print("2. No\n")
        otraop = input("Dime con un numero la opcion a elegir: ")
        if otraop=="1":
            MenuClientes()
        else:
            print("Adios")
    elif opcionMenu == "7":
        busquedasGlobalesC()
    elif opcionMenu == "8":
        os.system('python3 menu22.py')
    else:
        print("\n***Esa no es una opcion valida***\n")
        MenuClientes()

def MenuDirecciones():
    print("\nMenu de direcciones de Monterrey:")
    print("1. Mostrar direcciones registradas")
    print("2. Insertar direcciones")
    print("3. Eliminar direcciones")
    print("4. Modificar direcciones")
    print("5. Buscar")
    print("6. Mostrar todos las direcciones de las bases de datos")
    print("7. Busquedas Golbales")
    print("8. Regresar al menu principal\n")
    opcionMenudir = input("Dame la opcion que desees: ")
            
    if opcionMenudir == "1":
        query = "SELECT * FROM Direcciones"
        cursor.execute(query)
        filas = cursor.fetchall()
        num_fields = len(cursor.description)
        field_names = [i[0] for i in cursor.description]
        print(field_names)
        for fila in filas:
            print(fila)
        print("¿Deseas reliazar alguna otra operacion?")
        print("1. Si")
        print("2. No\n")
        otraop = input("Dime con un numero la opcion a elegir: ")
        if otraop=="1":
            MenuDirecciones()
        else:
            print("Adios")
    elif opcionMenudir == "2":
        insertardir()
    elif opcionMenudir == "3":
        borrardir()
    elif opcionMenudir == "4":
        moddir()
    elif opcionMenudir=="5":
        busquedasD()
    elif opcionMenudir=="6":
        query="SELECT * FROM SucursalMorelia.Direcciones UNION SELECT * FROM SucursalMonterrey.Direcciones"
        cursor.execute(query)
        filas = cursor.fetchall()
        num_fields = len(cursor.description)
        field_names = [i[0] for i in cursor.description]
        print(field_names)
        for fila in filas:
            print(fila)
        print("\n¿Deseas reliazar alguna otra operacion?")
        print("1. Si")
        print("2. No\n")
        otraop = input("Dime con un numero la opcion a elegir: ")
        if otraop=="1":
            MenuClientes()
        else:
            print("Adios")
    elif opcionMenudir == "7":
        busquedasGlobalesD()
    elif opcionMenudir == "8":
        os.system('python3 menu22.py')
    else:
        print("\n***Esa no es una opcion valida***\n")
        MenuDirecciones()

def MenuCompras():
    print("\nMenu de compras de Morelia:")
    print("1. Mostrar compras registradas")
    print("2. Regresar al menu principal\n")
    opcionMenucomp = input("Dame la opcion que desees: ")
    
    if opcionMenucomp == "1":
        query = "SELECT * FROM Compras"
        cursor.execute(query)
        filas = cursor.fetchall()
        num_fields = len(cursor.description)
        field_names = [i[0] for i in cursor.description]
        print(field_names)
        for fila in filas:
            print(fila)
        print("¿Deseas reliazar alguna otra operacion?")
        print("1. Si")
        print("2. No\n")
        otraop = input("Dime con un numero la opcion a elegir: ")
        if otraop=="1":
            MenuCompras()
        else:
            print("Adios")
    elif opcionMenucomp=="2":
        os.system('python3 menu22.py')
    else:
        print("\n***Esa no es una opcion valida***\n")
        MenuCompras()
        
def crearTabla():
    d={}
    nombre=input("Hola dame el nombre de la tabala: ")
    numatri=int(input("Cuantos atributos quieres?"))
    atr=[]
    pri=["PRIMARY KEY"]
    foreign=[", FOREIGN KEY"]


    for i in range(numatri):
        a=input("Dame el nombre del atibuto:")
        atr.append(a)
    primaria=input("Que atributo es la llave primaria?")
    pri.append("(")
    pri.append(primaria)
    pri.append(")")

    d[nombre]=atr
    print(d)
    key=[]
    val=[]

    for k, v in d.items():
        key.append(k)
        val.append(v)
        
    create=["CREATE TABLE"]
    table_name=key
    atr2=[]
    abrir=("(")
    cerrar=(")")
    coma=(",")
    key.append(abrir)

    for i in range(numatri-1):
        n=("VARCHAR (100)")
        atr2.append(v[i])
        atr2.append(n)
        atr2.append(coma)
    atr2.append(v[len(v)-1])
    inti=("INT")
    atr2.append(inti)
    atr2.append(coma)


    foran=input("tiene llave fornaea? 1.SI, 2.NO")
    if foran=="1":
        foranea=input("Que atributo es la llave foranea?")
        otra_tabla=input("con que otra tabla es la relacion: ")
        atr_otra=input("atributo ralcion de la otra tabla: ")
        foreign.append("(")
        foreign.append(foranea)
        foreign.append(")")
        foreign.append("REFERENCES")
        foreign.append(otra_tabla)
        foreign.append("(")
        foreign.append(atr_otra)
        foreign.append(")")
        hola=(create+key+atr2+pri+foreign+[")"])
        string=" "
        query=(string.join(hola))
        cursor.execute(query)
        print("Tabla creada")
    else:
        hola=(create+key+atr2+pri+[")"])
        string=" "
        query=(string.join(hola))
        cursor.execute(query)
        print("Tabla creada")
        
    h=str(d)

    archivo= open('tablas.txt','a')
    archivo.write(h + "\n")
    archivo.close()

print("\n*-*-*-*-*-*-*-*-*-*-*-*-*Bienvenido a la Sucursal Monterrey*-*-*-*-*-*-*-*-*-*-*-*\n")
        
print("¿Quieres clientes, direcciones o crear una nueva tabla?")
print("1. Clientes")
print("2. Direcciones")
print("3. xComprasx")
print("4. Nueva tabla")
        
opcionBDMonterrey = input("Dime con un numero la opcion a elegir: ")
        
if opcionBDMonterrey == "1":
    MenuClientes()
elif opcionBDMonterrey == "2":
    MenuDirecciones()
elif opcionBDMonterrey == "3":
    MenuCompras()
elif opcionBDMonterrey == "4":
    crearTabla()
    
else:
    print("Esa no es una opcion valida :(")

        
