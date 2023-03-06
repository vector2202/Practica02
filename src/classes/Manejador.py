import csv
import EGA
import Empleado
import Producto
import Sucursal
from Empleado import Empleado
from Producto import Producto
from Sucursal import Sucursal

def agregar(objeto, tipo):
    with open('' + str(tipo) + '.csv', 'a') as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow(objeto)
        return
def consultar(llave, objeto, tipo):
    with open('' + tipo + '.csv', 'r') as archivo:
        datos = csv.reader(archivo)
        for dato in datos:
            if(isinstance(objeto, Empleado)):
                aux = Empleado(*dato)
            elif(isinstance(objeto, Producto)):
                aux = Producto(*dato)
            else:
                aux = Sucursal(*dato)
            if(aux.identificador.__eq__(llave)):
                print(aux)
                return aux
        print("Objeto no existe")
        return
def eliminar(llave, objeto, tipo):
    datosAEscribir = []
    with open('' + tipo + '.csv', 'r') as archivo:
        datos = csv.reader(archivo)
        for dato in datos:
            if(isinstance(objeto, Empleado)):
                aux = Empleado(*dato)
            elif(isinstance(objeto, Producto)):
                aux = Producto(*dato)
            else:
                aux = Sucursal(*dato)
            if(not aux.identificador.__eq__(llave)):
                datosAEscribir.append(aux)
    with open('' + tipo + '.csv', 'w') as archivo:
        escritor = csv.writer(archivo)
        escritor.writerows(datosAEscribir)
    return
def editar(llave, objeto, tipo):
    datosAEscribir = []
    with open('' + tipo + '.csv', 'r') as archivo:
        datos = csv.reader(archivo)
        for dato in datos:
            if(isinstance(objeto, Empleado)):
                aux = Empleado(*dato)
            elif(isinstance(objeto, Producto)):
                aux = Producto(*dato)
            else:
                aux = Sucursal(*dato)
                
            if(aux.identificador.__eq__(llave)):
                datosAEscribir.append(objeto)
            else:
                datosAEscribir.append(aux)
    with open('' + tipo + '.csv', 'w') as archivo:
        escritor = csv.writer(archivo)
        escritor.writerows(datosAEscribir)
    return

def obtenerTamano(tipo):
    with open('' + tipo + '.csv', 'r') as archivo:
        datos = csv.reader(archivo)
        size = 0
        for dato in datos:
            size = 1 + size
    return size