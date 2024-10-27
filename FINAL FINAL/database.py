import sqlite3

def conectar():
    return sqlite3.connect('asistencia.db')

def crear_tablas():
    conexion = conectar()
    cursor = conexion.cursor()

    # Tabla de usuarios
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        rol TEXT NOT NULL,  
        correo TEXT UNIQUE NOT NULL,
        contrasena TEXT NOT NULL
    )
    ''')

    # Tabla de asistencia profesores
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS asistencia_profesores (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        profesor TEXT NOT NULL,
        dia_semana TEXT NOT NULL,
        hora_inicio TEXT NOT NULL,
        presente BOOLEAN NOT NULL
    )
    ''')

    conexion.commit()
    conexion.close()

def crear_usuario(nombre, rol, correo, contrasena):
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute('SELECT * FROM usuarios WHERE correo = ?', (correo,))
    if cursor.fetchone() is None:
        cursor.execute('''
        INSERT INTO usuarios (nombre, rol, correo, contrasena)
        VALUES (?, ?, ?, ?)
        ''', (nombre, rol, correo, contrasena))
        conexion.commit()
    conexion.close()

def registrar_asistencia_profesor(profesor, dia_semana, hora_inicio, presente):
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute('''
    INSERT INTO asistencia_profesores (profesor, dia_semana, hora_inicio, presente)
    VALUES (?, ?, ?, ?)
    ''', (profesor, dia_semana, hora_inicio, presente))
    conexion.commit()
    conexion.close()

def obtener_usuario(correo, contrasena):
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute('SELECT * FROM usuarios WHERE correo = ? AND contrasena = ?', (correo, contrasena))
    usuario = cursor.fetchone()
    conexion.close()
    return usuario