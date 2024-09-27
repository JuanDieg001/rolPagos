from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

def generar_pdf(mes, fecha_corte, identificacion, fecha_entrada, nombre, sueldo_base, cargo, dias_laborados,
                hrs_cien_por_ciento_trabajadas, hrs_cincuenta_por_ciento_trabajadas, bono_alimentacion, bono_transporte,
                dias_vacaciones, sbu, hra_trabajo_por_mes, sueldo, comisiones, hrs_suplementarias_100, hrs_suplementarias_50,
                alimentacion, transporte, vacaciones, fondo_reserva_m, decimo_3ro_mes, decimo_4to_mes, iess, anticipos,
                prestamo_interno, multa, comisariato, seguro_privado, otros_descuentos, impuesto_renta,
                prestamo_quirografario, prestamo_hipotecario, total_ingresos, total_egresos, total_recibir):
    
    # Crear el archivo PDF
    archivo_pdf = "Rol_de_Pagos.pdf"
    c = canvas.Canvas(archivo_pdf, pagesize=A4)
    
    # Ajustar la fuente y el tamaño
    c.setFont("Helvetica", 10)

    # Título
    c.drawString(200, 800, "ROL DE PAGO")

    # Primera sección
    c.drawString(50, 780, f"Mes: {mes}")
    c.drawString(350, 780, f"Fecha de corte: {fecha_corte}")
    c.drawString(50, 760, f"CI: {identificacion}")
    c.drawString(350, 760, f"Fecha de ingreso: {fecha_entrada}")
    c.drawString(50, 740, f"Nombre: {nombre}")
    c.drawString(350, 740, f"Sueldo base: {sueldo_base:.2f}")
    c.drawString(50, 720, f"Cargo: {cargo}")
    c.drawString(350, 720, f"Días laborados: {dias_laborados}")

    # Segunda sección (Horas y bonos)
    c.drawString(50, 700, f"horas s 100%: {hrs_cien_por_ciento_trabajadas}")
    c.drawString(50, 680, f"horas s 50%: {hrs_cincuenta_por_ciento_trabajadas}")
    c.drawString(50, 660, f"bono alimentacion: {bono_alimentacion}")
    c.drawString(50, 640, f"bono transporte: {bono_transporte}")
    c.drawString(50, 620, f"dias de vacaciones: {dias_vacaciones}")
    c.drawString(50, 600, f"sbu: {sbu}")
    c.drawString(50, 580, f"hrs trabajo x mes: {hra_trabajo_por_mes}")

    # Ingresos
    c.drawString(50, 560, "INGRESOS")
    c.drawString(50, 540, f"Sueldo: {sueldo:.2f}")
    c.drawString(50, 520, f"Comisiones: {comisiones:.2f}")
    c.drawString(50, 500, f"Horas suplementarias 100%: {hrs_suplementarias_100:.2f}")
    c.drawString(50, 480, f"Horas suplementarias 50%: {hrs_suplementarias_50:.2f}")
    c.drawString(50, 460, f"Alimentación: {alimentacion:.2f}")
    c.drawString(50, 440, f"Transporte: {transporte:.2f}")
    c.drawString(50, 420, f"Vacaciones: {vacaciones:.2f}")
    c.drawString(50, 400, f"Fondo de reserva mensualizado: {fondo_reserva_m:.2f}")
    c.drawString(50, 380, f"Décimo tercero mensualizado: {decimo_3ro_mes:.2f}")
    c.drawString(50, 360, f"Décimo cuarto mensualizado: {decimo_4to_mes:.2f}")

    c.drawString(50, 340, f"Total ingresos: {total_ingresos:.2f}")

    # Egresos
    c.drawString(300, 560, "EGRESOS")
    c.drawString(300, 540, f"IESS 9.45% (aporte personal): {iess:.2f}")
    c.drawString(300, 520, f"Anticipos: {anticipos:.2f}")
    c.drawString(300, 500, f"Préstamo interno: {prestamo_interno:.2f}")
    c.drawString(300, 480, f"Multa: {multa:.2f}")
    c.drawString(300, 460, f"Comisariato: {comisariato:.2f}")
    c.drawString(300, 440, f"Seguro privado: {seguro_privado:.2f}")
    c.drawString(300, 420, f"Otros descuentos: {otros_descuentos:.2f}")
    c.drawString(300, 400, f"Impuesto a la renta: {impuesto_renta:.2f}")
    c.drawString(300, 380, f"Préstamo quirografario: {prestamo_quirografario:.2f}")
    c.drawString(300, 360, f"Préstamo hipotecario: {prestamo_hipotecario:.2f}")

    c.drawString(300, 340, f"Total egresos: {total_egresos:.2f}")

    # Total a recibir
    c.drawString(50, 300, f"TOTAL A RECIBIR: {total_recibir:.2f}")

    # Guardar el PDF
    c.showPage()
    c.save()
    
    print(f"PDF generado: {archivo_pdf}")

# Llamar a la función con tus variables
generar_pdf(mes="OCTUBRE", fecha_corte="31/01/2024", identificacion="1720596152", fecha_entrada="15/01/2023",
            nombre="Juan Granada", sueldo_base=500.00, cargo="Programador", dias_laborados=24,
            hrs_cien_por_ciento_trabajadas=16, hrs_cincuenta_por_ciento_trabajadas=5, bono_alimentacion=100,
            bono_transporte=50, dias_vacaciones=6, sbu=460, hra_trabajo_por_mes=120, sueldo=450.00,
            comisiones=20.00, hrs_suplementarias_100=66.67, hrs_suplementarias_50=15.63, alimentacion=80.00,
            transporte=40.00, vacaciones=100.00, fondo_reserva_m=50.17, decimo_3ro_mes=50.19, decimo_4to_mes=19.17,
            iess=56.92, anticipos=100.00, prestamo_interno=10.00, multa=20.00, comisariato=10.00, seguro_privado=10.00,
            otros_descuentos=10.00, impuesto_renta=50.00, prestamo_quirografario=50.00, prestamo_hipotecario=50.00,
            total_ingresos=891.83, total_egresos=366.92, total_recibir=524.91)


