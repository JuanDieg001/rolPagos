from typing import Generic, TypeVar
from accessData.conexionOrm import Database
from sqlalchemy.orm import joinedload
from sqlalchemy.exc import NoResultFound
from datetime import datetime
import os



T = TypeVar('T')

class GenericRepository(Generic[T]):
    
    def __init__(self, model: T,  database: Database):
        self.model = model
        self.db = database

    def crear(self, **kwargs):
        instance = self.model(**kwargs)
        session = self.db.get_session()
        session.add(instance)
        session.commit()
        session.refresh(instance)
        session.close()
        return instance
    

    def buscarTodo(self):
        session = self.db.get_session()
        instance = session.query(self.model).all()
        session.close()
        return instance
    

    def buscar(self, identificacion):
        session = self.db.get_session()
        instance = session.query(self.model).filter_by(identificacion=identificacion).first()
        session.close()
        return instance
        
    
    
    def actualizar(self, id, obj_data) -> T:
        session = self.db.get_session()
        obj = session.query(self.model).get(id)

        if obj:
            for var, value in vars(obj_data).items():
                if hasattr(obj, var):
                    setattr(obj, var, value)            
            print('obj listo para update')
            print(vars(obj_data))
            session.commit()
            session.refresh(obj)
        else:
            print(f"Objeto con id {id} no encontrado.")
        
        session.close()
        return obj

    def borrar(self, identificacion):
        session = self.db.get_session()
        instance = self.buscar(identificacion)
        session.delete(instance)
        session.commit()

class ServiciosEmpleados(Generic[T]):

    def __init__(self, model: T,  database: Database):
        self.model = model
        self.db = database

    def actualizar(self, id, obj_data) -> T:
        session = self.db.get_session()
        obj = session.query(self.model).get(id)
        if obj:
            obj.nombre = obj_data.nombre
            obj.cargo = obj_data.cargo
            obj.fecha_entrada = obj_data.fecha_entrada
            obj.sueldo_base = obj_data.sueldo
            obj.identificacion = obj_data.identificacion
            session.commit()
            session.refresh(obj)
        session.close()
        return obj
    
    
class ServiciosUsuarios(Generic[T]):

    def __init__(self, model: T,  database: Database):
        self.model = model
        self.db = database

    def actualizar(self, id, obj_data) -> T:
        session = self.db.get_session()
        obj = session.query(self.model).get(id)
        if obj:
            obj.nombre = obj_data.nombre
            obj.cargo = obj_data.cargo
            obj.fecha_entrada = obj_data.fecha_entrada
            obj.identificacion = obj_data.identificacion
            obj.clave = obj_data.clave
            session.commit()
            session.refresh(obj)
        session.close()
        return obj

    def login(self, nombre_usuario: str, clave: str) -> bool:
        session = self.db.get_session()
        try:
            user = session.query(self.model).filter_by(nombre=nombre_usuario).first()
            if user:
                if user.clave == clave:
                    return user
        except NoResultFound:
            pass
        finally:
            session.close()
        return False

