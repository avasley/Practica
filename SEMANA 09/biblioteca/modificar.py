# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 10:36:26 2022

@author: ANTONY
"""

import sqlite3

conexion = sqlite3.connect("bdbiblioteca.db")
cursor= conexion.cursor()
consulta = """ UPDATE EDITORIAL
            SET 
              NOMBRE= 'Editorial Imprenta Unión'
            WHERE
              IDEDITORIAL = 1
           """
cursor = conexion.cursor()
cursor.execute(consulta)
conexion.commit()
conexion.close()