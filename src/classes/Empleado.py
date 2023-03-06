import Interfaz

class Empleado(Interfaz):
    
    def __init__(self,identificador, nombre, fechaNacimiento,direccion, telefonos, correo,puesto,sucursal):
        super().__init__(identificador, nombre, fechaNacimiento, direccion, telefonos)
        self.correos = correo
        self.puesto = puesto
        self.sucursal = sucursal
        


