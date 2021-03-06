#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" JARVIS v005alpha

El estado actual de este prototipo contiene las siguientes estructuras
    jarvis.estructura_ESN2017
    jarvis.estructura_ODS2030
	
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
__all__ = ['02 bb', '5a 30', '5f ee','7d a8']
__author__ = "Rafael Ausejo Prieto"
__authors__ = "Rafael Ausejo Prieto and Rafael Ausejo Prieto"
__copyright__ = "(c) 2019 Rafael Ausejo Prieto"
__credits__ = ["Rafael Ausejo Prieto", "Rafael Ausejo Prieto"]
__date__ = "17/08/2019"
__license__ = "GPL"
__version__ = "005a2"
__maintainer__ = "Rafael Ausejo Prieto"
__email__ = "rafael.ausejo@gmail.com"
__status__ = "Prototype"
#__status__ = "Development"
#__status__ = "Production"

import os    # Standard library
import sys
import configparser
from datetime import datetime

# Related third party imports
# Local application/library specific imports


# Función jarvis_direccion(configuration)
def jarvis_direccion(file,dir_base):
    r""" Creates Planification Structure """ 
    # Lee la planificación y crea los directorios
    now_time = datetime.now()
    print (f"[*] {now_time} Starting structure creation")
    print (f"[+] {dir_base}")
    with open(file, encoding='utf-8') as f:
        dir_path = f.readline().lstrip().rstrip()
        while dir_path != '': 
#        for line in f:
#            line = line [0:len(line)-1]
            directory = os.path.join(dir_base, dir_path)			
            print(f"Creating directory: {directory}")
            if not os.path.exists(directory):
                os.makedirs(directory)
            dir_path = f.readline().lstrip().rstrip()
    f.closed
    now_time = datetime.now()	
    print (f"[*] {now_time} Ending structure creation")    
    # os.chdir({dir})


# Función jarvis_obtencion()
def jarvis_obtencion(configuration):
    r""" Creates directoriesy and discriminates file format """ 

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


# Función jarvis_direccion()
def jarvis_elaboracion():
    r""" Elaboration step, to be defined """ 
    # Función de Elaboración de Inteligencia, por definir
    pass


# Función jarvis_difusion()
def jarvis_difusion():
    r""" Dissemination step, to be defined """ 
    # Función de Difusión de Inteligencia, por definir
    pass


# Función main()
def main(): 
    r""" Main program, implementing Intelligence Cycle steps """ 
    # Programa principal con las variables globales
    old_path = os.getcwd()
    print(f"")
    print(f"JARVIS v{__version__} {__copyright__} [{__date__}]")
    start_time = datetime.now()
    now_time = start_time
    print (f"[*] {now_time} Configuration starts")
    config = configparser.ConfigParser()
    config.read(f'jarvis.ini')
#    configuration = 'DEFAULT'
    configuration = 'ODS2030'
    dir_base = config[configuration]['dir_base']
    print (f"[+] {dir_base}")
    jarvis_structure = config[configuration]['jarvis_structure']
    print (f"[+] {jarvis_structure}")	
    wget_params = config[configuration]['wget_params']
    print (f"[+] wget {wget_params}")
    wget_user_agent = config[configuration]['wget_user_agent']
    print (f"[+] {wget_user_agent}")
    end_time = datetime.now()
    print (f"[*] {end_time} Configuration ends")
    jarvis_direccion(jarvis_structure, dir_base)
#    jarvis_obtencion(configuration = 'DEFAULT')
#    jarvis_elaboracion()
#    jarvis_difusion()

    os.chdir(old_path)
    end_time = datetime.now()
    print (f"[*] {end_time} Program ends")
    total_time = end_time - start_time
    print (f"[*] Finished in {total_time}")


# Comienzo del programa main()
    r""" Main program """ 
if __name__ == "__main__": 
    main()