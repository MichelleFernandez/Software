#! /usr/bin/python

# ------------------------------------------------------------
# Ingenieria de Software
# Tarea 3

# Descuento.py
# Clase que representa un descuento en el paquete de inscripciones.
#
# Autores: Michelle Fernandez, 09-10279.
#	   Donato Rolo, 10-10640.
#	   Carla Barazarte, 08-10096
#	   Alejandro Garbi, 08-10398
#	   Jose Figueredo, 10-10245
#	   Alejandro Guillen, 10-10333
# ------------------------------------------------------------
class Descuento:
    def __init__(self,tipo_descuento = None):
        self.tipo_descuento = tipo_descuento
    def inscripcion(self):
        if self.tipo_descuento != None:
            return self.tipo_descuento.inscripcion()
        else:
            return "Debe introducir un tipo de descuento"