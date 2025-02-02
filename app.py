#!/usr/bin/env python3
import os
import mysql.connector

# Configuración de la base de datos utilizando las variables de entorno
DB_CONFIG = {
    'user': os.environ.get('MYSQL_USER'),
    'password': os.environ.get('MYSQL_PASSWORD'),
    'host': os.environ.get('MYSQL_HOST'),
    'database': os.environ.get('MYSQL_DATABASE'),
    'port': int(os.environ.get('MYSQL_PORT', 3306)),
    'ssl_ca': os.environ.get('MYSQL_SSL_CA') or None
}

def main():
    try:
        # Conectar a la base de datos
        connection = mysql.connector.connect(**DB_CONFIG)
        cursor = connection.cursor(dictionary=True)  # Usamos dictionary=True para obtener resultados en forma de diccionario

        # Consulta para obtener todos los registros de la tabla 'productos'
        query = "SELECT * FROM productos"
        cursor.execute(query)
        registros = cursor.fetchall()

        # Mostrar los registros obtenidos
        if registros:
            print("Registros encontrados en la tabla 'productos':")
            for registro in registros:
                print(registro)
        else:
            print("No se encontraron registros en la tabla 'productos'.")

    except mysql.connector.Error as err:
        print(f"Error al conectarse a la base de datos: {err}")
    finally:
        # Cerrar cursor y conexión si están abiertos
        if cursor:
            cursor.close()
        if connection and connection.is_connected():
            connection.close()

if __name__ == '__main__':
    main()
