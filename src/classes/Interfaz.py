class Interfaz:

    def __init__(self, identificador, nombre, fecha, direccion='', telefonos=[]):
        self.identificador = identificador
        self.nombre = nombre
        self.direccion = direccion
        self.telefonos = telefonos
        self.fecha = fecha

    # Metodos Accesores
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
