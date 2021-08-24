#Este programa trata sobre un "launcher" donde puedes crear tu jerarquia de archivos python 

import os
from shutil import rmtree
import shutil

#Funciones

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def crearcarpetas():
    os.mkdir("sample")
    os.mkdir("docs")
    os.mkdir("tests")
    os.mkdir("C_DIR_AND_C_FILES")

def creararchivos():
    file = open("setup.py", "w")
    file2 = open("README.md", "w")
    file3 = open("LICENSE", "w")
    file4 = open("requirements.txt", "w")
    file5 = open("sample/__init__.py", "w")
    file6 = open("sample/helpers.py", "w")
    file7 = open("docs/conf.py", "w")
    file8 = open("docs/index.rst", "w")
    file9 = open("tests/test_basic.py", "w")
    file10 = open("tests/testadvanced.py", "w")
    file.close()

#Codigo 


clear()

op1 = input("1.-Crear repo 99.-Salir\n\n>>> ")

if op1 == "1":
    op1_1 = input("Indica el directorio\n\n>>> ")
    op1_2 = input(f"Quieres borrar los archivos de {op1_1} ...Y/N...\n\n>>> ")
    if op1_2 == "Y" or "y" or "yes":
        try:
            shutil.rmtree(op1_1)
        except OSError as e:
            print("Error")
        crearcarpetas()
        creararchivos()
    elif op1_2 == "N" or "n" or "no":
        print("Estamos creando los directorios y archivos necesarios, espere porfavor")
        crearcarpetas()
        creararchivos()
    else:
        SystemError
elif op1 == "99":
    SystemExit
else:
    print("Error")
    SystemError

print("El programa ha creado los archivos en:", os.getcwd(), "satisfactoriamente")


