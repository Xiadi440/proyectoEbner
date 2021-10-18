#!/usr/bin/env python
# coding: utf-8

# ### Práctica 1: Manejo de BD con SQLite3 y Python
# #### Alumna: López Aguillón Anayansi Xiadani

# In[1]:


import sqlite3


# In[2]:


conexion = sqlite3.connect("ejemplo.db")


# In[3]:


#abrimos conexión
conexion = sqlite3.connect("ejemplo.db")

#creamos el cursor
cursor = conexion.cursor()

#cerramos la conexión
conexion.close()


# #### Crear una tabla 

# In[7]:


conexion = sqlite3.connect("ejemplo.db")
cursor = conexion.cursor()

#creamos una tabla llamada estudiantes
cursor.execute("CREATE TABLE estudiantes (email VARCHAR(100), carrera VARCHAR(100), nombre VARCHAR(100), edad INTEGER)")

conexion.close()


# #### Insertar datos 

# In[8]:


conexion = sqlite3.connect("ejemplo.db")
cursor = conexion.cursor()

#insertamos un registro en la tabla estudiantes
cursor.execute("INSERT INTO estudiantes VALUES ('bluenote@googlemail.com','Artes','Sharon', 27)")

#guardamos los cambios
conexion.commit()

conexion.close()


# #### Seleccionar e imprime registros de una tabla

# In[9]:


conexion = sqlite3.connect("ejemplo.db")
cursor = conexion.cursor()

#selecciona todos los registros de la tabla
cursor.execute("SELECT * FROM estudiantes")

usuarios = cursor.fetchone()##toma un solo registro
print(usuarios)


# #### Ingresar y leer varios registros al mismo tiempo

# In[10]:


##insertar
conexion = sqlite3.connect("ejemplo.db")
cursor = conexion.cursor()

usuarios = [
    ('parrillaexquisita@vip.com','Arquitectura','Giulia', 26),
    ('lollipopbusiness@vip.com','Contaduría','Rosana', 60),
    ('solfernandez@googlemail.com','Estadística','Sol', 30),
    ('carlitos@googlemail.com','Computación','Carlos', 60),
    ('imprentadetata@vip.com','Periodismo','Luciano', 21)
]

cursor.executemany("INSERT INTO estudiantes VALUES (?,?,?,?)", usuarios)

conexion.commit()

conexion.close()


# In[12]:


##leer
conexion = sqlite3.connect("ejemplo.db")
cursor = conexion.cursor()

##recuperamos los registros de la tabla
cursor.execute("SELECT * FROM estudiantes")

usuarios = cursor.fetchall()##toma todos los registros

##print(usuarios),este for lo hace por registro en vez de imprimir la tupla completa
for u in usuarios:
    print(u)
    
conexion.close()


# #### Leer un CSV e insertarlo en la BD 

# In[13]:


import csv

conexion = sqlite3.connect(r"C:\Users\Xiadani\ejemplo.db")##ruta exacta donde se encuentra la BD
cursor = conexion.cursor()

##abre el archivo de texto
archivo = open(r"C:\Users\Xiadani\008 datos_db.txt")##ruta exacta donde se encuentra el .txt

filas = csv.reader(archivo)##lee lo que hay dentro del .txt

cursor.executemany("INSERT INTO estudiantes VALUES (?,?,?,?)", filas)

##Para ver los resultados
cursor.execute("SELECT * FROM estudiantes")
print(cursor.fetchall())##imprime los datos de la tabla "estudiantes" con los nuevos registros

conexion.commit()
conexion.close()


# In[ ]:




