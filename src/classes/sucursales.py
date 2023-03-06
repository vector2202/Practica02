
class Sucursales:
    
    def __init__(self,identificador, nombre, direccion, telefonos, fechaDeApaertura):
        self.identificador = identificador
        self.nombre = nombre 
        self.direccion = direccion 
        self.telefonos = telefonos 
        self.fechaDeApaertura = fechaDeApaertura

    def getIdentificador(self):
        return self.identificador
        
    def getNombre(self):
        return self.nombre
    
    def getDireccion(self):
        return self.direccion 
        
    def getTelefonos(self):
        return self.telefonos

    def getApertura(self):
        return self.fechaDeApaertura
    
    def getNumEmpleados(self):
        pass    
    
    def __str__(self):
        numeros = ''
        for numero in self.telefonos:
            numeros += f'{numero}, '
        return f'Identificador de la sucursal: {self.identificador}.\nNombre: {self.nombre}\nDireccion: {self.direccion}\
            \nTelefonos: {numeros}\nFecha de apertura: {self.fechaDeApaertura}'


    
        
