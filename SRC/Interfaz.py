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