class RolDePagos:
    
    @staticmethod
    def ingresar_datos():
        while True:
            # Sección: Ingreso de datos generales
            mes = input("Ingrese el mes: ")
            
            # Sección: Fecha de corte (con validación de formato)
            while True:
                fechaStr = input("Ingrese la fecha de corte (año-mes-día): ")
                try:
                    fecha_corte = datetime.strptime(fechaStr, "%Y-%m-%d").date()
                    break
                except ValueError:
                    print(" X Formato incorrecto. Por favor, use el formato año-mes-día.")

            # Sección: Ingreso de horas y bonificaciones
            hrs_cien_por_ciento_trabajadas = int(input("Ingrese las horas 100% trabajadas: "))
            hrs_cincuenta_por_ciento_trabajadas = int(input("Ingrese las horas 50% trabajadas: "))
            
            # Sección: Bonos
            bono_alimentacion = float(input("Ingrese el bono de alimentación: "))
            bono_transporte = float(input("Ingrese el bono de transporte: "))
            
            # Sección: Otros datos
            dias_vacaciones = int(input("Ingrese días de vacaciones: "))
            sbu = float(input("Ingrese el salario básico unificado: "))
            comisiones = float(input("Ingrese las comisiones: "))
            hra_trabajo_por_mes = float(input("Ingrese las horas trabajadas por mes: "))
            dias_laborados = int(input("Ingrese los días laborados: "))
            os.system('cls')
            # Mostrar datos ingresados para confirmación
            print("\n----- Datos Ingresados -----")
            print(f"Mes: {mes}")
            print(f"Fecha de corte: {fecha_corte}")
            print(f"Horas 100% trabajadas: {hrs_cien_por_ciento_trabajadas}")
            print(f"Horas 50% trabajadas: {hrs_cincuenta_por_ciento_trabajadas}")
            print(f"Bono de alimentación: ${bono_alimentacion:.2f}")
            print(f"Bono de transporte: ${bono_transporte:.2f}")
            print(f"Días de vacaciones: {dias_vacaciones}")
            print(f"SBU: ${sbu:.2f}")
            print(f"Comisiones: ${comisiones:.2f}")
            print(f"Horas de trabajo por mes: {hra_trabajo_por_mes}")
            print(f"dias laborados: {dias_laborados}")
            print("----------------------------\n")
            
            # Confirmación de los datos ingresados
            confirmacion = input("¿Los datos ingresados son correctos? (S/N): ").strip().lower()
            if confirmacion == 's':
                return (
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
                )
            else:
                print("Vamos a volver a ingresar los datos...\n")

    @staticmethod
    def egresos():
        os.system('cls')
        # Preguntar si tiene egresos que ingresar
        desea_ingresar = input("¿Desea ingresar egresos? (S/N): ").strip().lower()
        
        if desea_ingresar == 'n':
            # Mostrar los valores que se establecerán en 0
            anticipos = 0.0
            prestamo_interno = 0.0
            multa = 0.0
            comisariato = 0.0
            seguro_privado = 0.0
            otros_descuentos = 0.0
            impuesto_renta = 0.0
            prestamo_quirografario = 0.0
            prestamo_hipotecario = 0.0
            
            print("\n----- Datos de Egresos que se establecerán en 0 -----")
            print(f"Anticipo: ${anticipos:.2f}")
            print(f"Préstamo interno: ${prestamo_interno:.2f}")
            print(f"Multa: ${multa:.2f}")
            print(f"Comisariato: ${comisariato:.2f}")
            print(f"Seguro privado: ${seguro_privado:.2f}")
            print(f"Otros descuentos: ${otros_descuentos:.2f}")
            print(f"Impuesto a la renta: ${impuesto_renta:.2f}")
            print(f"Préstamo quirografario: ${prestamo_quirografario:.2f}")
            print(f"Préstamo hipotecario: ${prestamo_hipotecario:.2f}")
            print("-------------------------------------------------------\n")

            # Preguntar confirmación para establecer en 0
            confirmacion = input("¿Está seguro que desea establecer todos los egresos en 0? (S/N): ").strip().lower()
            if confirmacion == 's':
                return (
                    anticipos,
                    prestamo_interno,
                    multa,
                    comisariato,
                    seguro_privado,
                    otros_descuentos,
                    impuesto_renta,
                    prestamo_quirografario,
                    prestamo_hipotecario
                )
            else:
                # Si el usuario no está seguro, se vuelve a preguntar
                return RolDePagos.egresos()

        while True:
            os.system('cls')
            # Ingreso de datos de egresos
            anticipos = float(input("Ingrese el anticipo: "))
            prestamo_interno = float(input("Ingrese el préstamo interno: "))
            multa = float(input("Ingrese la multa: "))
            comisariato = float(input("Ingrese el comisariato: "))
            seguro_privado = float(input("Ingrese el seguro privado: "))
            otros_descuentos = float(input("Ingrese otros descuentos: "))
            impuesto_renta = float(input("Ingrese el impuesto a la renta: "))
            prestamo_quirografario = float(input("Ingrese el préstamo quirografario: "))
            prestamo_hipotecario = float(input("Ingrese el préstamo hipotecario: "))
            
            os.system('cls')
            # Mostrar datos ingresados para confirmación
            print("\n----- Datos de Egresos Ingresados -----")
            print(f"Anticipo: ${anticipos:.2f}")
            print(f"Préstamo interno: ${prestamo_interno:.2f}")
            print(f"Multa: ${multa:.2f}")
            print(f"Comisariato: ${comisariato:.2f}")
            print(f"Seguro privado: ${seguro_privado:.2f}")
            print(f"Otros descuentos: ${otros_descuentos:.2f}")
            print(f"Impuesto a la renta: ${impuesto_renta:.2f}")
            print(f"Préstamo quirografario: ${prestamo_quirografario:.2f}")
            print(f"Préstamo hipotecario: ${prestamo_hipotecario:.2f}")
            print("-----------------------------------------\n")

            # Confirmación de los datos ingresados
            confirmacion = input("¿Los datos de egresos ingresados son correctos? (S/N): ").strip().lower()
            if confirmacion == 's':
                return (
                    anticipos,
                    prestamo_interno,
                    multa,
                    comisariato,
                    seguro_privado,
                    otros_descuentos,
                    impuesto_renta,
                    prestamo_quirografario,
                    prestamo_hipotecario
                )
            else:
                print("Vamos a volver a ingresar los datos de egresos...\n")

    @staticmethod 
    def calcular_sueldo(sueldo_base, dias_laborados):
        return (sueldo_base/30)*dias_laborados

    @staticmethod
    def horas_suplementaria_100(sueldo_base, hrs_cien_por_ciento_trabajadas):
        return (((sueldo_base / 240) * 1) + (sueldo_base / 240)) * hrs_cien_por_ciento_trabajadas
    
    @staticmethod
    def horas_suplementaria_50(sueldo_base, hrs_cincuenta_por_ciento_trabajadas):
        return (((sueldo_base / 240) * 0.5) + (sueldo_base / 240)) * hrs_cincuenta_por_ciento_trabajadas

    @staticmethod
    def alimentacion(bono_alimentacion, dias_laborados):
        return (bono_alimentacion/30)*dias_laborados
    
    @staticmethod
    def transporte(bono_transporte, dias_laborados):
        return (bono_transporte/30)*dias_laborados
    
    @staticmethod
    def vacaciones(dias_vacaciones, sueldo_base):
        return (sueldo_base/30)*dias_vacaciones
    
    @staticmethod
    def fondo_reserva_m(fecha_corte,
                        fecha_ingreso,
                        sueldo_base,
                        comisiones,
                        horas_suplementaria_100,
                        horas_suplementaria_50):
        
        if (fecha_corte - fecha_ingreso).days > 360:
            resultado = (sueldo_base + comisiones + horas_suplementaria_100 + horas_suplementaria_50) * 0.0833
        else:
            resultado = 0

        return resultado
    
    @staticmethod
    def decimo_3ero_m(sueldo_base,
                    dias_laborados,
                    dias_vacaciones,
                    comisiones,
                    horas_suplementaria_100,
                    horas_suplementaria_50):

        return  (((sueldo_base / 30) * (dias_laborados + dias_vacaciones)) + (comisiones + horas_suplementaria_100 + horas_suplementaria_50)) / 12

    @staticmethod
    def decimo_4to_m(sbu,
                    hra_trabajo_por_mes,
                    dias_laborados,
                    dias_vacaciones,):

        return  ((((sbu / 240) * hra_trabajo_por_mes) / 30) * (dias_laborados + dias_vacaciones)) / 12
    
    @staticmethod
    def total_ingresos(
                        sueldo,
                        comisiones,
                        hrs_suplementarias_100,
                        hrs_suplementarias_50,
                        alimentacion,
                        transporte,
                        vacaciones,
                        fondo_reserva_m,
                        decimo_3ro_mes,
                        decimo_4to_mes
                        ):
        return sueldo + comisiones + hrs_suplementarias_100 + hrs_suplementarias_50 + alimentacion + transporte + vacaciones + fondo_reserva_m + decimo_3ro_mes + decimo_4to_mes

    @staticmethod
    def iess (sueldo,
              comisiones,
              hrs_suplementarias_100,
              hrs_suplementarias_50,
              vacaciones):
        return (sueldo + comisiones + hrs_suplementarias_100 + hrs_suplementarias_50 + vacaciones) * 0.0945

    @staticmethod
    def total_egresos(iess,
                      anticipos,
                      prestamo_interno,
                      multa,
                      comisariato,
                      seguro_privado,
                      otros_descuentos,
                      impuesto_renta,
                      prestamo_quirografario,
                      prestamo_hipotecario):
        
        return iess + anticipos + prestamo_interno + multa + comisariato + seguro_privado + otros_descuentos + impuesto_renta + prestamo_quirografario + prestamo_hipotecario

    @staticmethod
    def total_recibir(total_ingresos, total_egresos):
        return total_ingresos-total_egresos

    @staticmethod 
    def imprimir_todo(
                    mes,
                    fecha_corte,
                    identificacion,
                    fecha_entrada,
                    nombre,
                    sueldo_base,
                    cargo,
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
                    ):
        os.system('cls')
        
        # Listas de ingresos y egresos
        ingresos = [
            ("Sueldo", sueldo),
            ("Comisiones y bonificaciones", comisiones),
            ("Horas suplementarias 100%", hrs_suplementarias_100),
            ("Horas suplementarias 50%", hrs_suplementarias_50),
            ("Alimentación", alimentacion),
            ("Transporte", transporte),
            ("Vacaciones", vacaciones),
            ("Fondos de reserva mensualizado", fondo_reserva_m),
            ("Décimo tercero mensualizado", decimo_3ro_mes),
            ("Décimo cuarto mensualizado", decimo_4to_mes)
        ]
        
        egresos = [
        ("IESS 9.45% (aporte personal)", iess),
        ("Anticipos", anticipos),
        ("Préstamo interno", prestamo_interno),
        ("Multas", multa),
        ("Comisariato", comisariato),
        ("Seguro privado", seguro_privado),
        ("Otros descuentos", otros_descuentos),
        ("Impuesto a la renta", impuesto_renta),
        ("Préstamo quirografario", prestamo_quirografario),
        ("Préstamo hipotecario", prestamo_hipotecario)
        ]
        
        
        # Imprimir información del empleado y detalles
        print(f"Mes: {mes:<25} {'Fecha de corte:':<25} {fecha_corte}")
        print(f"CI: {identificacion:<26} {'Fecha de ingreso:':<25} {fecha_entrada}")
        print(f"Nombre: {nombre:<22} {'Sueldo base:':<25} {sueldo_base:.2f}")
        print(f"Cargo: {cargo:<23} {'Días laborados:':<25} {dias_laborados}")
        print()
        print()
        print(f"horas s 100%:         {hrs_cien_por_ciento_trabajadas:<5}")
        print(f"horas s 50%:          {hrs_cincuenta_por_ciento_trabajadas:<5}")
        print(f"bono alimentacion:    {bono_alimentacion:<5}")
        print(f"bono transporte:      {bono_transporte:<5}")
        print(f"dias de vacaciones:   {dias_vacaciones:<5}")
        print(f"sbu:                  {sbu:<5}")
        print(f"hrs trabajo x mes:    {hra_trabajo_por_mes:<5}")
        print()
        print()
        # Encabezados de ingresos y egresos
        print(f"{'INGRESOS':<54} {'EGRESOS'}")
        print("="*96)

        # Imprimir ingresos y egresos en columnas
        for i in range(max(len(ingresos), len(egresos))):
            ingreso_str = f"{ingresos[i][0]:<40} {ingresos[i][1]:>10.2f}" if i < len(ingresos) else ""
            egreso_str = f"{egresos[i][0]:<30} {egresos[i][1]:>10.2f}" if i < len(egresos) else ""
            print(f"{ingreso_str}    {egreso_str}")
        
        # Imprimir totales
        print()
        print(f"{'Total ingresos:':<40} {total_ingresos:>10.2f}")
        print(f"{'Total egresos:':<40} {total_egresos:>10.2f}")
        print(f"{'TOTAL A RECIBIR:':<40} {total_recibir:>10.2f}")
        input("Presiona 'Enter' para limpiar la consola...")
                


