class Interfaz:
    '''
    Clase Interfaz

    ...

    Atributos
    ---------
    identificador: str
        identificador del empleado, sucursal o producto
    nombre: str
        nombre
    fecha: str
        fecha
    direccion: str
        direccion
    telefonos: str
        telefonos

    Metodos
    -------
    def getIdentificador(self):
        return self.identificador

    def getNombre(self):
        return self.nombre

    def getDireccion(self):
        return self.direccion

    def getTelefonos(self):
        return self.telefonos

    def getFecha(self):
        return self.fecha

    def __str__(self):
        return f'Identificador : {self.identificador}.\nNombre: {self.nombre}\nDireccion: {self.direccion}\
                \nFecha de apertura: {self.fecha}'

    def __iter__(self):
        return iter([self.identificador, self.nombre, self.direccion, self.telefonos, self.fecha])


    '''

    def __init__(self, identificador, nombre, fecha, direccion='', telefonos=''):
        '''
        Constructor que crea los atributos necesarios para la interfaz.

        Parametros
        ----------
        identificador: str
            devuelve identificador del empleado, sucursal o producto
        nombre: str
            devuelve nombre
        fecha: str
            devuelve fecha
        direccion: str
            devuelve direccion
        telefonos: str
            devuelve telefonos
            
        '''
        self.identificador = identificador
        self.nombre = nombre
        self.direccion = direccion
        self.telefonos = telefonos
        self.fecha = fecha

    # Metodos Accesores
    def getIdentificador(self):
        '''Metodo getter que devuelve el identificador'''
        return self.identificador

    def getNombre(self):
        '''Metodo getter que devuelve el nombre'''
        return self.nombre

    def getDireccion(self):
        '''Metodo getter que devuelve la direccion'''
        return self.direccion

    def getTelefonos(self):
        '''Metodo getter que devuelve los numero de telefono'''
        return self.telefonos

    def getFecha(self):
        '''Metodo getter que devuelve la fecha'''
        return self.fecha

    def __str__(self):
        '''Metodo string que devuelve en forma los atributos con su informacion'''
        return f'Identificador : {self.identificador}.\nNombre: {self.nombre}\nDireccion: {self.direccion}\
                \nFecha de apertura: {self.fecha}'

    def __iter__(self):
        '''Metodo iterador de objetos que itera en cada uno de los atributos y los devuelve'''
        return iter([self.identificador, self.nombre, self.direccion, self.telefonos, self.fecha])
