import Main
import Empleado
import Manejador
import Producto
import Sucursal
from Sucursal import Sucursal
from Empleado import Empleado
from Producto import Producto

def getInt(mensaje, error,min, max):
    while (True):
        print(mensaje)
        val = input()
        if val.isnumeric():
            if (int(val) < min or max < int(val)):
                print(error)
            else:
                return str(val)
        else:
            print(error)

def agregarEmpleado():
    '''Funcion que permite llenar los datos del empleado'''
    ID = str((Manejador.obtenerTamano('Empleado'))+1)
    print('El ID del nuevo empleado es ' + ID)
    nombre = input('Ingresa el nombre del empleado: ')
    nacimiento = getInt('Ingresa su fecha de nacimiento con formato aaaammdd: ', 'Ingrese una fecha valida', 9999999, 100000000)
    direccion = input('Ingrese su dirección: ')
    telefono = getInt('Ingrese su telefono: ', 'Ingrese un numero valido de diez digitos.', 999999999, 10000000000)
    correo = input('Ingrese su correo: ')                                                   
    puesto = input('Ingrese su puesto: ')
    sucursal = getInt('Ingrese su sucursal: ', 'Ingrese una suucrsal valida', 0,100)
    Empleadonuevo = Empleado(ID,nombre,nacimiento,direccion,telefono,correo,puesto,sucursal)
    Manejador.agregar(Empleadonuevo,'Empleado')


def agregarProducto():
    '''Funcion que permite llenar los datos del producto'''
    ID = str((Manejador.obtenerTamano('Producto'))+1)
    print('El ID del nuevo producto es ' + ID)
    nombre = input('Ingresa el nombre del producto: ')
    fechaPreparacion = getInt('Ingresa la fecha de preparación del producto con formato aaaammdd: ', 'Ingrese una fecha valida', 9999999, 100000000)
    precio = input('Ingresa el precio del producto: ')
    cantidad = input('Ingresa la cantidad de productos que se tienen: ')
    marca = input('Ingresa la marca del producto: ')
    presentación= input('Ingresa la forma de presentación: ')
    refrigeracion = input('Ingresa si requiere refrigeración o no: ')
    fechaCaducidad = getInt('Ingresa la fecha de caducidad con formato aaaammdd: ', 'Ingrese una fecha valida', 9999999, 100000000)
    ProductoNuevo = Producto(ID, nombre, fechaPreparacion,precio,cantidad,marca,presentación,refrigeracion,fechaCaducidad)
    Manejador.agregar(ProductoNuevo,'Producto')
   

def agregarSucursal():
    '''Funcion que permite llenar los datos de la sucursal'''
    id = str(Manejador.obtenerTamano('Sucursal')+1)
    print('El ID de la nueva sucursal es: ' + id)
    nombre = input('Ingresa el nombre de la sucursal: ')
    fechaApertura = getInt('Ingresa su fecha de apertura con formato aaaammdd: ', 'Ingrese una fecha valida.', 9999999, 100000000)
    direccion = input('Ingresa la direccion: ')
    telefono= getInt('Ingrese su telefono: ', 'Ingrese un numero valido de diez digitos.', 999999999, 10000000000)
    SucursalNueva = Sucursal(id, nombre, fechaApertura,direccion,telefono)
    Manejador.agregar(SucursalNueva,'Sucursal')

def consultarEmpleado():
    '''Funcion que permite consular al objeto empleado'''
    IDaConsultar = input('Ingrese el ID del empleado que desea consultar: ')
    empleadoGenerico = Empleado("", "", "", "", "", "", "", "")
    Manejador.consultar(IDaConsultar,empleadoGenerico,'Empleado')

def consultarProducto():
    '''Funcion que permite consular al objeto Producto'''
    IDaConsultar = input('Ingrese el ID del producto a consultar: ')
    productoGenerico = Producto("", "", "", "", "", "", "", "", "")
    Manejador.consultar(IDaConsultar, productoGenerico, 'Producto')

