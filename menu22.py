import os
    
            
def main():
    print("Bienvenido, a que sucursal quiere conectarse: ")
    print("1. Sucursal Morelia")
    print("2. Sucursal Monterrey")
    print("3. Salir\n")
            
    opcionMain = input("Dame la sucusal que prefieras: ")
        
    if opcionMain == "1":
       os.system('python3 SucursalMorelia.py')
        
    elif opcionMain == "2":
        os.system('python3 SucursalMonterrey.py')
        
    elif opcionMain =="3":
            print("\nAdios, vuelva pronto")
    else:
        print("Esa sucursal no existe :(")

main()
