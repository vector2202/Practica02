
class Producto(Interfaz):

    def __init__(self,identificador, nombre, fechaPreparacion, precio,cantidad, marca, presentacion, refrigeracion, fechaCaducidad):
        super().__init__(identificador, nombre, fechaPreparacion)
        self.precio = precio
        self.cantidad = cantidad
        self.marca = marca
        self.presentacion = presentacion
        self.refrigeracion = refrigeracion
        self.fechaCaducidad = fechaCaducidad