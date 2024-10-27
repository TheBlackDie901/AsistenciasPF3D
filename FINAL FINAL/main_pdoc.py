"""
Sistema de Gestión de Asistencias

Este script utiliza Streamlit para crear una aplicación web para la gestión de asistencias en diferentes carreras.
Se conecta a una base de datos a través del módulo database, donde se gestionan usuarios, horarios y registros de asistencia.

Módulos Importados:
- streamlit: Para crear la interfaz de usuario de la aplicación web.
- database: Módulo personalizado que gestiona la base de datos.
- datetime: Para manejar las fechas y horas en la aplicación.

"""

import streamlit as st
import database as db
from datetime import datetime, timedelta
import reportes as rp


db.crear_tablas()
'''
Funciones Principales:
- crear_tablas(): Crea las tablas necesarias en la base de datos.
- crear_usuario(nombre, tipo_usuario, correo, contrasena): Crea un nuevo usuario en la base de datos.
- login(correo, contrasena): Valida las credenciales del usuario y retorna su información.
- mostrar_horarios(carrera, dia_semana): Muestra los horarios de clases para una carrera específica en un día determinado.
- admin_menu(usuario): Muestra el menú de administración para el jefe de grupo, donde se selecciona un día y se visualizan los horarios correspondientes.

'''
# Jefes de grupo
'''
Ejemplo de Uso:
1. Al ejecutar la aplicación, se crean las tablas y se añaden los usuarios iniciales.
2. Los usuarios pueden iniciar sesión con su correo y contraseña.
3. Una vez iniciada la sesión, los jefes de grupo pueden seleccionar un día y ver los horarios de sus respectivas carreras.
'''
db.crear_usuario("Miguel Ángel Ortiz Torres", "admin", "Miguel@ucol.mx", "Miguel123")  # ICI
db.crear_usuario("Cesar Eduardo Zepeda Gorrocino", "admin", "Cesar@ucol.mx", "Cesar123")  # IME
db.crear_usuario("Michelle Rosales Sánchez", "admin", "Michelle@ucol.mx", "Michelle123")  # IM
db.crear_usuario("Panfilo Gutierrez Alvarez Diaz","admin","Panfilo@ucol.mx","Panfilo123") #ISET


# ICI
db.crear_usuario("Juan Antonio Diaz Hernández", "maestro", "Juan@ucol.mx", "Juan123")
db.crear_usuario("Walter Alexander Mata López", "maestro", "Walter@ucol.mx", "Walter123")
db.crear_usuario("Carlos Adrián Bricio Chapula", "maestro", "Carlos@ucol.mx", "Carlos123")
db.crear_usuario("Oscar Octavio Ochoa Zúñiga", "maestro", "Oscar@ucol.mx", "Oscar123")
db.crear_usuario("Elizabeth Santiago Hernández", "maestro", "Elizabeth@ucol.mx", "Elizabeth123")
db.crear_usuario("David Alejandro Sierra Andrade", "maestro", "David@ucol.mx", "David123")
db.crear_usuario("Luis Eduardo Moran López", "maestro", "Luis@ucol.mx", "Luis123")

# ISET
db.crear_usuario("Vazquez Gonzales Cruz Ernesto", "maestro", "Vazquez@ucol.mx", "Vazquez123")
db.crear_usuario("Martines Camera Edgar", "maestro", "Edgar@ucol.mx", "Edgar123")
db.crear_usuario("Francisco Manuel Soto Ochoa", "maestro", "Francisco@ucol.mx", "Francisco123")
db.crear_usuario("Luis Daniel Benavides Sanches", "maestro", "LuisBenavides@ucol.mx", "LuisBenavides123")

# IME
db.crear_usuario("Jaime Arroyo Ledesma", "maestro", "Jaime@ucol.mx", "Jaime123")
db.crear_usuario("Pablo Armando Alcaraz Valencia", "maestro", "Pablo@ucol.mx", "Pablo123")
db.crear_usuario("Sergio Llamas Zamorano", "maestro", "Sergio@ucol.mx", "Sergio123")
db.crear_usuario("Selene Cárdenas Rodríguez", "maestro", "Selene@ucol.mx", "Selene123")
db.crear_usuario("José Alberto García Jiménez", "maestro", "Jose@ucol.mx", "Jose123")
db.crear_usuario("Manfredo Paredes Jacquez", "maestro", "Manfredo@ucol.mx", "Manfredo123")

