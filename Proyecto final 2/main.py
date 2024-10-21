import streamlit as st
import database as db

# Crear tablas
db.crear_tablas()

# Crear usuarios
if db.obtener_usuario("admin@escuela.com", "admin123") is None:
    db.crear_usuario("Admin", "admin", "admin@escuela.com", "admin123")
    
if db.obtener_usuario("walter@escuela.com", "walter123") is None:
    db.crear_usuario("Walter", "maestro", "walter@escuela.com", "walter123")
    
if db.obtener_usuario("alumno@escuela.com", "alumno123") is None:
    db.crear_usuario("Carlos López", "alumno", "alumno@escuela.com", "alumno123")

# login
def login(correo, contrasena):
    return db.obtener_usuario(correo, contrasena)

# Menú de administrador
def admin_menu():
    st.header("Panel de Administrador")
    opcion = st.selectbox("Elija una opción", ["Añadir Profesor", "Añadir Materia", "Añadir Horario", "Añadir Grupo", 
                                               "Consultar/Modificar Profesores", "Consultar/Modificar Alumnos", 
                                               "Consultar/Modificar Grupos", "Consultar/Modificar Materias", 
                                               "Consultar/Modificar Asistencias"])

    if opcion == "Añadir Profesor":
        nombre = st.text_input("Nombre del Profesor")
        carrera = st.text_input("Carrera")
        if st.button("Guardar Profesor"):
            db.insertar_profesor(nombre, carrera)
            st.success("Profesor guardado exitosamente")
    
    elif opcion == "Añadir Materia":
        nombre = st.text_input("Nombre de la Materia")
        profesores = db.obtener_profesores()
        profesor = st.selectbox("Seleccione un Profesor", [p[1] for p in profesores])
        profesor_id = [p[0] for p in profesores if p[1] == profesor][0]
        carrera = st.text_input("Carrera")
        if st.button("Guardar Materia"):
            db.insertar_materia(nombre, profesor_id, carrera)
            st.success("Materia guardada exitosamente")
    
    elif opcion == "Añadir Horario":
        grupos = db.obtener_grupos()
        grupo = st.selectbox("Seleccione un Grupo", [g[1] for g in grupos])
        grupo_id = [g[0] for g in grupos if g[1] == grupo][0]
        
        materias = db.obtener_materias()
        materia = st.selectbox("Seleccione una Materia", [m[1] for m in materias])
        materia_id = [m[0] for m in materias if m[1] == materia][0]
        
        profesores = db.obtener_profesores()
        profesor = st.selectbox("Seleccione un Profesor", [p[1] for p in profesores])
        profesor_id = [p[0] for p in profesores if p[1] == profesor][0]
        
        dia_semana = st.text_input("Día de la Semana")
        hora_inicio = st.text_input("Hora de Inicio (HH:MM)")
        hora_fin = st.text_input("Hora de Fin (HH:MM)")
        if st.button("Guardar Horario"):
            db.insertar_horario(grupo_id, materia_id, profesor_id, dia_semana, hora_inicio, hora_fin)
            st.success("Horario guardado exitosamente")

    elif opcion == "Añadir Grupo":
        nombre = st.text_input("Nombre del Grupo")
        if st.button("Guardar Grupo"):
            db.insertar_grupo(nombre)
            st.success("Grupo guardado exitosamente")
    
    # Consultar/Modificar Profesores
    elif opcion == "Consultar/Modificar Profesores":
        profesores = db.obtener_profesores()
        if profesores:
            profesor_seleccionado = st.selectbox("Seleccione un Profesor", [p[1] for p in profesores])
            profesor_id = [p[0] for p in profesores if p[1] == profesor_seleccionado][0]
            nuevo_nombre = st.text_input("Nuevo Nombre", value=profesor_seleccionado)
            nueva_carrera = st.text_input("Nueva Carrera")
            
            if st.button("Modificar Profesor"):
                db.modificar_profesor(profesor_id, nuevo_nombre, nueva_carrera)
                st.success("Profesor modificado exitosamente")

            if st.button("Eliminar Profesor"):
                db.eliminar_profesor(profesor_id)
                st.success("Profesor eliminado exitosamente")
        else:
            st.warning("No hay profesores disponibles.")
    
    # Consultar/Modificar Grupos
    elif opcion == "Consultar/Modificar Grupos":
        grupos = db.obtener_grupos()
        if grupos:
            grupo_seleccionado = st.selectbox("Seleccione un Grupo", [g[1] for g in grupos])
            grupo_id = [g[0] for g in grupos if g[1] == grupo_seleccionado][0]
            nuevo_nombre = st.text_input("Nuevo Nombre del Grupo", value=grupo_seleccionado)
            
            if st.button("Modificar Grupo"):
                db.modificar_grupo(grupo_id, nuevo_nombre)
                st.success("Grupo modificado exitosamente")

            if st.button("Eliminar Grupo"):
                db.eliminar_grupo(grupo_id)
                st.success("Grupo eliminado exitosamente")
        else:
            st.warning("No hay grupos disponibles.")
    
    # Consultar/Modificar Asistencias
    elif opcion == "Consultar/Modificar Asistencias":
        asistencias = db.obtener_asistencias()
        if asistencias:
            asistencia_seleccionada = st.selectbox("Seleccione una Asistencia", [f"ID: {a[0]}" for a in asistencias])
            asistencia_id = [a[0] for a in asistencias if f"ID: {a[0]}" == asistencia_seleccionada][0]
            nueva_asistencia = st.checkbox("Clase Impartida", value=asistencias[asistencia_id-1][1])

            if st.button("Modificar Asistencia"):
                db.modificar_asistencia(asistencia_id, nueva_asistencia)
                st.success("Asistencia modificada exitosamente")
        else:
            st.warning("No hay asistencias disponibles.")

