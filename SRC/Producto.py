import Interfaz


class Producto(Interfaz):

    def __init__(self, identificador, nombre, fechaPreparacion, precio, cantidad, marca, presentacion, refrigeracion, fechaCaducidad):
        super().__init__(identificador, nombre, fechaPreparacion)
        self.precio = precio
        self.cantidad = cantidad
        self.marca = marca
        self.presentacion = presentacion
        self.refrigeracion = refrigeracion
        self.fechaCaducidad = fechaCaducidad

    # Metodos Accesores
    def getPrecio(self):
        return self.precio

    def getCantidad(self):
        return self.cantidad

    def getMarca(self):
        return self.marca

    def getPresentacion(self):
        return self.presentacion

    def getRefrigeracion(self):
        return self.refrigeracion

    def getFechaCaducidad(self):
        return self.fechaCaducidad