# IM
db.crear_usuario("Laura Stanley Gaytán Lugo", "maestro", "Laura@ucol.mx", "Laura123")
db.crear_usuario("Luis López Moran", "maestro", "LuisLopez@ucol.mx", "LuisLopez123")
db.crear_usuario("Martha Elizabeth Evangelista Salazar", "maestro", "Martha@ucol.mx", "Martha123")
db.crear_usuario("Antonio Alfonso Luis Morales", "maestro", "Antonio@ucol.mx", "Antonio123")
db.crear_usuario("Oswaldo Carrillo Zepeda", "maestro", "Oswaldo@ucol.mx", "Oswaldo123")
db.crear_usuario("Apolinar González Potes", "maestro", "Apolinar@ucol.mx", "Apolinar123")

def login(correo, contrasena):
    '''
    """
    Verifica las credenciales del usuario.

    Args:
        correo (str): Correo electrónico del usuario.
        contrasena (str): Contraseña del usuario.

    Returns:
        tuple: Información del usuario si las credenciales son válidas, None en caso contrario.
    """

    '''
    return db.obtener_usuario(correo, contrasena)

# Horarios 
horarios_ici = {
    '''
    Datos fijos de los maestros con sus horarios y su materias 

    '''
    "Lunes": [("09:15", "11:00", "Métodos Numéricos", "David Alejandro Sierra Andrade"),
              ("11:00", "13:00", "Programación Funcional", "Walter Alexander Mata López")],
    "Martes": [("07:00", "08:40", "Sistemas Digitales Embebidos", "Carlos Adrián Bricio Chapula"),
               ("11:00", "13:00", "Interconexión de Redes", "Juan Antonio Diaz Hernández")],
    "Miércoles": [("07:00", "08:40", "Estructura de Datos", "Luis Eduardo Moran López"),
                 ("10:00", "12:00", "Métodos Numéricos", "David Alejandro Sierra Andrade"),
                 ("12:00", "13:00", "Inglés", "Oscar Octavio Ochoa Zúñiga"),
                 ("13:00", "15:00", "Programación Funcional", "Walter Alexander Mata López")],
    "Jueves": [("07:00", "08:40", "Sistemas Digitales Embebidos", "Carlos Adrián Bricio Chapula"),
               ("09:15", "11:00", "Ecuaciones Diferenciales", "Elizabeth Santiago Hernández"),
               ("11:00", "13:00", "Interconexión de Redes", "Juan Antonio Diaz Hernández"),
               ("13:00", "15:00", "Inglés", "Oscar Octavio Ochoa Zúñiga")],
    "Viernes": [("09:15", "11:00", "Ecuaciones Diferenciales", "Elizabeth Santiago Hernández"),
                ("11:00", "12:00", "Métodos Numéricos", "David Alejandro Sierra Andrade"),
                ("13:00", "15:00", "Estructura de Datos", "Luis Eduardo Moran López")]
}

horarios_iset = {
    "Lunes": [("07:00", "08:40", "Ecuaciones Diferenciales", "Vazquez Gonzales Cruz Ernesto"),
              ("09:15", "11:00", "Programación Funcional", "Walter Alexander Mata López"),
              ("12:00", "14:00", "Inglés", "Luis Daniel Benavides Sanches"),
              ("14:00", "15:00", "Métodos Numéricos", "Martines Camera Edgar")],
    "Martes": [("09:15", "11:00", "Ecuaciones Diferenciales", "Vazquez Gonzales Cruz Ernesto"),
               ("11:00", "12:00", "Inglés", "Luis Daniel Benavides Sanches")],
    "Miércoles": [("08:00", "08:40", "Ecuaciones Diferenciales", "Vazquez Gonzales Cruz Ernesto"),
                  ("10:00", "12:00", "Interconexión de Redes", "Juan Antonio Diaz Hernández"),
                  ("12:00", "14:00", "Métodos Numéricos", "Martines Camera Edgar")],
    "Jueves": [("09:15", "11:00", "Sistemas Digitales Embebidos", "Carlos Adrián Bricio Chapula"),
               ("11:00", "13:00", "Estructuras de Datos", "Francisco Manuel Soto Ochoa"),
               ("13:00", "15:00", "Programación Funcional", "Walter Alexander Mata López")],
    "Viernes": [("07:00", "08:40", "Sistemas Digitales Embebidos", "Carlos Adrián Bricio Chapula"),
                ("09:15", "11:00", "Métodos Numéricos", "Martines Camera Edgar"),
                ("11:00", "13:00", "Interconexión de Redes", "Juan Antonio Diaz Hernández")]
}

