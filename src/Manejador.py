import csv

def agregar(objeto, tipo):
    with open('' + tipo + '.csv', 'a') as archivo:
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
            if(aux.id.__eq__(llave)):
                return aux
        print("Empleado no existe")
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
            if(not aux.id.__eq__(llave)):
                datosAEscribir.append(aux)
    with open('' + tipo + '.csv', 'w') as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow(objeto)
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
                
            if(aux.id.__eq__(llave)):
                datosAEscribir.append(objeto)
            else:
                datosAEscribir.append(aux)
    with open('' + tipo + '.csv', 'w') as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow(objeto)
    return

def obtenerTamano(tipo):
    with open('' + tipo + '.csv', 'r') as archivo:
        datos = csv.reader(archivo)
        size = 0
        for dato in datos:
            size = 1 + size
    return size
