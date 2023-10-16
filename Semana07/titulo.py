# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 09:34:51 2023

@author: Alumno
"""
# Importamos la libreria
import camelcase

nombre = "jhonny tenorio casiano"

print(nombre.upper())
print(nombre.title())


#Creamos un objeto llamado cam
cam = camelcase.CamelCase()
print("Con camelcase....")

# imprimimos el nombre en formato título
# utilizamos camelcase
print(cam.hump(nombre))

# Para resolver el problema
# creamos otro objeto llamado cam2
# al definir el objeto, incluimos los argumentos
# 'flor' y 'león' 
cam2 = camelcase.CamelCase('jhonny','casiano')
print(cam2.hump(nombre))