horarios_ime = {
    "Lunes":[("07:00", "08:40", "Circuitos" , "José Alberto García Jiménez"),
            ("07:00", "8:40", "Circuitos",  "José Alberto García Jiménez"),
            ("09:15", "11:00", "Tecnología de los Materiales", "Selene Cárdenas Rodríguez"),
            ("12:00", "13:00", "Ecuaciones Diferenciales", "Jaime Arroyo Ledesma")],
    "Martes":[("07:00", "08:40", "Electrónica", "José Alberto García Jiménez"),
              ("9:15", "11:00", "Dinámica",  "Sergio Llamas Zamorano"),
              ("11:00", "13:00", "Métodos Numéricos",  "Pablo Armando Alcaraz Valencia"),
              ("13:00", "14:00", "Ecuaciones Diferenciales",  "Jaime Arroyo Ledesma")],
    "Miércoles":[("10:00", "12:00", "Métodos Numéricos",  "Pablo Armando Alcaraz Valencia")], 
     "Jueves":[("07:00", "08:40", "Circuitos", "José Alberto García Jiménez"),
              ("09:15", "11:02",  "Dinámica",  "Sergio Llamas Zamorano"),
              ("11:00", "13:00",  "Ingles",  "Oscar Octavio Ochoa Zúñiga"),
              ("13:00", "14:00",  "Tecnología de los Materiales", "Selene Cárdenas Rodríguez")],
    "Viernes":[("07:00", "08:40",   "Electrónica",  "José Alberto García Jiménez"),
               ("10:00", "11:00",  "Ingles",  "Oscar Octavio Ochoa Zúñiga"),
               ("11:00", "13:00",  "Ecuaciones Diferénciales",  "Jaime Arroyo Ledesma")],

}

horarios_im = {
    "Lunes":[("07:00", "08:00",  "Programacion Web",  "Antonio Alfonso Luis Morales"),
             ("9:15", "11:00", "Aprendizaje de maquina",  "Luis López Moran"), 
             ("12:00",  "14:00",  "Escalamiento de redes", "Oswaldo Carrillo Zepeda")],
    "Martes":[("07:00",  "08:40",  "Ingles",  "Luis Daniel Benavides Sanchez"),
              ("09:15",  "11:00",  "Interacción humano Computadora","Laura Stanley Gaytán Lugo "),
              ("11:00",  "12:00",  "Aprendizaje de maquina",  "Luis López Moran"),
              ("13:00",  "15:00", "Sistemas operativos",  "Apolinar González Potes")],
    "Miercoles":[("9:15", "11:00", "Base de datos no relaciónales",  "Martha Elizabeth Evangelista Salazar"),
                 ("12:00",  "14:00", "Escalamiento de redes", "Oswaldo Carrillo Zepeda")],        
    "Jueves":[("07:00" ,"08:40", "Programación web",  "Antonio Alfonso Luis Morales"),
              ("10:00", "11:00", "Ingles", "Luis Daniel Benavides Sanchez"),
              ("12:00", "14:00",  "Aprendizaje de maquina",   "Luis López Moran")], 
    "Viernes":[("09:15", "11:00", "Sistemas operativos",  "Apolinar González Potes"),
               ("11:00",  "13:00",  "Base de datos no relacionales",   "Martha Elizabeth Evangelista Salazar"),
               ("13: 00",  "15:00",  "Interacción humana computadora",   "Laura Stanley Gaytán Lugo")] 


}



