from datetime import datetime

class Personal:

    def __init__(
            self, 
            id=None, 
            nombre=None, 
            cargo=None,
            fecha_entrada=None,
            identificacion=None
            ):

        
        self._id = id
        self._nombre = nombre
        self._cargo = cargo
        self._fecha_entrada = fecha_entrada
        self._identificacion = identificacion

#Getters de la clase Padre (Personal)
    #id
    @property
    def id(self):
        return self._id
    #nombre
    @property
    def nombre(self):
        return self._nombre
    #cargo
    @property
    def cargo(self):
        return self._cargo
    #fecha de entrada
    @property
    def fecha_entrada(self):
        return self._fecha_entrada
    #identificacion
    @property
    def identificacion(self):
        return self._identificacion
    
# Setters de la clase Padre (Personal)

    #id (no se agrega un setter ya que ese valor es auto incrementable en la base de datos)

    #nombre
    @nombre.setter
    def nombre(self, value):
        self._nombre=value

    #cargo
    @cargo.setter
    def cargo(self, value):
        self._cargo=value

    #fecha de entrada
    @fecha_entrada.setter
    def fecha_entrada(self, value):
        self._fecha_entrada=value

    #identificacion
    @identificacion.setter
    def identificacion(self, value):
        if 1 <= value <= 9999999999:
            self._identificacion = value
        else:
            raise ValueError("La identificación debe tener un máximo de 10 dígitos")
        
    @staticmethod
    def ingresar_datos():
        nombre = input("Ingrese el nombre del personal: ")
        cargo = input("ingrese el cargo del personal: ")
        while True:#fecha ingreso
            fechaStr = input("ingrese la fecha de entrada año-mes-día: ")
            try:
                fecha_entrada = datetime.strptime(fechaStr, "%Y-%m-%d").date()
                break
            except ValueError:
                print("Formato incorrecto... intente año-mes-día")
        identificacion = int(input("ingrese la identificación del personal: "))

        return nombre, cargo, fecha_entrada, identificacion
    
    @staticmethod
    def imprimir_personal(personal):
        print(f"[(nombre){personal.nombre}][(profeción){personal.cargo}][(fechaIngreso){personal.fecha_entrada}][(id){personal.identificacion}]", end="")
    
    @staticmethod
    def imprimir_lista(entidades):
        for entidad in entidades:
            print(f"[{entidad.id}][(nombre){entidad.nombre}][(profeción){entidad.cargo}][(fechaIngreso){entidad.fecha_entrada}][(id){entidad.identificacion}]", end="")

    @staticmethod
    def ingresar_identificacion():
        identificacion = int(input("Ingrese la identificacion del personal: "))
        return identificacion

    def actualizar_datos(self, dato):
        nombre = input(f"Ingrese el nuevo nombre (nombre actual: {dato.nombre})") or dato.nombre
        cargo = input(f"Ingrese el nuevo cargo (cargo actual: {dato.cargo})") or dato.cargo
        fecha_str = input(f"Ingrese la nueva fecha de entrada (fecha de entrada actual: {dato.fecha_entrada})") or dato.fecha_entrada

        # Comprobar si la entrada es una cadena y no está vacía
        if isinstance(fecha_str, str) and fecha_str:
            try:
                # Intentar convertir la cadena en una fecha
                fecha_entrada = datetime.strptime(fecha_str, "%Y-%m-%d").date()
            except ValueError:
                # Si el formato es incorrecto, mantener la fecha actual
                print("Formato de fecha incorrecto, manteniendo la fecha actual.")
                fecha_entrada = dato.fecha_entrada
        else:
            # Si no se ingresa nada, mantener la fecha actual
            fecha_entrada = dato.fecha_entrada

    
        # Ingreso de la identificación con validación
        identificacion_input = input(f"Ingrese la nueva identificación (identificación actual: {dato.identificacion}): ")
        identificacion = int(identificacion_input) if identificacion_input else dato.identificacion
        
        # Retornar los datos actualizados
        return nombre, cargo, fecha_entrada, identificacion
    
    def ingresar_clave():
        print("=" * 30)
        print("      INICIO DE SESIÓN      ")
        print("=" * 30)

        username = input("Ingrese el nombre de usuario: ")
        password = input("Ingrese la contraseña: ")
        
        print("=" * 30)
        return username, password


  

