#! /usr/bin/python

# ------------------------------------------------------------
# Ingenieria de Software
# Tarea 3

# TipoInscripcion.py
# Clase que representa el paquete de inscripciones.
#
# Autores: Michelle Fernandez, 09-10279.
#	   Donato Rolo, 10-10640.
#	   Carla Barazarte, 08-10096
#	   Alejandro Garbi, 08-10398
#	   Jose Figueredo, 10-10245
#	   Alejandro Guillen, 10-10333
# ------------------------------------------------------------
class TipoInscripcion:
    def __init__(self,tipo_inscripcion = None):
        self.tipo_inscripcion = tipo_inscripcion
    def inscripcion(self):
        if self.tipo_inscripcion != None:
            return self.tipo_inscripcion.inscripcion()
        else:
            return "Debe introducir un tipo de inscripcion"
