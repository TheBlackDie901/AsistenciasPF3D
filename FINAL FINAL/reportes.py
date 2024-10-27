from fpdf import FPDF

# Inicializa el PDF
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)

# Título del documento
pdf.cell(200, 10, "Documentación del Sistema de Registro de Asistencia", ln=True, align="C")

# Descripción general
pdf.ln(10)
pdf.cell(200, 10, "Descripción General", ln=True, align="L")
pdf.multi_cell(0, 10, "Este sistema permite gestionar el registro de usuarios y el control de asistencia de profesores en una base de datos SQLite.")

# Descripción de cada función
pdf.ln(10)
pdf.cell(200, 10, "1. Funciones del Sistema", ln=True, align="L")

# Documentación de la función conectar()
pdf.ln(5)
pdf.cell(200, 10, "1.1 conectar()", ln=True, align="L")
pdf.multi_cell(0, 10, "Esta función establece una conexión con la base de datos 'asistencia.db' y la devuelve. Es usada en las demás funciones para interactuar con la base de datos.")

# Documentación de la función crear_tablas()
pdf.ln(5)
pdf.cell(200, 10, "1.2 crear_tablas()", ln=True, align="L")
pdf.multi_cell(0, 10, "Crea las tablas necesarias en la base de datos: 'usuarios' y 'asistencia_profesores'. Si las tablas ya existen, no realiza ningún cambio.")

# Documentación de la función crear_usuario()
pdf.ln(5)
pdf.cell(200, 10, "1.3 crear_usuario(nombre, rol, correo, contrasena)", ln=True, align="L")
pdf.multi_cell(0, 10, "Permite crear un nuevo usuario en la base de datos con los campos 'nombre', 'rol', 'correo' y 'contrasena'. Antes de crear el usuario, verifica que el correo no esté ya registrado.")

# Documentación de la función registrar_asistencia_profesor()
pdf.ln(5)
pdf.cell(200, 10, "1.4 registrar_asistencia_profesor(profesor, dia_semana, hora_inicio, presente)", ln=True, align="L")
pdf.multi_cell(0, 10, "Registra la asistencia de un profesor en la tabla 'asistencia_profesores' con los detalles del día, hora de inicio, y si estuvo presente o no.")

# Documentación de la función obtener_usuario()
pdf.ln(5)
pdf.cell(200, 10, "1.5 obtener_usuario(correo, contrasena)", ln=True, align="L")
pdf.multi_cell(0, 10, "Busca un usuario en la base de datos según el correo y contraseña proporcionados. Si encuentra coincidencia, devuelve los datos del usuario.")

# Guardar el PDF
pdf.output("Documentacion_Sistema_Asistencia.pdf")
