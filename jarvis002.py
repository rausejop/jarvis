#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os, sys

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


def descarga_pais(pais, url):
    os.mkdir(pais)
    os.chdir(pais)
    current_path = os.getcwd()
    print (f"Directorio actual: {current_path}")
    print (f"Descargando URL: {url}")
    command = f'wget -c --content-disposition "{url}"'
    os.system(command)
    print (f"{command}")


# Programa principal
old_path = os.getcwd()
for i in range(len(PAISES)):
    descarga_pais(PAISES[i], URL[i])
    os.chdir(old_path)