def mostrar_horarios(carrera, dia_semana):
    '''
    Muestra los horarios de clases para una carrera específica y día de la semana.

    Parameters:
    carrera (str): Nombre de la carrera.
    dia_semana (str): Día de la semana a mostrar (e.g., "Lunes").

    Funcionalidad:
    - Muestra las materias, horarios y profesores.
    - Permite registrar asistencia a través de checkboxes.

    '''
    st.write(f"Mostrando horarios para {dia_semana} de la carrera {carrera}")  

    horarios = []
    if carrera == "ICI":
        horarios = horarios_ici.get(dia_semana, [])
    elif carrera == "ISET":
        horarios = horarios_iset.get(dia_semana, [])
    elif carrera == "IME":
        horarios = horarios_ime.get(dia_semana, [])
    elif carrera == "IM":
        horarios = horarios_im.get(dia_semana, [])

    if not horarios:
        st.warning(f"No hay horarios disponibles para {dia_semana}.")
        return


    for hora_inicio, hora_fin, materia, profesor in horarios:
        col_horario, col_materia, col_asistencia = st.columns([1, 3, 1])
        col_horario.write(f"{hora_inicio} - {hora_fin}")
        col_materia.markdown(f"*{materia} - {profesor}*")
        asistencia = col_asistencia.checkbox(f"Asistió", key=f"{dia_semana}-{hora_inicio}-{hora_fin}")
        if st.button(f"Registrar ({hora_inicio}-{hora_fin})", key=f"btn-{dia_semana}-{hora_inicio}-{hora_fin}"):
            presente = True if asistencia else False
            db.registrar_asistencia_profesor(profesor, dia_semana, hora_inicio, presente)
            st.success(f"Asistencia registrada para {materia}.")

# Jefe de Grupo
def admin_menu(usuario):
    '''
    Muestra el calendario para registrar la asitencia de 
    los mastros si llegaron a la clase.

    '''
    st.header(f"Panel de Asistencia - {usuario[1]}")

    fecha_seleccionada = st.date_input("Selecciona un día", value=datetime.today(), min_value=datetime.today() - timedelta(days=30), max_value=datetime.today() + timedelta(days=30))
    dia_semana = fecha_seleccionada.strftime("%A")  

    dias_semana_traducidos = {
        "Monday": "Lunes",
        "Tuesday": "Martes",
        "Wednesday": "Miércoles",
        "Thursday": "Jueves",
        "Friday": "Viernes",
        "Saturday": "Sábado",
        "Sunday": "Domingo"
    }
    dia_semana_es = dias_semana_traducidos.get(dia_semana, dia_semana)  

    st.write(f"Día seleccionado: {dia_semana_es}")  
    if usuario[1] == "Miguel Ángel Ortiz Torres":
        mostrar_horarios("ICI", dia_semana_es)
    elif usuario[1] == "Cesar Eduardo Zepeda Gorrocino":
        mostrar_horarios("IME", dia_semana_es)
    elif usuario[1] == "Michelle Rosales Sánchez":
        mostrar_horarios("IM", dia_semana_es)
    elif usuario[1] == "Panfilo Gutierrez Alvarez Diaz":
        mostrar_horarios("ISET", dia_semana_es)

def menu_maestro(usuario):
    """
    Muestra el menú de opciones para los maestros, permitiéndoles descargar su propio 
    reporte de asistencia en un rango de fechas específico.

    Parameters:
    usuario (list or tuple): Información del usuario maestro autenticado. 
                             usuario[0] es el ID del maestro y usuario[1] es el nombre.

    Funcionalidad:
    - Permite al maestro seleccionar un rango de fechas.
    - Ofrece un botón para descargar un reporte PDF de su asistencia en el periodo especificado.

    """
    st.header(f"Panel de Asistencia - {usuario[1]} (Maestro)")

    # Selección del rango de fechas para el reporte
    fecha_inicio = st.date_input("Fecha de inicio", value=datetime.today() - timedelta(days=7))
    fecha_fin = st.date_input("Fecha de fin", value=datetime.today())

    # Botón para descargar el reporte de asistencia en PDF
    if st.button("Descargar Reporte de Asistencia en PDF"):
        rp.generar_reporte_profesor(usuario[0])
        st.success("Reporte descargado con éxito.")

# Login
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
        else:
            st.error("Credenciales incorrectas")
else:
    usuario = st.session_state['usuario']
    st.success(f"Bienvenido {usuario[1]} ({usuario[2]})")

    if usuario[2] == "admin":
        admin_menu(usuario)
    elif usuario[2] == "maestro":
        menu_maestro(usuario)

if st.session_state['usuario'] is not None:
    if st.button("Cerrar sesión"):
        st.session_state['usuario'] = None