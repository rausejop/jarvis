#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" JARVIS v005alpha

El estado actual de este prototipo contiene los primeros módulos de
obtención automatizada de fuentes, en concreto:
    GEO.EU.ES\exteriores.gob.es
    GEO.EU.ES\defensa.gob.es\ccd')
	
NOTA: esta versióin jarvis005a es una versión Alfa incompleta
      La última versión estable se encuentra en el siguiente enlace:
	  https://github.com/rausejop/jarvis/blob/master/jarvis004.py
	
"""

#  PEP 8 -- Style Guide for Python Code
# https://www.python.org/dev/peps/pep-0008/
# PEP 257 -- Docstring Conventions
# https://www.python.org/dev/peps/pep-0257/

# from __future__ import futuros

# Module Level Dunder Names
__all__ = ['r', 'a', 'p']
__author__ = "Rafael Ausejo Prieto"
__authors__ = "Rafael Ausejo Prieto and Rafael Ausejo Prieto"
__copyright__ = "Copyright 2019, Rafael Ausejo Prieto"
__credits__ = ["Rafael Ausejo Prieto", "Rafael Ausejo Prieto"]
__date__ = "6 de agosto de 2019"
__license__ = "GPL"
__version__ = "005a"
__maintainer__ = "Rafael Ausejo Prieto"
__email__ = "rafael.ausejo@gmail.com"
__status__ = "Prototype"
#__status__ = "Development"
#__status__ = "Production"

import os    # Standard library
import sys
import configparser

# Related third party imports
# Local application/library specific imports

# CONSTANTES
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36"
WGET_PARAMS = "-c --no-check-certificate --content-disposition"


# Fuente:    GEO.EU.ES\exteriores.gob.es
source = 'Ministerio de Asuntos Exteriores. Gobierno de España'
classification = 'A1'
dir_base = 'D:\DATALAKE'
dir_path = 'GEO.EU.ES\exteriores.gob.es'
PAISES = [
    "Alemania",
    "Austria",
    "Bélgica",
    "Bulgaria",
    "Chequia",
    "Chipre",
    "Croacia",
    "Dinamarca",
    "Eslovaquia",
    "Eslovenia",
    "España",
    "Estonia",
    "Finlandia",
    "Francia",
    "Grecia",
    "Hungría",
    "Irlanda",
    "Italia",
    "Letonia",
    "Lituania",
    "Luxemburgo",
    "Malta",
    "Países Bajos",
    "Polonia",
    "Portugal",
    "Reino Unido",
    "Rumanía",
    "Suecia",
    ]	

URL = [
    'http://www.exteriores.gob.es/Documents/FichasPais/ALEMANIA_FICHA%20PAIS.pdf',
    'http://www.exteriores.gob.es/Documents/FichasPais/AUSTRIA_FICHA%20PAIS.pdf',
    'http://www.exteriores.gob.es/Documents/FichasPais/BELGICA_FICHA%20PAIS.pdf',
    'http://www.exteriores.gob.es/Documents/FichasPais/BULGARIA_FICHA%20PAIS.pdf',
    'http://www.exteriores.gob.es/Documents/FichasPais/REPUBLICACHECA_FICHA%20PAIS.pdf',
    'http://www.exteriores.gob.es/Documents/FichasPais/CHIPRE_FICHA%20PAIS.pdf',
    'http://www.exteriores.gob.es/Documents/FichasPais/CROACIA_FICHA%20PAIS.pdf',
    'http://www.exteriores.gob.es/Documents/FichasPais/DINAMARCA_FICHA%20PAIS.pdf',
    'http://www.exteriores.gob.es/Documents/FichasPais/ESLOVAQUIA_FICHA%20PAIS.pdf',
    'http://www.exteriores.gob.es/Documents/FichasPais/ESLOVENIA_FICHA%20PAIS.pdf',
    'https://www.icex.es/icex/GetDocumento?dDocName=DAX2017729356&site=icexES -o DAX2017729356.pdf',
    'http://www.exteriores.gob.es/Documents/FichasPais/ESTONIA_FICHA%20PAIS.pdf',
    'http://www.exteriores.gob.es/Documents/FichasPais/FINLANDIA_FICHA%20PAIS.pdf',
    'http://www.exteriores.gob.es/Documents/FichasPais/FRANCIA_FICHA%20PAIS.pdf',
    'http://www.exteriores.gob.es/Documents/FichasPais/GRECIA_FICHA%20PAIS.pdf',
    'http://www.exteriores.gob.es/Documents/FichasPais/HUNGRIA_FICHA%20PAIS.pdf',
    'http://www.exteriores.gob.es/Documents/FichasPais/IRLANDA_FICHA%20PAIS.pdf',
    'http://www.exteriores.gob.es/Documents/FichasPais/ITALIA_FICHA%20PAIS.pdf',
    'http://www.exteriores.gob.es/Documents/FichasPais/LETONIA_FICHA%20PAIS.pdf',
    'http://www.exteriores.gob.es/Documents/FichasPais/LITUANIA_FICHA%20PAIS.pdf',
    'http://www.exteriores.gob.es/Documents/FichasPais/LUXEMBURGO_FICHA%20PAIS.pdf',
    'http://www.exteriores.gob.es/Documents/FichasPais/MALTA_FICHA%20PAIS.pdf',
    'http://www.exteriores.gob.es/Documents/FichasPais/PAISESBAJOS_FICHA%20PAIS.pdf',
    'http://www.exteriores.gob.es/Documents/FichasPais/POLONIA_FICHA%20PAIS.pdf',
    'http://www.exteriores.gob.es/Documents/FichasPais/PORTUGAL_FICHA%20PAIS.pdf',
    'http://www.exteriores.gob.es/Documents/FichasPais/REINOUNIDO_FICHA%20PAIS.pdf',
    'http://www.exteriores.gob.es/Documents/FichasPais/RUMANIA_FICHA%20PAIS.pdf',
    'http://www.exteriores.gob.es/Documents/FichasPais/SUECIA_FICHA%20PAIS.pdf',
    ]

# Función jarvis_direccion()
def jarvis_direccion():
    r""" Direction step, to be defined """ 
    # Función de Planificación de Inteligencia, por definir


# Función jarvis_obtencion()
def jarvis_obtencion(configuration):
    r""" Creates directory and discriminates file format """ 
    # Carga el fichero de configuración con el índice de las fuentes
    config = configparser.ConfigParser()
    config.read(f'jarvis.ini')
    source = config[configuration]['source']
    classification = config[configuration]['classification']
    dir_base = config[configuration]['dir_base']
    dir_path = config[configuration]['dir_path']
    file = config[configuration]['file']
    fileformat = config[configuration]['fileformat']
    print(f"FUENTE:            {source}")
    print(f"CLASIFICACIÓN:     {classification}")
    print(f"BASE:              {dir_base}")
    print(f"RUTA:              {dir_path}")
    print(f"FICHERO:           {file}")
    print(f"FORMATO:           {fileformat}")	

    # Crea el directorio y discrimina el formato del fichero de fuente
    old_path = os.getcwd()
    os.chdir(old_path)
    # os.path.join genera el path correcto tanto para WIndows como para Linux
	# Es importante que el fichero leido por configparser no tenga valores entrecomillados
    #        para que no fallen las rutas
    directory = os.path.join(dir_base, dir_path)
	# No es necesarios crear un backslash
	#    backslash = '\\'
    # directory = dir_base + backslash + dir_path
    print(f"DIRECTORIO:        {directory}")
    if not os.path.exists(directory):
        os.makedirs(directory)
    os.chdir(directory)

    # Discriminación de formatos
    print ({fileformat})
    if ({fileformat}) == "lista":
        print("Formato: lista")

    elif ({fileformat}) == "directorios":
        print("Formato: directorios")
        for i in range(len(PAISES)):
            descarga_directorios(PAISES[i], URL[i])
            # Vuelve al direcorio base
            os.chdir(directory)

    else:
        print("Formato: <desconocido>")

    # Vuelve a direcorio raíz
    os.chdir(old_path)


# Función descarga_directorios() para jarvis_obtencion()
def descarga_directorios(directorio, url):
    r""" Performs documents download """ 
    # Realiza la descarga de los docuemntos
    if not os.path.exists(directorio):
        os.mkdir(directorio)
    os.chdir(directorio)
    current_path = os.getcwd()
    print (f"Directorio actual: {current_path}")
    print (f"Descargando URL: {url}")
    # Añadir las comillas para envolver la URL. No olvidar los espacios entre parámetros
    command = "wget" + " " + WGET_PARAMS + " " + '--user-agent="' + USER_AGENT + '"' + " " + f'"{url}"'
# MASTER SWITCH ###############################################################
#    os.system(command)
    print (f"{command}")


# Función main()
def main(): 
    r""" Main program, implementing Intelligence Cycle steps """ 
    # Programa principal con las fases del Ciclo de Inteligencia
    jarvis_direccion()
    jarvis_obtencion(configuration = 'DEFAULT')
    jarvis_obtencion(configuration = 'GEO.EU.ES\exteriores.gob.es')
    jarvis_obtencion(configuration = 'GEO.EU.ES\defensa.gob.es\ccd')
#    jarvis_elaboracion()
#    jarvis_difusion()


# Comienzo del programa main()
    r""" Main program """ 
if __name__ == "__main__": 
    main()