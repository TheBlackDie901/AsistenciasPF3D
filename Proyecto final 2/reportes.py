from fpdf import FPDF
import database as db

def generar_reporte_profesor(profesor_id):
    registros = db.obtener_asistencia_por_profesor(profesor_id)
    
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(200, 10, 'Reporte de Asistencia', ln=True, align='C')
    pdf.ln(10)
    
    pdf.set_font('Arial', 'B', 12)
    pdf.cell(50, 10, 'Materia', 1)
    pdf.cell(50, 10, 'Fecha', 1)
    pdf.cell(50, 10, 'Asistencia', 1)
    pdf.ln()

    for registro in registros:
        pdf.cell(50, 10, registro[0], 1)
        pdf.cell(50, 10, registro[1], 1)
        pdf.cell(50, 10, "Sí" if registro[2] else "No", 1)
        pdf.ln()

    pdf.output(f'reporte_profesor_{profesor_id}.pdf')
