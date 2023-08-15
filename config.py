#!/usr/bin/python
from configparser import ConfigParser

#Definición de la función config para la lectura del .ini
def config(filename='database.ini', section='postgresql'):
    #objeto parser de la clase ConfigParser del constructor ConfigParser()
    parser = ConfigParser()
    # lectura del archivo y sección de este.
    parser.read(filename)

    # diccionario vacío que almacenará los parámetros de conexión
    db = {}
    if parser.has_section(section):
        params = parser.items(section) #pasar por la tupla para conexión
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))

    return db