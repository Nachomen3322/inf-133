# Importar módulo sqlite3
import sqlite3

# Crear conexión a la base de datos
conn = sqlite3.connect("personal.db")


# Crear tablas de SALARIOS
try:
    conn.execute(
        """
        CREATE TABLE SALARIOS
        (id INTEGER PRIMARY KEY,
        empleado_id INTEGER NOT NULL,
        salario REAL NOT NULL,
        fecha_inicio DATE NOT NULL,
        fecha_fin DATE NOT NULL,
        fecha_creacion TEXT NOT NULL);
        """
    )
except sqlite3.OperationalError:
    print("La tabla SALARIOS ya existe")

    # Crear tablas de EMPLEADOS
try:
    conn.execute(
        """
        CREATE TABLE EMPLEADOS
        (id INTEGER PRIMARY KEY,
        nombres TEXT NOT NULL,
        apellido_paterno TEXT NOT NULL,
        apellido_materno TEXT NOT NULL,
        fecha_contratacion DATE NOT NULL,
        departamento_id INTEGER NOT NULL,
        cargo_id INTEGER NOT NULL,
        fecha_creacion TEXT NOT ALL);
        """
    )

except sqlite3.OperationalError:
    print("La tabla EMPLEADOS ya existe")

    # Crear tablas de DEPARTAMENTOS
try:
    conn.execute(
        """
        CREATE TABLE DEPARTAMENTOS
        (id INTEGER PRIMARY KEY,
        nombre TEXT NOT NULL,
        fecha_creacion TEXT NOT NULL);
        """
    )

except sqlite3.OperationalError:
    print("La tabla DEPARTAMENTOS ya existe")

    # Crear tablas de CARGOS
try:
    conn.execute(
        """
        CREATE TABLE CARGOS
        (id INTEGER PRIMARY KEY,
        nombre TEXT NOT NULL,
        nivel TEXT NOT NULL,
        fecha_creacion TEXT NOT NULL);
        """
    )

except sqlite3.OperationalError:
    print("La tabla CARGOS ya existe")


# Insertar datos de DEPARTAMENTOS
conn.execute(
    """
    INSERT INTO DEPARTAMENTOS (id, nombre, fecha_creacion) 
    VALUES ('2020', 'Ventas', '11-04-2020')
    """
)

conn.execute(
    """
    INSERT INTO CARGOS (id, nombre, nivel, fecha_creacion) 
    VALUES (1, 'Gerente de Ventas', 'Senior', '10-02-2024')
    VALUES (2, 'Analista de Marketing', 'Junior', '11-04-2024')
    VALUES (3, 'Representante de ventas', 'Junior', '12-04-2024')
    """
)

# Inserta Empleados
conn.execute(
    """
    INSERT INTO EMPLEADOS (id, nombres, apellido_paterno, apellido_materno, fecha_contratacion, fecha_creacion)
    VALUES (1,'Juan', 'Gonzales', 'Perez', '15-05-2023', '10-04-2020')
    VALUES (2,'Maria', 'Lopez', 'Martinez', '20-06-2023', '11-04-2020')
    """
)

# Inserta  sALARIO

conn.execute(
    """
    INSERT INTO SALARIOS (id, salario, fecha_inicio, fecha_fin, fecha_creacion)
    VALUES('5', '3000', '01-04-2024', '30-04-2025', '15-05-2023')
    VALUES('5', '3500', '01-07-2023', '30-04-2024', '20-06-2023')
    
    """
)


# Consultar datos
print("SALARIOS:")
cursor = conn.execute("SELECT * FROM SALARIOS")
for row in cursor:
    print(row)

# Consultar datos
print("SALARIOS:")
cursor = conn.execute("SELECT * FROM CARGOS")
for row in cursor:
    print(row)

# Actualiza el precio del plato con id 2 (hamburguesa) a 9.99
conn.execute(
    """
    SELECT Salarios.
    """
)
print("\nActualiza el precio del plato con id 2 (hamburguesa) a 9.99")

cursor = conn.execute("SELECT * FROM SALARIOS")
for row in cursor:
    print(row)
cursor = conn.execute("SELECT * FROM EMPLEADOS")
for row in cursor:
    print(row)

# Actualiza el precio del plato con id 2 (hamburguesa) a 9.99
conn.execute(
    """
    UPDATE CARGOS
    SET cargo = 'Representante de Ventas'
    WHERE empleado_id = 2
    """
)
cursor = conn.execute("SELECT * CARGOS")
for row in cursor:
    print(row)


conn.execute(
    """
    UPDATE SALARIO
    SET salario = 3600
    WHERE empleado_id = 2
    """
)
cursor = conn.execute("SELECT * CARGOS")
for row in cursor:
    print(row)

# DELETE MARIA LOPEZ
# Elimina el pedido con id 3
# SON 2 DELETES


# HAY QUE ELIMINAR TODAS LAS TABLAS
# HAY QUE IR DE LA QUE MENOS DEPENDE HACIA LA QUE DEPENDE
conn.execute(
    """
    DELETE FROM EMPLEADOS
    WHERE id = 2
    """
)

print("\nElimina el empleado Maria Lopez Martinez")
cursor = conn.execute("SELECT * FROM EMPLEADOS")
for row in cursor:
    print(row)



##Nuevo representante # ultimo ejercicio


# Confirmar cambios
conn.commit()

# Cerrar conexión
conn.close()
