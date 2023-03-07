
import Interfaz

class Empleado(Interfaz.Interfaz):
    '''
    Clase que representa al empleado

    ...

    Atributos
    ---------
    identificador: str
    nombre: str
    fechaNacimiento: str
    direccion: str
    telefonos: str
    correo: str
    puesto: str
    sucursal: str

    Metodos
    -------

    getCorreos():
        devuelve el correo
    getPuesto():
        devuelve el puesto
    getSucursal():
        devuelve el correo

    '''

    def __init__(self, identificador, nombre, fechaNacimiento, direccion, telefonos, correo, puesto, sucursal):
        super().__init__(identificador, nombre, fechaNacimiento, direccion, telefonos)
        '''
        Construye los atributos necesarios para el objeto empleado.

        Parametros
        ----------
        identificador: str
        nombre: str
        fechaNacimiento: str
        direccion: str
        telefonos: str
        correo: str
        puesto: str
        sucursal: str
            
        '''
        self.correos = correo
        self.puesto = puesto
        self.sucursal = sucursal

    # Metodos Accesores
    def getCorreos(self):
        '''Funcion que devuelve el correo'''
        return self.correos

    def getPuesto(self):
        '''Funcion que devuelve el puesto'''
        return self.puesto

    def getSucursal(self):
        '''Funcion que devuelve la sucursal en la que trabaja'''
        return self.sucursal

    def __str__(self):
        '''Funcion que devuelve la informacion de todos los atributos'''
        return f'Identificador : {self.identificador}.\nNombre: {self.nombre}\nFechaNacimiento: {self.fecha}\nDireccion: {self.direccion}\Telefonos: {self.telefonos}\nCorreos: {self.correos}\nPuesto: {self.puesto}\nSucursal: {self.sucursal}'

    def __iter__(self):
        '''Funcion iteradora de objetos que pasa por cada uno de los objetos que se le pasen como parametros'''
        return iter([self.identificador, self.nombre, self.fecha, self.direccion, self.telefonos, self.correos, self.puesto, self.sucursal])

    def getSucursal(self):
        '''Funcion que devuelve la sucursal'''
        return self.sucursal
