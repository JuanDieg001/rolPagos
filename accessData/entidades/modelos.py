from sqlalchemy import Column, Date, String, Double, Integer, ForeignKey, CheckConstraint
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

BaseDeDatos = declarative_base()

class Empleados(BaseDeDatos):
    
    __tablename__ = 'Empleados'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(50), nullable=False)
    cargo = Column(String(50), nullable=False)
    fecha_entrada = Column((Date), nullable=False)
    identificacion= Column (Integer, nullable=False)
    sueldo_base = Column(Double, nullable=False)

    # Relación uno a muchos con RolDePagos
    roles_de_pagos = relationship("RolDePagos", back_populates="empleado")

    __table_args__ = (
        CheckConstraint('identificacion >= 1 AND identificacion <= 9999999999', name='identificacion_10_digitos'),
    )


class Usuarios(BaseDeDatos):

    __tablename__ = 'Usuarios'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(50), nullable=False)
    cargo = Column(String(50), nullable=False)
    fecha_entrada = Column((Date), nullable=False)
    clave= Column (String(50), nullable=False)
    identificacion= Column (Integer, nullable=False)

    __table_args__ = (
        CheckConstraint('identificacion >= 1 AND identificacion <= 9999999999', name='identificacion_10_digitos'),
    )

class RolDePagos(BaseDeDatos):

    __tablename__ = 'rolDePagos'

    id = Column(Integer, primary_key=True, autoincrement=True)
    #ingreso manual contador
    mes = Column (Date, nullable=False)
    fecha_de_corte = Column (Date, nullable=False)
    dias_laborados = Column(Integer)
    hrs_cien_por_ciento_trabajadas = Column(Integer)
    hrs_cincuenta_por_ciento_trabajadas = Column(Integer)
    bono_alimentacion = Column(Double)
    bono_transporte = Column(Double)
    dias_vacaciones = Column(Integer)
    sbu = Column(Double, nullable=False)#salario basico unificado
    hra_trabajo_por_mes = Column(Double)
    #Ingresos
    sueldo = Column(Double)
    comisiones = Column(Double)
    horas_suplementarias_cien_por_ciento = Column(Double)
    horas_suplementarias_cincuenta_por_ciento = Column(Double)
    alimentacion = Column(Double, nullable=False)
    transporte = Column(Double, nullable=False)
    vacaciones = Column(Double, nullable=False)
    fondos_reserva_mes = Column(Double, nullable=False)
    dec_tercero_mes = Column(Double, nullable=False)
    dec_cuarto_mes = Column(Double, nullable=False)
    total_ingresos = Column(Double, nullable=False)
    #egresos
    iess = Column(Double, nullable=False)
    anticipos = Column(Double, nullable=False)
    prestamo_interno = Column(Double, nullable=False)
    multas = Column(Double, nullable=False)
    comisariato = Column(Double, nullable=False)
    seguro_privado = Column(Double, nullable=False)
    otros_descuentos = Column(Double, nullable=False)
    impuesto_renta = Column(Double, nullable=False)
    prestamo_quirografario = Column(Double, nullable=False)
    prestamo_hipotecario = Column(Double, nullable=False)
    total_egresos = Column(Double, nullable=False)
    #total de todo
    total_recibir = Column(Double, nullable=False)

    # Clave foránea que enlaza con el empleado
    empleado_id = Column(Integer, ForeignKey('Empleados.id'), nullable=False)

    # Relación con la clase Empleados
    empleado = relationship("Empleados", back_populates="roles_de_pagos")

