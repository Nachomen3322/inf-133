import sqlite3

conn = sqlite3.connect("restaurante.db")


# conn.execute(
#     """
#     INSERT INTO ESTUDIANTES (nombre, apellido, fecha_nacimiento)
#     VALUES ('Carlos','Gomez','2022-5-5')
#     """
# )

# conn.execute(
#     """
#     INSERT INTO CARRERAS (nombre, DURACION)
#     VALUES ('Licenciatura en Contabilidad', 4)
#     """
# )
# conn.commit()


conn.execute(
    """
    SELECT PLATOS.nombre, MESAS.numero
    FROM PEDIDOS
    JOIN MESAS ON MESAS.id = PEDIDOS.mesa_id
    JOIN PLATOS ON PLATOS.id = PEDIDOS.plato_id    
    """
)

cursor = conn.execute("SELECT * FROM MESAS")
for row in cursor:
    print(row)


conn.commit()