# Menú de maestro
def maestro_menu(usuario):
    st.header(f"Panel de Maestro - {usuario[1]}")
    materias = db.obtener_materias()
    materia_seleccionada = st.selectbox("Seleccione una Materia", [m[1] for m in materias])
    materia_id = [m[0] for m in materias if m[1] == materia_seleccionada][0]
    
    alumnos = db.obtener_alumnos()
    alumno_seleccionado = st.multiselect("Seleccione los alumnos presentes", [a[1] for a in alumnos])
    alumnos_presentes = [a[0] for a in alumnos if a[1] in alumno_seleccionado]
    
    if st.button("Registrar Asistencia"):
        for alumno_id in alumnos_presentes:
            db.registrar_asistencia(usuario[0], materia_id, True)
        st.success("Asistencia registrada exitosamente")

# Panel del alumno
def alumno_menu(usuario):
    st.header(f"Panel de Alumno - {usuario[1]}")
    asistencias = db.obtener_asistencias_por_alumno(usuario[0])
    if asistencias:
        for asistencia in asistencias:
            st.write(f"Materia: {asistencia[1]} - Asistencia: {'Sí' if asistencia[2] else 'No'}")
    else:
        st.warning("No hay asistencias registradas para mostrar.")

# Sistema ogin
if 'usuario' not in st.session_state:
    st.session_state['usuario'] = None

if st.session_state['usuario'] is None:
    st.title("Sistema de Gestión de Asistencias")

    correo = st.text_input("Correo")
    contrasena = st.text_input("Contraseña", type="password")

    if st.button("Iniciar sesión"):
        usuario = login(correo, contrasena)
        if usuario:
            st.session_state['usuario'] = usuario
            st.set_query_params()
        else:
            st.error("Credenciales incorrectas")
else:
    usuario = st.session_state['usuario']
    st.success(f"Bienvenido {usuario[1]} ({usuario[2]})")

    if usuario[2] == "admin":
        admin_menu()
    elif usuario[2] == "maestro":
        maestro_menu(usuario)
    elif usuario[2] == "alumno":
        alumno_menu(usuario)

# Cerrar sesión
if st.session_state['usuario'] is not None:
    if st.button("Cerrar sesión"):
        st.session_state['usuario'] = None
        st.set_query_params()
