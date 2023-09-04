'''
solicite al usuario el ingreso, activo, pasivo, patrimonio, sector y nombre de la empresa. 
Con los datos, mostrar la utilidad, roa, roe y luego registrelo en un archivo 
para que luego pueda recuperarlo
'''
'''
para abrir archivos csv se debe agregar el argumento newline=''
para abrir un archivo se debe crear una variable writer
'''
import os
import csv
import pathlib

AGREGAR = 1
MOSTRAR = 2
BUSCAR  = 3
MODIFICAR = 4
ELIMINAR = 5
SALIR = 0

def menu():
    os.system("cls")
    print(f"""          Bienvenido al programa. Que desea realizar?\n
        {AGREGAR}) Agregar nuevos datos.
        {MOSTRAR}) Mostrar datos.
        {BUSCAR}) Buscar datos.
        {MODIFICAR}) Modificar datos.
        {ELIMINAR}) Eliminar datos.
        {SALIR}) Salir del programa.
""")
#Procedimiento para registrar
def registrar_datos(nombre_datos):
    campos = ["Empresa", "Sector", "Ingreso", "Activo", "Pasivo", "Patrimonio", "Utilidad"]

    #Verificamos si existe el archivo, si existe se agrega los datos y si no, se crea
    while True:
        os.system("cls")
        print("Ingrese sus datos...")
        if not pathlib.Path(nombre_datos).exists():
            with open(nombre_datos, 'w', newline='') as datos_csv:
                escribir = csv.DictWriter(datos_csv, fieldnames=campos)
                escribir.writeheader()
        with open(nombre_datos, 'a', newline='') as datos_csv:
            escribir = csv.DictWriter(datos_csv, fieldnames=campos)
            empresa = input("Nombre: ")
            sector = input("Sector: ")
            ingreso = int(input("Ingreso: "))
            activo = int(input("Activo: "))
            pasivo = int(input("Pasivo: "))
            patrimonio = int(input("Patrimonio: "))

            utilidad = ingreso - pasivo

            #Ahora ingresamos la informacion en el archivo

            escribir.writerow({"Empresa": empresa, "Sector":sector, "Ingreso":ingreso, 
                        "Activo":activo, "Pasivo":pasivo, "Patrimonio":patrimonio, "Utilidad": utilidad})

            respuesta = input("¿Desea agregar más datos? (s/n): ")

            # Si la respuesta es "n", finaliza el bucle
            if respuesta == "n":
                break


def recuperar_informacion(nombre_datos):
    os.system("cls")
    print("Datos Registrados: ")
    with open(nombre_datos, "r", newline="") as datos_csv:
        #Creamos una variable para lectura
        leer = csv.DictReader(datos_csv)

        for linea in leer:
            for campo, valor in linea.items():
                print(f"{campo}: {valor}")
            print("~"*50)

def main():
    datos = "datos.csv"
    menu()
    opc = int(input("Seleccione una opcion: "))
    if opc == AGREGAR:
        registrar_datos(datos)
    if opc == MOSTRAR:
        recuperar_informacion(datos)
    
if __name__ == "__main__":
    main()