class EmpleadosDTO(Personal):
    
    def __init__(
            self,
            id=None,
            nombre=None, 
            cargo=None, 
            fecha_entrada=None, 
            identificacion=None,
            sueldo_base=None
                ):

        super().__init__( 
                        id, 
                        nombre, 
                        cargo,
                        fecha_entrada,
                        identificacion
                         )
        
        self._sueldo_base = sueldo_base


    # Getters de la clase EmpleadosDTO:
    
    #sueldo
    @property
    def sueldo_base(self):
        return self._sueldo_base
   

    # Setters de la clase EmpleadosDTO

    #sueldo
    @sueldo_base.setter
    def sueldo(self, value):
        self._sueldo_base=value

    @staticmethod
    def ingresar_datos():
        nombre, cargo, fecha_entrada, identificacion = Personal.ingresar_datos()
        sueldo_base = input("ingrese el sueldo del empleado: ")
        return nombre, cargo, fecha_entrada, identificacion, sueldo_base
    
    @staticmethod
    def imprimir_personal(personal):
        Personal.imprimir_personal(personal)
        print(f"[(sueldo_base)${personal.sueldo_base}]")

    @staticmethod
    def imprimir_lista(empleados):
        print("Lista de empleados")
        for empleado in empleados:
            print(f"[{empleado.id}][(nombre){empleado.nombre}][(profeción){empleado.cargo}][(fechaIngreso){empleado.fecha_entrada}][(id){empleado.identificacion}][(sueldo_base)${empleado.sueldo_base}]")


    @staticmethod
    def ingresar_identificacion():
        return Personal.ingresar_identificacion()
    
    def actualizar_datos(self, dato):
        # Llamar al método de la clase base para obtener los valores básicos
        nombre, cargo, fecha_entrada, identificacion = Personal.actualizar_datos(self, dato)

        # Añadir la lógica para actualizar el campo sueldo
        sueldo_input = input(f"Ingrese el nuevo sueldo (sueldo_base actual: {dato.sueldo_base}): ")
        sueldo_base = float(sueldo_input) if sueldo_input else dato.sueldo_base

        # Retornar todos los valores, incluyendo el nuevo campo sueldo
        return nombre, cargo, fecha_entrada, identificacion, sueldo_base

    
    

class UsuariosDTO(Personal):
    def __init__(
                self,
                id=None,
                nombre=None,
                cargo=None,
                fecha_entrada=None,
                identificacion=None,
                clave=None
                ):
        
        super().__init__( 
                        id, 
                        nombre, 
                        cargo,
                        fecha_entrada,
                        identificacion
                         )
        
        self._clave = clave


 # Getters de la clase UsuarioDTO:
    #cargo
    @property
    def clave(self):
        return self._clave
 

# Setters de la clase UsuarioDTO:
    #cargo
    @clave.setter
    def clave(self, value):
        self._clave=value

    @staticmethod
    def ingresar_datos():
        nombre, cargo, fecha_entrada, identificacion = Personal.ingresar_datos()
        clave = input("ingrese la clave del usuario: ")
        return nombre, cargo, fecha_entrada, identificacion, clave
    
    @staticmethod
    def imprimir_personal(personal):
        Personal.imprimir_personal(personal)
        print(f"[(clave){personal.clave}]")

    @staticmethod
    def imprimir_lista(usuarios):
        print("Lista de Usuarios")
        for usuario in usuarios:
            print(f"[{usuario.id}][(nombre){usuario.nombre}][(profeción){usuario.cargo}][(fechaIngreso){usuario.fecha_entrada}][(id){usuario.identificacion}][(clave){usuario.clave}]")

    @staticmethod
    def ingresar_identificacion():
        return Personal.ingresar_identificacion()
    
    def actualizar_datos(self, dato):
        # Llamar al método de la clase base para obtener los valores básicos
        nombre, cargo, fecha_entrada, identificacion = Personal.actualizar_datos(self, dato)

        # Añadir la lógica para actualizar el campo clave
        clave = input(f"Ingrese la clave del usuario (clave actual: {dato.clave}): ") or dato.clave

        # Retornar todos los valores, incluyendo el nuevo campo sueldo
        return nombre, cargo, fecha_entrada, identificacion, clave



 