def consultarSucursal():
    '''Funcion que permite consular al objeto Sucursal'''
    IDaConsultar = input('Ingrese el ID de la sucursal a consultar: ')
    sucursalGenerico = Sucursal("", "", "", "", "")
    Manejador.consultar(IDaConsultar, sucursalGenerico, 'Sucursal')


def eliminarEmpleado():
    '''Funcion que elimina el dato de empleado deseado'''
    IDaEliminar = input('Ingrese el ID del empleado que desea eliminar: ')
    empleadoGenerico = Empleado("", "", "", "", "", "", "", "")
    Manejador.eliminar(IDaEliminar,empleadoGenerico,'Empleado')

def eliminarProducto():
    '''Funcion que elimina el dato de producto deseado'''
    IDaEliminar = input('Ingrese el ID del producto que desea eliminar: ')
    productoGenerico = Producto("", "", "", "", "", "", "", "", "")
    Manejador.eliminar(IDaEliminar, productoGenerico, 'Producto')

def eliminarSucursal():
    '''Funcion que elimina el dato de sucursal deseado'''
    IDaEliminar = input('Ingrese el ID de la sucursal que desea eliminar: ')
    sucursalGenerico = Sucursal("", "", "", "", "")
    Manejador.eliminar(IDaEliminar, sucursalGenerico, 'Sucursal')

def editarEmpleado():
    '''Funcion que perimte editar datos del empleado'''
    IDaEditar = input('Ingrese el ID del empleado que desea editar: ')
    nombre = input('Ingresa el nombre del empleado: ')
    nacimiento = getInt('Ingresa su fecha de nacimiento con formato aaaammdd: ', 'Ingrese una fecha valida', 9999999, 100000000)
    direccion = input('Ingrese su dirección: ')
    telefono = getInt('Ingrese su telefono: ', 'Ingrese un numero valido de diez digitos.', 999999999, 10000000000)
    correo = input('Ingrese su correo: ')
    puesto = input('Ingrese su puesto: ')
    sucursal = input('Ingrese su sucursal: ')
    EmpleadoEditado = Empleado(IDaEditar,nombre,nacimiento,direccion,telefono,correo,puesto,sucursal)
    Manejador.editar(IDaEditar, EmpleadoEditado,'Empleado')

def editarProducto():
    '''Funcion que perimte editar datos del producto'''
    IDaEditar = input('Ingrese el ID del producto que desea editar: ')
    nombre = input('Ingresa el nombre del producto: ')
    precio = input('Ingresa el precio del producto: ')
    cantidad = input('Ingresa la cantidad de productos que se tienen: ')
    marca = input('Ingresa la marca del producto: ')
    presentación= input('Ingresa la forma de presentación: ')
    refrigeracion = input('Ingresa si requiere refrigeración o no: ')
    fechaPreparacion = getInt('Ingresa la fecha de preparación del producto con formato aaaammdd: ', 'Ingrese una fecha valida', 9999999, 100000000)
    fechaCaducidad = getInt('Ingresa la fecha de caducidad con formato aaaammdd: ', 'Ingrese una fecha valida', 9999999, 100000000)
    ProductoEditado = Producto(IDaEditar, nombre, fechaPreparacion,precio,cantidad,marca,presentación,refrigeracion,fechaCaducidad)
    Manejador.editar(IDaEditar,ProductoEditado,'Producto')
    


def editarSucursal():
    '''Funcion que perimte editar datos de la sucursal'''
    IDaEditar = input('Ingrese el ID de la sucursal que desea editar: ')
    nombre = input('Ingresa el nombre de la sucursal: ')
    fechaApertura = getInt('Ingresa su fecha de apertura con formato aaaammdd: ', 'Ingrese una fecha valida.', 9999999, 100000000)
    direccion = input('Ingresa la direccion: ')
    telefono= getInt('Ingrese su telefono: ', 'Ingrese un numero valido de diez digitos.', 999999999, 10000000000)
    SucursalEditada = Sucursal(IDaEditar, nombre, fechaApertura,direccion,telefono)
    Manejador.editar(IDaEditar,SucursalEditada,'Sucursal')
