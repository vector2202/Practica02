import Interfaz


class Producto(Interfaz.Interfaz):

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

    def __str__(self):
        return f'Identificador : {self.identificador}.\nNombre: {self.nombre}\nFechaPreparacio: {self.fecha}\
                \nPrecio: {self.precio}\nCantidad: {self.cantidad}\nMarca: {self.marca}\nPresentacion: {self.presentacion}\
                \nRefrigeracion: {self.refrigeracion}\nFechaCaducidad: {self.fechaCaducidad}'

    def __iter__(self):
        return iter([self.identificador, self.nombre, self.fecha, self.precio, self.cantidad, self.marca, self.presentacion, self.refrigeracion, self.fechaCaducidad])
