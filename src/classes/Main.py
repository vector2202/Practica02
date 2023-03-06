import EGA
def mostrar_menu(nombre,opciones):
    print(f'# {nombre}. Bienvenido al sistema de archivos del Gran Abarrotero. Seleccione una opción:')
    for clave in sorted(opciones):
        print(f' {clave}) {opciones[clave][0]}')

def leer_opcion(opciones):
    while (a := input('Opción: ')) not in opciones:
        print('Opción incorrecta, vuelva a intentarlo.')
    return a

def ejecutar_opcion(opcion, opciones):
    opciones[opcion][1]()

def generar_menu(nombre, opciones, opcion_salida):
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
    opciones={
        'a' : ('Empleado', EGA.consultarEmpleado),
        'b' : ('Producto', EGA.consultarProducto),
        'c' : ('Sucursal', EGA.consultarSucursal),
        'd' : ('Volver al menu principal',salir)
    }
    generar_menu('Consultar',opciones,'d')


# Agregar
def submenuA():
    opciones={
        'a' : ('Empleado', EGA.agregarEmpleado),
        'b' : ('Producto', EGA.agregarProducto),
        'c' : ('Sucursal', EGA.agregarSucursal),
        'd' : ('Volver al menu principal',salir)
    }
    generar_menu('Agregar',opciones,'d')



# Eliminar
def submenuE():
    opciones={
        'a' : ('Empleado', EGA.eliminarEmpleado),
        'b' : ('Producto', EGA.eliminarProducto),
        'c' : ('Sucursal', EGA.eliminarSucursal),
        'd' : ('Volver al menu principal',salir)
    }
    generar_menu('Eliminar',opciones,'d')



# Editar
def submenuEd():
    opciones={
        'a' : ('Empleado', EGA.editarEmpleado),
        'b' : ('Producto', EGA.editarProducto),
        'c' : ('Sucursal', EGA.editarSucursal),
        'd' : ('Volver al menu principal',salir)
    }
    generar_menu('Editar',opciones,'d')


#Salir

def salir():
    print('Saliendo. Vuelva pronto')


if __name__ == "__main__":
    main()