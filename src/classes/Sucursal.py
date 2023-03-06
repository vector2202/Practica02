
import Interfaz
import csv

class Sucursal(Interfaz.Interfaz):
    
    def __init__(self,identificador, nombre,fechaDeApertura, direccion, telefonos):
        super().__init__(identificador, nombre,fechaDeApertura,direccion, telefonos)
        self.numEmpleados = 0

    def numeroEmpleados(self):
        """ Realiza la lectura del archivo que contiene los empleados de la sucursal.
        """
        with open('../assets/Empleados.csv', mode = 'r') as file:
            reader = csv.reader(file)  
            empleados = 0
            for rows in reader:
                print(type(rows[7]))
                if self.getIdentificador() == rows[7]:
                    empleados += 1     
            self.numEmpleados=empleados
           
    def getNumEmpleados(self):
        self.numeroEmpleados()
        return self.numEmpleados 
    
    def __str__(self):
        numeros = ''
        empleados = self.getNumEmpleados()
        for numero in self.telefonos:
            numeros += f'{numero}, '
        return f'Identificador de la sucursal: {self.identificador}.\nNombre: {self.nombre}\nDireccion: {self.direccion}\
            \nTelefonos: {numeros}\nFecha de apertura: {self.fecha}\nNumero de empleados: {empleados}'

# def main():
#     G = Sucursal('S1', 'PP',1,'Peña',[4444])
#     print(G)

# main()    