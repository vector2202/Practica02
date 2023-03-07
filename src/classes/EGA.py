import Main
import Empleado
import Manejador
import Producto
import Sucursal
from Sucursal import Sucursal
from Empleado import Empleado
from Producto import Producto

def agregarEmpleado():
    '''Funcion que permite llenar los datos del empleado'''
    ID = str((Manejador.obtenerTamano('Empleado'))+1)
    print('El ID del nuevo empleado es ' + ID)
    nombre = input('Ingresa el nombre del empleado: ')
    nacimiento = input('Ingresa su fecha de nacimiento: ')
    direccion = input('Ingrese su dirección: ')
    telefono = input('Ingrese su telefono: ')
    correo = input('Ingrese su correo: ')
    puesto = input('Ingrese su puesto: ')
    sucursal = input('Ingrese su sucursal: ')
    Empleadonuevo = Empleado(ID,nombre,nacimiento,direccion,telefono,correo,puesto,sucursal)
    Manejador.agregar(Empleadonuevo,'Empleado')


def agregarProducto():
    '''Funcion que permite llenar los datos del producto'''
    ID = str((Manejador.obtenerTamano('Producto'))+1)
    print('El ID del nuevo producto es ' + ID)
    nombre = input('Ingresa el nombre del producto: ')
    fechaPreparacion = input('Ingresa la fecha de preparación del producto: ')
    precio = input('Ingresa el precio del producto: ')
    cantidad = input('Ingresa la cantidad de productos que se tienen: ')
    marca = input('Ingresa la marca del producto: ')
    presentación= input('Ingresa la forma de presentación: ')
    refrigeracion = input('Ingresa si requiere refrigeración o no: ')
    fechaCaducidad = input('Ingresa la fecha de caducidad: ')
    ProductoNuevo = Producto(ID, nombre, fechaPreparacion,precio,cantidad,marca,presentación,refrigeracion,fechaCaducidad)
    Manejador.agregar(ProductoNuevo,'Producto')
   

def agregarSucursal():
    '''Funcion que permite llenar los datos de la sucursal'''
    id = str(Manejador.obtenerTamano('Sucursal')+1)
    print('El ID de la nueva sucursal es: ' + id)
    nombre = input('Ingresa el nombre de la sucursal: ')
    fechaApertura = input('Ingresa la fecha de Apertura: ')
    direccion = input('Ingresa la direccion: ')
    telefono= input('Ingresa los telefonos: ')
    SucursalNueva = Sucursal(id, nombre, fechaApertura,direccion,telefono)
    Manejador.agregar(SucursalNueva,'Sucursal')

def consultarEmpleado():
    '''Funcion que permite consular al objeto empleado'''
    IDaConsultar = input('Ingrese el ID del empleado que desea consultar')
    empleadoGenerico = Empleado("", "", "", "", "", "", "", "")
    Manejador.consultar(IDaConsultar,empleadoGenerico,'Empleado')

def consultarProducto():
    '''Funcion que permite consular al objeto Producto'''
    IDaConsultar = input('Ingrese el ID del producto a consultar')
    productoGenerico = Producto("", "", "", "", "", "", "", "", "")
    Manejador.consultar(IDaConsultar, productoGenerico, 'Producto')

def consultarSucursal():
    '''Funcion que permite consular al objeto Sucursal'''
    IDaConsultar = input('Ingrese el ID de la sucursal a consultar')
    sucursalGenerico = Sucursal("", "", "", "", "")
    Manejador.consultar(IDaConsultar, sucursalGenerico, 'Sucursal')


def eliminarEmpleado():
    '''Funcion que elimina el dato de empleado deseado'''
    IDaEliminar = input('Ingrese el ID del empleado que desea eliminar')
    empleadoGenerico = Empleado("", "", "", "", "", "", "", "")
    Manejador.eliminar(IDaEliminar,empleadoGenerico,'Empleado')

def eliminarProducto():
    '''Funcion que elimina el dato de producto deseado'''
    IDaEliminar = input('Ingrese el ID del producto que desea eliminar')
    productoGenerico = Producto("", "", "", "", "", "", "", "", "")
    Manejador.eliminar(IDaEliminar, productoGenerico, 'Producto')

def eliminarSucursal():
    '''Funcion que elimina el dato de sucursal deseado'''
    IDaEliminar = input('Ingrese el ID de la sucursal que desea eliminar')
    sucursalGenerico = Sucursal("", "", "", "", "")
    Manejador.eliminar(IDaEliminar, sucursalGenerico, 'Sucursal')

def editarEmpleado():
    '''Funcion que perimte editar datos del empleado'''
    IDaEditar = input('Ingrese el ID del empleado que desea editar: ')
    nombre = input('Ingresa el nombre del empleado: ')
    nacimiento = input('Ingresa su fecha de nacimiento: ')
    direccion = input('Ingrese su dirección: ')
    telefono = input('Ingrese su telefono: ')
    correo = input('Ingrese su correo: ')
    puesto = input('Ingrese su puesto: ')
    sucursal = input('Ingrese su sucursal: ')
    EmpleadoEditado = Empleado(IDaEditar,nombre,nacimiento,direccion,telefono,correo,puesto,sucursal)
    Manejador.editar(IDaEditar, EmpleadoEditado,'Empleado')

def editarProducto():
    '''Funcion que perimte editar datos del producto'''
    IDaEditar = input('Ingrese el ID del producto que desea editar: ')
    nombre = input('Ingresa el nombre del producto: ')
    fechaPreparacion = input('Ingresa la fecha de preparación del producto: ')
    precio = input('Ingresa el precio del producto: ')
    cantidad = input('Ingresa la cantidad de productos que se tienen: ')
    marca = input('Ingresa la marca del producto: ')
    presentación= input('Ingresa la forma de presentación: ')
    refrigeracion = input('Ingresa si requiere refrigeración o no: ')
    fechaCaducidad = input('Ingresa la fecha de caducidad: ')
    ProductoEditado = Producto(IDaEditar, nombre, fechaPreparacion,precio,cantidad,marca,presentación,refrigeracion,fechaCaducidad)
    Manejador.editar(IDaEditar,ProductoEditado,'Producto')


def editarSucursal():
    '''Funcion que perimte editar datos de la sucursal'''
    IDaEditar = input('Ingrese el ID de la sucursal que desea editar: ')
    nombre = input('Ingresa el nombre de la sucursal: ')
    fechaApertura = input('Ingresa la fecha de Apertura: ')
    direccion = input('Ingresa la direccion: ')
    telefono= input('Ingresa los telefonos: ')
    SucursalEditada = Sucursal(IDaEditar, nombre, fechaApertura,direccion,telefono)
    Manejador.editar(IDaEditar,SucursalEditada,'Sucursal')
