import sqlite3

def conectar():
    return sqlite3.connect('asistencia.db')

def crear_tablas():
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        rol TEXT NOT NULL,  
        correo TEXT UNIQUE NOT NULL,
        contrasena TEXT NOT NULL
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS profesores (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        carrera TEXT NOT NULL
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS materias (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        profesor_id INTEGER NOT NULL,
        carrera TEXT NOT NULL,
        FOREIGN KEY(profesor_id) REFERENCES profesores(id)
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS grupos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS horarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        grupo_id INTEGER NOT NULL,
        materia_id INTEGER NOT NULL,
        profesor_id INTEGER NOT NULL,
        dia_semana TEXT NOT NULL,
        hora_inicio TEXT NOT NULL,
        hora_fin TEXT NOT NULL,
        FOREIGN KEY(grupo_id) REFERENCES grupos(id),
        FOREIGN KEY(materia_id) REFERENCES materias(id),
        FOREIGN KEY(profesor_id) REFERENCES profesores(id)
    )
    ''')

    conexion.commit()
    conexion.close()

def crear_usuario(nombre, rol, correo, contrasena):
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute('SELECT * FROM usuarios WHERE correo = ?', (correo,))
    if cursor.fetchone() is not None:
        print(f"El usuario con correo {correo} ya existe.")
    else:
        cursor.execute('''
        INSERT INTO usuarios (nombre, rol, correo, contrasena)
        VALUES (?, ?, ?, ?)
        ''', (nombre, rol, correo, contrasena))
        conexion.commit()
        print(f"Usuario {nombre} agregado exitosamente.")
    conexion.close()

def obtener_usuario(correo, contrasena):
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute('SELECT * FROM usuarios WHERE correo = ? AND contrasena = ?', (correo, contrasena))
    usuario = cursor.fetchone()
    conexion.close()
    return usuario

def insertar_profesor(nombre, carrera):
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO profesores (nombre, carrera) VALUES (?, ?)", (nombre, carrera))
    conexion.commit()
    conexion.close()

def obtener_profesores():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT id, nombre FROM profesores")
    profesores = cursor.fetchall()
    conexion.close()
    return profesores

def insertar_materia(nombre, profesor_id, carrera):
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO materias (nombre, profesor_id, carrera) VALUES (?, ?, ?)", (nombre, profesor_id, carrera))
    conexion.commit()
    conexion.close()

def obtener_materias():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT id, nombre FROM materias")
    materias = cursor.fetchall()
    conexion.close()
    return materias

def insertar_grupo(nombre):
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO grupos (nombre) VALUES (?)", (nombre,))
    conexion.commit()
    conexion.close()

def obtener_grupos():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT id, nombre FROM grupos")
    grupos = cursor.fetchall()
    conexion.close()
    return grupos

def insertar_horario(grupo_id, materia_id, profesor_id, dia_semana, hora_inicio, hora_fin):
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute('''
    INSERT INTO horarios (grupo_id, materia_id, profesor_id, dia_semana, hora_inicio, hora_fin)
    VALUES (?, ?, ?, ?, ?, ?)
    ''', (grupo_id, materia_id, profesor_id, dia_semana, hora_inicio, hora_fin))
    conexion.commit()
    conexion.close()

