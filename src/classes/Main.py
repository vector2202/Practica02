import EGA
def mostrar_menu(nombre,opciones):
    '''
    Funcion que despliega un menu con opciones para poder interactuar

    Parametros
    ----------
    nombre: str
    opciones: str

    Imprime las opciones
    '''
    print(f'# {nombre}. Bienvenido al sistema de archivos del Gran Abarrotero. Seleccione una opción:')
    for clave in sorted(opciones):
        print(f' {clave}) {opciones[clave][0]}')

def leer_opcion(opciones):
    '''
    Metodo que lee la opcion escogida y devuele error si no se encuentra entre las opciones

    Parametros
    ----------

    opciones: str
        Devuelve a que sea una de las opciones a escoger, en su defecto imprime que la opcion fue incorrecta
    '''

    while (a := input('Opción: ')) not in opciones:
        print('Opción incorrecta, vuelva a intentarlo.')
    return a

def ejecutar_opcion(opcion, opciones):
    '''
    Metodo que ejecuta la opcion que se escogio en el menu

    Parametros
    ----------

    opcion: str
    opciones: str
    '''
    opciones[opcion][1]()

def generar_menu(nombre, opciones, opcion_salida):
    '''
    Metodo que genera el menu para el usuario

    Parametros
    ----------

    nombre: str
    opciones: str
    opcion_salida: str

    Devuelve en el menu la opcion que se escogio
    '''
    opcion = None
    while opcion != opcion_salida:
        mostrar_menu(nombre,opciones)
        opcion = leer_opcion(opciones)
        ejecutar_opcion(opcion, opciones)
        print()

def main():

    opciones = {
        '1' : ('Consultar', submenuC),
        '2' : ('Agregar', submenuA),
        '3' : ('Eliminar', submenuE),
        '4' : ('Editar', submenuEd),
        '5' : ('Salir', salir)
    }

    generar_menu('Menu Principal', opciones,'5')

# Consultar
def submenuC():
    '''
    Metodo que genera el submenu para poder consultar informacion
    '''
    opciones={
        'a' : ('Empleado', EGA.consultarEmpleado),
        'b' : ('Producto', EGA.consultarProducto),
        'c' : ('Sucursal', EGA.consultarSucursal),
        'd' : ('Volver al menu principal',salir)
    }
    generar_menu('Consultar',opciones,'d')


# Agregar
def submenuA():
    '''
    Metodo que genera el submenu para poder agregar informacion
    '''
    opciones={
        'a' : ('Empleado', EGA.agregarEmpleado),
        'b' : ('Producto', EGA.agregarProducto),
        'c' : ('Sucursal', EGA.agregarSucursal),
        'd' : ('Volver al menu principal',salir)
    }
    generar_menu('Agregar',opciones,'d')



# Eliminar
def submenuE():
    '''
    Metodo que genera el submenu para poder eliminar informacion
    '''
    opciones={
        'a' : ('Empleado', EGA.eliminarEmpleado),
        'b' : ('Producto', EGA.eliminarProducto),
        'c' : ('Sucursal', EGA.eliminarSucursal),
        'd' : ('Volver al menu principal',salir)
    }
    generar_menu('Eliminar',opciones,'d')



# Editar
def submenuEd():
    '''
    Metodo que genera el submenu para poder editar informacion
    '''
    opciones={
        'a' : ('Empleado', EGA.editarEmpleado),
        'b' : ('Producto', EGA.editarProducto),
        'c' : ('Sucursal', EGA.editarSucursal),
        'd' : ('Volver al menu principal',salir)
    }
    generar_menu('Editar',opciones,'d')


#Salir

def salir():
    '''
    Metodo para salir del menu
    '''
    print('Saliendo. Vuelva pronto')


if __name__ == "__main__":
    main()
