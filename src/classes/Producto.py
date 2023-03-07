import Interfaz


class Producto(Interfaz.Interfaz):
    '''
    Clase que representa al producto

    ...

    Atributos
    ---------
    Identificador: str
    nombre: str 
    fechaPreparacion: int
    precio: int
    cantidad: int
    marca: str
    presentacion: str
    refriferacion: str
    fechaCaducidad: int

    Metodos
    -------
    # Metodos Accesores
    def getPrecio(self):

    def getCantidad(self):

    def getMarca(self):

    def getPresentacion(self):

    def getRefrigeracion(self):

    def getFechaCaducidad(self):

    def __str__(self):

    def __iter__(self):

    '''

    def __init__(self, identificador, nombre, fechaPreparacion, precio, cantidad, marca, presentacion, refrigeracion, fechaCaducidad):
        '''
        Constructor que crea los atributos necesarios para el objeto producto

        Parametros
        ----------
        Identificador: str
        nombre: str 
        fechaPreparacion: int
        precio: int
        cantidad: int
        marca: str
        presentacion: str
        refriferacion: str
        fechaCaducidad: int
        

        '''
        super().__init__(identificador, nombre, fechaPreparacion)
        self.precio = precio
        self.cantidad = cantidad
        self.marca = marca
        self.presentacion = presentacion
        self.refrigeracion = refrigeracion
        self.fechaCaducidad = fechaCaducidad

    # Metodos Accesores
    def getPrecio(self):
        '''Metodo getter para el precio'''
        return self.precio

    def getCantidad(self):
        '''Metodo getter para la cantidad'''
        return self.cantidad

    def getMarca(self):
        '''Metodo getter para la marca'''
        return self.marca

    def getPresentacion(self):
        '''Metodo getter para la presentacion'''
        return self.presentacion

    def getRefrigeracion(self):
        '''Metodo getter para la refrigeracion'''
        return self.refrigeracion

    def getFechaCaducidad(self):
        '''Metodo getter para la fecha de caducidad'''
        return self.fechaCaducidad

    def __str__(self):
        '''Funcion que regresa la informacion de los atributos de manera que el lo pueda leer el usuario'''
        return f'Identificador : {self.identificador}.\nNombre: {self.nombre}\nFechaPreparacio: {self.fecha}\
                \nPrecio: {self.precio}\nCantidad: {self.cantidad}\nMarca: {self.marca}\nPresentacion: {self.presentacion}\
                \nRefrigeracion: {self.refrigeracion}\nFechaCaducidad: {self.fechaCaducidad}'

    def __iter__(self):
        '''Funcion iter es un iterador de objeto que itera en cada uno de los atributos que se le dieron al objeto'''
        return iter([self.identificador, self.nombre, self.fecha, self.precio, self.cantidad, self.marca, self.presentacion, self.refrigeracion, self.fechaCaducidad])
