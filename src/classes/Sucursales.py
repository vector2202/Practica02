import Interfaz
import csv
class Sucursales(Interfaz):
    
    def __init__(self,identificador, nombre,fechaDeApertura, direccion, telefonos):
        super().__init__(identificador, nombre,fechaDeApertura,direccion, telefonos)

    def getNumEmpleados(self):
        pass    

    def numeroEmpleados(self):
        pass
    
    def __str__(self):
        numeros = ''
        for numero in self.telefonos:
            numeros += f'{numero}, '
        return f'Identificador de la sucursal: {self.identificador}.\nNombre: {self.nombre}\nDireccion: {self.direccion}\
            \nTelefonos: {numeros}\nFecha de apertura: {self.fechaDeApaertura}'


    
        
