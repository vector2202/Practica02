
import Interfaz



class Empleado(Interfaz.Interfaz):

    def __init__(self, identificador, nombre, fechaNacimiento, direccion, telefonos, correo, puesto, sucursal):
        super().__init__(identificador, nombre, fechaNacimiento, direccion, telefonos)
        self.correos = correo
        self.puesto = puesto
        self.sucursal = sucursal

    # Metodos Accesores
    def getCorreos(self):
        return self.correos

    def getPuesto(self):
        return self.puesto

    def getSucursal(self):
        return self.sucursal

    def __str__(self):
        numeros = ''
        correos = ''
        #for numero in self.telefonos:
        numeros += f'{self.telefonos}, '
        #for correo in self.:
        correos += f'{self.correos}'

        return f'Identificador : {self.identificador}.\nNombre: {self.nombre}\nFechaNacimiento: {self.fecha}\nDireccion: {self.direccion}\Telefonos: {self.telefonos}\nCorreos: {self.correos}\nPuesto: {self.puesto}\nSucursal: {self.sucursal}'

    def __iter__(self):
        return iter([self.identificador, self.nombre, self.fecha, self.direccion, self.telefonos, self.correos, self.puesto, self.sucursal])

    def getSucursal(self):
        return self.sucursal
