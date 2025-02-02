#!/usr/bin/env python3
import os
import mysql.connector
from flask import Flask, jsonify
from flask_cors import CORS

# Crear la instancia de Flask
app = Flask(__name__)
CORS(app)

# Configuración de la base de datos utilizando las variables de entorno
DB_CONFIG = {
    'user': os.environ.get('MYSQL_USER'),
    'password': os.environ.get('MYSQL_PASSWORD'),
    'host': os.environ.get('MYSQL_HOST'),
    'database': os.environ.get('MYSQL_DATABASE'),
    'port': int(os.environ.get('MYSQL_PORT', 3306)),
    'ssl_ca': os.environ.get('MYSQL_SSL_CA') or None
}

@app.route('/productos', methods=['GET'])
def get_productos():
    try:
        # Conectar a la base de datos
        connection = mysql.connector.connect(**DB_CONFIG)
        cursor = connection.cursor(dictionary=True)

        # Consulta para obtener todos los registros de la tabla 'productos'
        query = "SELECT * FROM productos"
        cursor.execute(query)
        registros = cursor.fetchall()

        return jsonify(registros), 200

    except mysql.connector.Error as err:
        return jsonify({'error': f"Error al conectarse a la base de datos: {err}"}), 500

    finally:
        if cursor:
            cursor.close()
        if connection and connection.is_connected():
            connection.close()

if __name__ == '__main__':
    app.run(debug=True)
