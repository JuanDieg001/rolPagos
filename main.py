from accessData.conexionOrm import Database, DATABASE_URL
from accessData.entidades.modelos import BaseDeDatos, Empleados, Usuarios
from dominio.entidadesDto.dto import EmpleadosDTO, UsuariosDTO, Personal
from servicios.serviciosGenerales import GenericRepository, ServiciosEmpleados, ServiciosUsuarios, RolDePagos, ArtilugiosDelSistema
from accessData.entidades.modelos import Usuarios
import os


def main():

    #servicios C.R.U.D para empleados
    servicioGenerico = GenericRepository[Empleados](Empleados, db)
    servicioEmpleados = ServiciosEmpleados[Empleados](Empleados, db)
    #servicios C.R.U.D para usuario
    servicioGenericoU = GenericRepository[Usuarios](Usuarios, db)
    servicioUsuarios = ServiciosUsuarios[Usuarios](Usuarios, db)

    while True:#modulo de seguridad
        os.system('cls')
        usuario, clave = Personal.ingresar_clave()

        user = servicioUsuarios.login(usuario, clave)

        if user:
            if user.cargo == "administrador":
                
                os.system('cls')
                ArtilugiosDelSistema.mostrar_bienvenida(user.nombre, user.cargo)
                      
                while True:#menu de administrador de sistema

                    ArtilugiosDelSistema.menu_admin()
                    opcion= input("selecione una opción: ")

                    if opcion == "1":#Menú Empleados
                        while True:
                            ArtilugiosDelSistema.menu_empleados()

                            opcion = input("Seleccione una opción: ")

                            if opcion == "1":#ingresar empleado

                                (nombre, cargo, fecha_entrada, identificacion, sueldo_base) = EmpleadosDTO.ingresar_datos()
                                empleado = EmpleadosDTO(None, nombre, cargo, fecha_entrada, identificacion, sueldo_base)
                                servicioGenerico.crear(
                                                        nombre=empleado.nombre,
                                                        cargo=empleado.cargo, 
                                                        fecha_entrada=empleado.fecha_entrada, 
                                                        sueldo_base=empleado.sueldo, 
                                                        identificacion=empleado.identificacion
                                                        )
                                EmpleadosDTO.imprimir_personal(empleado)

                            elif opcion == "2":#Lista empleados
                                empleados = servicioGenerico.buscarTodo()
                                EmpleadosDTO.imprimir_lista(empleados)

                            elif opcion == "3":#buscar empleados
                                empleado = servicioGenerico.buscar(EmpleadosDTO.ingresar_identificacion())
                                if empleado:
                                    EmpleadosDTO.imprimir_personal(empleado)
                                else:
                                    print("empleado no encontrado.")

                            elif opcion == "4":#Actualizar empleados

                                empleado = servicioGenerico.buscar(EmpleadosDTO.ingresar_identificacion())
                                
                                if empleado:
                                    empleado_dto = EmpleadosDTO()
                                    (nombre, cargo, fecha_entrada, identificacion, sueldo_base) = empleado_dto.actualizar_datos(empleado)

                                    empleado_actualizado = EmpleadosDTO(empleado.id, nombre, cargo, fecha_entrada, identificacion, sueldo_base)
                                    
                                    servicioEmpleados.actualizar(empleado.id, empleado_actualizado)
                                    print("Empleado actualizado")
                                else:
                                    print("Empleado no encontrado.")

                            elif opcion == "5":#eliminar empleados
                                empleado = servicioGenerico.buscar(EmpleadosDTO.ingresar_identificacion())

                                if empleado:
                                    servicioGenerico.borrar(empleado.identificacion)

                                    print("Empleado eliminado exitosamente.")
                                else:
                                    print("Empleado no encontrado.")
                            
                            elif opcion == "6":#volver al sistema administrador
                                break
                            
                            else:
                                print("Opción inválida. Por favor, seleccione una opción válida.")
                    
                    elif opcion == "2":#Menú Usuarios
                        while True:
                            os.system('cls')
                            print("\n--- Menú Usuarios ---")
                            print("1. Crear Usuarios")
                            print("2. Mostrar todos los Usuarios")
                            print("3. Buscar Usuario")
                            print("4. Actualizar Usuario")
                            print("5. Eliminar Usuario")
                            print("6. volver a Menu")


                            opcion= input("selecione una opción: ")

                            if opcion == "1":#Crear Usuarios

                                (nombre, cargo, fecha_entrada, identificacion, clave) = UsuariosDTO.ingresar_datos()   

                                usuario = UsuariosDTO(None, nombre, cargo, fecha_entrada, identificacion, clave)
                                servicioGenericoU.crear(
                                                        nombre=usuario.nombre,
                                                        cargo=usuario.cargo, 
                                                        fecha_entrada=usuario.fecha_entrada, 
                                                        identificacion=usuario.identificacion,
                                                        clave=usuario.clave
                                                        )
                            
                                UsuariosDTO.imprimir_personal(usuario)

                            elif opcion == "2":#Mostrar todos los Usuarios
                                usuarios = servicioGenericoU.buscarTodo()
                                UsuariosDTO.imprimir_lista(usuarios)

                            elif opcion == "3":#Buscar Usuarios
                                usuario = servicioGenericoU.buscar(UsuariosDTO.ingresar_identificacion())
                                if usuario:
                                    UsuariosDTO.imprimir_personal(usuario)
                                else:
                                    print("Usuario no encontrado.")

                            elif opcion == "4":#Actualizar Usuario

                                usuario = servicioGenericoU.buscar(UsuariosDTO.ingresar_identificacion())

                                if usuario:

                                    usuario_dto = UsuariosDTO()
                                    (nombre, cargo, fecha_entrada, identificacion, clave) = usuario_dto.actualizar_datos(usuario)

                                    usuario_actualizado = UsuariosDTO(
                                                                    usuario.id,  # Mantén el ID actual
                                                                    nombre,
                                                                    cargo,
                                                                    fecha_entrada,
                                                                    identificacion,
                                                                    clave
                                                                    )
                                    
                                    servicioUsuarios.actualizar(usuario.id, usuario_actualizado)
                                    print("Usuario actualizado")
                                else:
                                    print("Usuario no encontrado.")
                                        
                            elif opcion == "5":#Eliminar Usuario
                                usuario = servicioGenericoU.buscar(UsuariosDTO.ingresar_identificacion())

                                if usuario:
                                    servicioGenericoU.borrar(usuario.identificacion)

                                    print("Usuario eliminado exitosamente.")
                                else:
                                    print("Usuario no encontrado.")

                            elif opcion == "6":#volver al sistema administrador
                                break
            
                    elif opcion == "3":#salir al login
                        break

                    else:
                        os.system('cls')
                        

            elif user.cargo == "contador":
                os.system('cls')
                ArtilugiosDelSistema.mostrar_bienvenida(user.nombre, user.cargo)
                
                while True:#menu de contador de sistema
                    os.system('cls')
                    ArtilugiosDelSistema.menu_contador()
                    opcion= input("selecione una opción: ")

                    if opcion == "1":#Menú Empleados
                        while True:
                            os.system('cls')
                            ArtilugiosDelSistema.menu_empleados

                            opcion = input("Seleccione una opción: ")

                            if opcion == "1":#ingresar empleado

                                (nombre, cargo, fecha_entrada, identificacion, sueldo_base) = EmpleadosDTO.ingresar_datos()
                                empleado = EmpleadosDTO(None, nombre, cargo, fecha_entrada, identificacion, sueldo_base)
                                servicioGenerico.crear(
                                                        nombre=empleado.nombre,
                                                        cargo=empleado.cargo, 
                                                        fecha_entrada=empleado.fecha_entrada, 
                                                        sueldo_base=empleado.sueldo, 
                                                        identificacion=empleado.identificacion
                                                        )
                                EmpleadosDTO.imprimir_personal(empleado)

                            elif opcion == "2":#Lista empleados
                                empleados = servicioGenerico.buscarTodo()
                                EmpleadosDTO.imprimir_lista(empleados)

                            elif opcion == "3":#buscar empleados
                                empleado = servicioGenerico.buscar(EmpleadosDTO.ingresar_identificacion())
                                if empleado:
                                    EmpleadosDTO.imprimir_personal(empleado)
                                else:
                                    print("empleado no encontrado.")

                            elif opcion == "4":#Actualizar empleados

                                empleado = servicioGenerico.buscar(EmpleadosDTO.ingresar_identificacion())
                                
                                if empleado:
                                    empleado_dto = EmpleadosDTO()
                                    (nombre, cargo, fecha_entrada, identificacion, sueldo_base) = empleado_dto.actualizar_datos(empleado)

                                    empleado_actualizado = EmpleadosDTO(empleado.id, nombre, cargo, fecha_entrada, identificacion, sueldo_base)
                                    
                                    servicioEmpleados.actualizar(empleado.id, empleado_actualizado)
                                    print("Empleado actualizado")
                                else:
                                    print("Empleado no encontrado.")

                            elif opcion == "5":#eliminar empleados
                                empleado = servicioGenerico.buscar(EmpleadosDTO.ingresar_identificacion())

                                if empleado:
                                    servicioGenerico.borrar(empleado.identificacion)

                                    print("Empleado eliminado exitosamente.")
                                else:
                                    print("Empleado no encontrado.")
                            
                            elif opcion == "6":#volver al sistema contador
                                break
                            
                            else:
                                print("Opción inválida. Por favor, seleccione una opción válida.")
                     
                    elif opcion == "2":#rol de pagos

                        print("----Rol de pagos-----")

                        while True:
                            empleado = servicioGenerico.buscar(EmpleadosDTO.ingresar_identificacion())

                            if empleado:

                                EmpleadosDTO.imprimir_personal(empleado)
                                #ingresa datos el contador
                                (
                                    mes,
                                    fecha_corte,
                                    hrs_cien_por_ciento_trabajadas,
                                    hrs_cincuenta_por_ciento_trabajadas,
                                    bono_alimentacion,
                                    bono_transporte,
                                    dias_vacaciones,
                                    sbu,
                                    comisiones,
                                    hra_trabajo_por_mes,
                                    dias_laborados
                                ) = RolDePagos.ingresar_datos()
                                #datos egreso
                                (
                                    anticipos,
                                    prestamo_interno,
                                    multa,
                                    comisariato,
                                    seguro_privado,
                                    otros_descuentos,
                                    impuesto_renta,
                                    prestamo_quirografario,
                                    prestamo_hipotecario,
                                ) = RolDePagos.egresos()
                                #formulas
                                sueldo = RolDePagos.calcular_sueldo(empleado.sueldo_base, dias_laborados)
                                hrs_suplementarias_100 = RolDePagos.horas_suplementaria_100(empleado.sueldo_base, hrs_cien_por_ciento_trabajadas)
                                hrs_suplementarias_50 = RolDePagos.horas_suplementaria_50(empleado.sueldo_base, hrs_cincuenta_por_ciento_trabajadas)
                                alimentacion = RolDePagos.alimentacion(bono_alimentacion, dias_laborados)
                                transporte = RolDePagos.transporte(bono_transporte, dias_laborados)
                                vacaciones = RolDePagos.vacaciones(dias_vacaciones, empleado.sueldo_base)

                                fondo_reserva_m = RolDePagos.fondo_reserva_m(fecha_corte,
                                                                        empleado.fecha_entrada,
                                                                        empleado.sueldo_base, comisiones,
                                                                        hrs_suplementarias_100,
                                                                        hrs_suplementarias_50)

                                decimo_3ro_mes = RolDePagos.decimo_3ero_m(empleado.sueldo_base,
                                                                       dias_laborados,
                                                                       dias_vacaciones,
                                                                       comisiones,
                                                                       hrs_suplementarias_100,
                                                                       hrs_suplementarias_50)

                                decimo_4to_mes = RolDePagos.decimo_4to_m(sbu,
                                                                         hra_trabajo_por_mes,
                                                                         dias_laborados,
                                                                         dias_vacaciones,)
                                iess = RolDePagos.iess(sueldo,
                                                       comisiones,
                                                       hrs_suplementarias_100,
                                                       hrs_suplementarias_50,
                                                       vacaciones)
                                
                                total_ingresos = RolDePagos.total_ingresos(
                                                                           sueldo,
                                                                           comisiones,
                                                                           hrs_suplementarias_100,
                                                                           hrs_suplementarias_50,
                                                                           alimentacion,
                                                                           transporte,
                                                                           vacaciones,
                                                                           fondo_reserva_m,
                                                                           decimo_3ro_mes,
                                                                           decimo_4to_mes)
                                
                                total_egresos = RolDePagos.total_egresos(iess,
                                                                         anticipos,
                                                                         prestamo_interno,
                                                                         multa,
                                                                         comisariato,
                                                                         seguro_privado,
                                                                         otros_descuentos,
                                                                         impuesto_renta,
                                                                         prestamo_quirografario,
                                                                         prestamo_hipotecario)

                                total_recibir = RolDePagos.total_recibir(total_ingresos, total_egresos)
                                
                                
                                RolDePagos.imprimir_todo(mes,
                                                         fecha_corte,
                                                         empleado.identificacion,
                                                         empleado.fecha_entrada,
                                                         empleado.nombre,
                                                         empleado.sueldo_base,
                                                         empleado.cargo,
                                                         dias_laborados,
                                                         hrs_cien_por_ciento_trabajadas,
                                                         hrs_cincuenta_por_ciento_trabajadas,
                                                         bono_alimentacion,
                                                         bono_transporte,
                                                         dias_vacaciones,
                                                         sbu,
                                                         hra_trabajo_por_mes,
                                                         sueldo,
                                                         comisiones,
                                                         hrs_suplementarias_100,
                                                         hrs_suplementarias_50,
                                                         alimentacion,
                                                         transporte,
                                                         vacaciones,
                                                         fondo_reserva_m,
                                                         decimo_3ro_mes,
                                                         decimo_4to_mes,
                                                         iess,
                                                         anticipos,
                                                         prestamo_interno,
                                                         multa,
                                                         comisariato,
                                                         seguro_privado,
                                                         otros_descuentos,
                                                         impuesto_renta,
                                                         prestamo_quirografario,
                                                         prestamo_hipotecario,
                                                         total_ingresos,
                                                         total_egresos,
                                                         total_recibir
                                                        )

                                break
                            else:
                                os.system('cls')
                                print("empleado no encontrado.")
                                break
                    
                    elif opcion == "3":
                        break

                    else:
                        os.system('cls')
        else:
            print("Credenciales incorrectas o usuario no encontrado. Inténtelo nuevamente.")

if __name__ == "__main__":
    db = Database(DATABASE_URL)
    engine = db.engine
    BaseDeDatos.metadata.create_all(bind=engine)
    main()