
import Interfaz

class Sucursal(Interfaz.Interfaz):
    '''
    Clase que representa la Sucursal

    ...

    Atributos
    ---------
    identificador: str
    nombre: str
    fechaDeApertura: str
    direccion: str
    telefonos: str

    Metodos
    -------
    def __init__(self, identificador, nombre, fechaDeApertura, direccion, telefonos):
        super().__init__(identificador, nombre, fechaDeApertura, direccion, telefonos)

    def __iter__(self):

    def __str__(self):
        devuelve la informacion de los atributos

    '''

    def __init__(self, identificador, nombre, fechaDeApertura, direccion, telefonos):
        '''
        Constructor que crea todos los atributos necesarios para el objeto sucursal

        Parametros
        ----------
        identificador: str
        nombre: str
            nombre de la sucursal
        fechaDeApertura: str
            fecha de apertura de la sucursal
        direccion: str
            direccion de la sucursal
        telefonos: str
            telefono de la sucursal

        '''
        super().__init__(identificador, nombre, fechaDeApertura, direccion, telefonos)

    def __iter__(self):
        '''Funcion iteradora de objeto que itera en cada uno de los atributos'''
        return iter([self.identificador, self.nombre, self.fecha, self.direccion, self.telefonos])

    def __str__(self):
        '''Funcion que devuele la informacion de los atributos, humanamente legible'''
        return f'Identificador de la sucursal: {self.identificador}.\nNombre: {self.nombre}\nDireccion: {self.direccion}\
            \nTelefonos: {self.telefonos}\nFecha de apertura: {self.fecha}'
