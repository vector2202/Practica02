
import Interfaz

class Sucursal(Interfaz.Interfaz):

    def __init__(self, identificador, nombre, fechaDeApertura, direccion, telefonos):
        super().__init__(identificador, nombre, fechaDeApertura, direccion, telefonos)

    def __iter__(self):
        return iter([self.identificador, self.nombre, self.fecha, self.direccion, self.telefonos])

    def __str__(self):
        return f'Identificador de la sucursal: {self.identificador}.\nNombre: {self.nombre}\nDireccion: {self.direccion}\
            \nTelefonos: {self.telefonos}\nFecha de apertura: {self.fecha}'