class ArtilugiosDelSistema:
    
    @staticmethod
    def limpiar_consola():
        os.system('cls' if os.name == 'nt' else 'clear')

    @staticmethod
    def mostrar_bienvenida(nombre, cargo):
        # Imprimir el resultado directamente en el print
        print("-" * 50)
        print(f"{'Bienvenido al sistema (' + cargo + ' : ' + nombre + ')':^50}")
        print("-" * 50)

    @staticmethod
    def menu_admin():
            print("╔════════════════════════════╗")
            print("║       MENÚ PRINCIPAL       ║")
            print("╠════════════════════════════╣")
            print("║  1. Gestión Empleados      ║")
            print("║  2. Gestión Usuarios       ║")
            print("║  3. Salir                  ║")
            print("╚════════════════════════════╝")

    @staticmethod
    def menu_contador():
            print("╔════════════════════════════╗")
            print("║       MENÚ PRINCIPAL       ║")
            print("╠════════════════════════════╣")
            print("║  1. Gestión Empleados      ║")
            print("║  2. Rol de Pagos           ║")
            print("║  3. Salir                  ║")
            print("╚════════════════════════════╝")

    @staticmethod
    def menu_empleados():
            print("╔════════════════════════════╗")
            print("║       MENÚ PRINCIPAL       ║")
            print("╠════════════════════════════╣")
            print("║  1. Ingresar Empleado      ║")
            print("║  2. Lista Empleados        ║")
            print("║  3. Buscar Empleado        ║")
            print("║  4. Actualizar Empleado    ║")
            print("║  5. Eliminar Empleado      ║")
            print("║  6. Volver Menu Principal  ║")
            print("╚════════════════════════════╝")
    
