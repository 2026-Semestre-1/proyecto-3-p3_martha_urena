#Proyecto 3
"""
*APUNTES:
-super() me lo enseño a usar el tutor de taller, me funciona para poder llamar el constructor de la clase que se heredan los atributos.
"""
import random
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
"""
Nombre: Pais
Atributos: codigo_fifa, nombre, continente, ranking_fifa
Métodos: constructor, mostrar_datos, actualizar_datos
"""
class Pais:
    """
    Definición: Constructor
    Salidas: analiza todos los atributos
    """
    def __init__(self, codigo_fifa, nombre, continente, ranking_fifa):
        self.codigo_fifa = codigo_fifa
        self.nombre = nombre
        self.continente = continente
        self.ranking_fifa = ranking_fifa

    """
    Nombre: validar_codigo_fifa
    Entradas: codigo_fifa
    Salidas: devuelve True si el código FIFA es un texto con exactamente 3 letras, y False si no cumple con la validación
    Restricciones:
        codigo_fifa debe ser un string
        el string debe tener exactamente 3 caracteres
        los caracteres deben ser letras mayúsculas o minúsculas
    """
    def validar_codigo_fifa(self, codigo_fifa):
        if not isinstance(codigo_fifa, str):
            return False
        try:
            letra_cero = codigo_fifa[0]
            letra_uno = codigo_fifa[1]
            letra_dos = codigo_fifa[2]
        except Exception:
            return False

        codigo_tiene_extra = False
        try:
            letra_extra = codigo_fifa[3]
            codigo_tiene_extra = True
        except Exception:
            codigo_tiene_extra = False

        if codigo_tiene_extra == True:
            return False

        indice = 0
        while indice < 3:
            letra = codigo_fifa[indice]
            if letra < "A" or letra > "Z":
                if letra < "a" or letra > "z":
                    return False
            indice += 1

        return True
    """
    Nombre: mostrar_datos
    Entradas: self.nombre, self.codigo, self.continente, self.ranking_fila
    Salidas:  muestra la información del país
    Restricciones:
        Los valores (self.nommbre, self.cofigo_fifa, self.contitente) deben ser de tipo String
        El valor self.ranking_fifa debe ser de tipo entero
    """
    def mostrar_datos(self):
        if not isinstance(self.nombre, str):
            return "Error: El nombre del país debe ser de tipo String"
        elif not self.validar_codigo_fifa(self.codigo_fifa) == True:
            return "Error: El código fifa debe ser de tipo String y debe tener exactamente 3 letras"
        elif not isinstance(self.continente, str):
            return "Error: El continente debe ser de tipo String"
        elif not isinstance(self.ranking_fifa, int):
            return "Error: El ranking fifa debe ser de tipo entero"
        elif self.ranking_fifa <= 0:
            return "Error: El ranking fifa debe ser un número positivo"
        else:
            print("País: ", self.nombre)
            print("Código FIFA: ", self.codigo_fifa)
            print("Continente: ", self.continente)
            print("Ranking FIFA: " , self.ranking_fifa)
            
    """
    Nombre: actualizar_datos
    Entradas: nombre, codigo, continente, ranking_fila
    Salidas: permite modificar uno o varios atributos
    Restricciones:
        Los valores (nommbre, cofigo_fifa, contitente) deben ser de tipo String
        El valor ranking_fifa debe ser de tipo entero positivo
    """
    def actualizar_datos(self, nombre, codigo_fifa, continente, ranking_fifa):
        if nombre != "":
            if not isinstance(nombre, str):
                return "Error: El nombre del país debe ser de tipo String"
            else:
                self.nombre = nombre
        if codigo_fifa != "":
            if not isinstance(codigo_fifa, str):
                return "Error: El código fifa debe ser de tipo String"
            if not self.validar_codigo_fifa(codigo_fifa):
                return "Error: El código fifa debe tener exactamente 3 letras"
            else:
                self.codigo_fifa = codigo_fifa
        if continente != "":
            if not isinstance(continente, str):
                return "Error: El continente debe ser de tipo String"
            else:
                self.continente = continente
        if ranking_fifa != 0:
            if not isinstance(ranking_fifa, int):
                return "Error: El ranking fifa debe ser de tipo entero y numérico"
            if ranking_fifa < 0:
                return "Error: El ranking fifa debe ser un número positivo"
            else:
                self.ranking_fifa = ranking_fifa

        return "Los datos han sido actualizados correctamente"

"""
Nombre: Persona (clase padre)
Atributos: nombre, apellido, fecha_nacimiento, nacionalidad
Métodos: constructor, mostrar_datos
"""
class Persona:
    """
    Definisión: Constructor
    Salidas: Analiza todos los atributos comunes
    """
    def __init__(self, nombre, apellido, fecha_nacimiento, nacionalidad):
        self.nombre = nombre
        self.apellido = apellido
        self.fecha_nacimiento = fecha_nacimiento
        self.nacionalidad = nacionalidad

    """
    Nombre: mostrar_datos
    Entradas: nombre, apellido, fecha_nacimiento, nacionalidad
    Salidas: muestra la información básica de la persona
    Restricciones:
        Los valores deben ser de tipo String
    """
    def mostrar_datos(self):
        if not isinstance(self.nombre, str):
            return "Error: El nombre debe ser de tipo String"
        elif not isinstance(self.apellido, str):
            return "Error: El apellido debe ser de tipo String"
        elif not isinstance(self.fecha_nacimiento, str):
            return "Error: La fecha de nacimiento debe ser de tipo String"
        elif not isinstance(self.nacionalidad, str):
            return "Error: La nacionalidad debe ser de tipo String"
        else:
            print("Nombre:", self.nombre)
            print("Apellido:", self.apellido)
            print("Fecha de nacimiento:", self.fecha_nacimiento)
            print("Nacionalidad:", self.nacionalidad)

"""
Nombre: Entrenador
Atributos: licencia, experiencia_anios, sistema_juego
Métodos: Costructor, mostrar_datos, actualizar_datos
"""
class Entrenador(Persona):
    """
    Definición: Constructor
    Salidas:
        Inicializa los atributos de Persona y los propios de Entrenador
        (debe invocar al constructor de la clase padre)
    """
    def __init__(self, nombre, apellido, fecha_nacimiento, nacionalidad, licencia, experiencia_anios, sistema_juego):
        super().__init__(nombre, apellido, fecha_nacimiento, nacionalidad)
        self.licencia = licencia
        self.experiencia_anios = experiencia_anios
        self.sistema_juego = sistema_juego

    """
    Nombre: mostrar_datos
    Entradas: nombre, apellido, fecha_nacimiento, nacionalidad, licencia, experiencia_anios, sistema_juego
    Salidas:muestra la información completa del entrenador
    Restricciones:
        Los valores de texto deben ser de tipo String
        experiencia_anios debe ser un entero no negativo
    """
    def mostrar_datos(self):
        if not isinstance(self.nombre, str):
            return "Error: El nombre debe ser de tipo String"
        elif not isinstance(self.apellido, str):
            return "Error: El apellido debe ser de tipo String"
        elif not isinstance(self.fecha_nacimiento, str):
            return "Error: La fecha de nacimiento debe ser de tipo String"
        elif not isinstance(self.nacionalidad, str):
            return "Error: La nacionalidad debe ser de tipo String"
        elif not isinstance(self.licencia, str):
            return "Error: La licencia debe ser de tipo String"
        elif not isinstance(self.experiencia_anios, int):
            return "Error: La experiencia debe ser de tipo entero"
        elif self.experiencia_anios < 0:
            return "Error: La experiencia debe ser un número no negativo"
        elif not isinstance(self.sistema_juego, str):
            return "Error: El sistema de juego debe ser de tipo String"
        else:
            print("Nombre:", self.nombre)
            print("Apellido:", self.apellido)
            print("Fecha de nacimiento:", self.fecha_nacimiento)
            print("Nacionalidad:", self.nacionalidad)
            print("Licencia:", self.licencia)
            print("Experiencia (años):", self.experiencia_anios)
            print("Sistema de juego:", self.sistema_juego)

    """
    Nombre: actualizar_datos
    Entradas: licencia, experiencia_anios, sistema_juego
    Salidas: permite modificar uno o varios atributos del entrenador
    Restricciones:
        Los valores de texto deben ser de tipo String
        experiencia_anios debe ser un entero no negativo
    """
    def actualizar_datos(self, licencia, experiencia_anios, sistema_juego):
        if licencia != "":
            if not isinstance(licencia, str):
                return "Error: La licencia debe ser de tipo String"
            self.licencia = licencia

        if experiencia_anios != 0:
            if not isinstance(experiencia_anios, int):
                return "Error: La experiencia debe ser de tipo entero"
            if experiencia_anios < 0:
                return "Error: La experiencia debe ser un número no negativo"
            self.experiencia_anios = experiencia_anios

        if sistema_juego != "":
            if not isinstance(sistema_juego, str):
                return "Error: El sistema de juego debe ser de tipo String"
            self.sistema_juego = sistema_juego
        
        return "Los datos han sido actualizados correctamente"

"""
Nombre: Futbolista
Atributos: dorsal, posicion, total_tarjetas_amarillas, total_tarjetas_rojas, goles, asistencias, puntaje_individual
Métodos: constructor, mostrar_datos, actualizar_datos, registrar_gol, registrar_asistencia, registrar_tarjeta
"""
class Futbolista(Persona):
    """
    Definición: Constructor
    Salidas: inicializa los atributos de Persona y los propios de Futbolista
    """
    def __init__(self, nombre, apellido, fecha_nacimiento, nacionalidad, dorsal, posicion, total_tarjetas_amarillas, total_tarjetas_rojas, goles, asistencias, puntaje_individual):
        super().__init__(nombre, apellido, fecha_nacimiento, nacionalidad)
        self.dorsal = dorsal
        self.posicion = posicion
        self.total_tarjetas_amarillas = total_tarjetas_amarillas
        self.total_tarjetas_rojas = total_tarjetas_rojas
        self.goles = goles
        self.asistencias = asistencias
        self.puntaje_individual = puntaje_individual

    """
    Nombre: mostrar_datos
    Entradas: nombre, apellido, fecha_nacimiento, nacionalidad, dorsal, posicion, total_tarjetas_amarillas, total_tarjetas_rojas, goles, asistencias, puntaje_individual
    Salidas: sobrescribe el método de Persona para incluir dorsal, posición, estadísticas y puntaje
    Restricciones:
        Los valores de texto deben ser de tipo String
        Los valores numéricos deben ser enteros y positivos
    """
    def mostrar_datos(self):
        if not isinstance(self.nombre, str):
             return "Error: El nombre debe ser de tipo String"
        elif not isinstance(self.apellido, str):
            return "Error: El apellido debe ser de tipo String"
        elif not isinstance(self.fecha_nacimiento, str):
            return "Error: La fecha de nacimiento debe ser de tipo String"
        elif not isinstance(self.nacionalidad, str):
            return "Error: La nacionalidad debe ser de tipo String"
        elif not isinstance(self.dorsal, int):
            return "Error: El dorsal debe ser de tipo entero"
        elif self.dorsal <= 0 or self.dorsal > 99:
            return "Error: El dorsal debe estar entre 1 y 99"
        elif not isinstance(self.posicion, str):
            return "Error: La posición debe ser de tipo String"
        elif not isinstance(self.total_tarjetas_amarillas, int):
            return "Error: Las tarjetas amarillas deben ser un número entero"
        elif self.total_tarjetas_amarillas < 0:
            return "Error: Las tarjetas amarillas no pueden ser un número negativo"
        elif not isinstance(self.total_tarjetas_rojas, int):
            return "Error: Las tarjetas rojas deben ser un número entero"
        elif self.total_tarjetas_rojas < 0:
            return "Error: Las tarjetas rojas no pueden ser un número negativo"
        elif not isinstance(self.goles, int):
            return "Error: Los goles deben ser un número entero"
        elif self.goles < 0:
            return "Error: Los goles no pueden ser un número negativo"
        elif not isinstance(self.asistencias, int):
            return "Error: Las asistencias deben ser un número entero"
        elif self.asistencias < 0:
            return "Error: Las asistencias no pueden ser un número negativo"
        elif not isinstance(self.puntaje_individual, int):
            return "Error: El puntaje individual debe ser de tipo entero"
        elif self.puntaje_individual < 1 or self.puntaje_individual > 100:
            return "Error: El puntaje individual debe estar entre 1 y 100"
        else:
            print("Nombre:", self.nombre)
            print("Apellido:", self.apellido)
            print("Fecha de nacimiento:", self.fecha_nacimiento)
            print("Nacionalidad:", self.nacionalidad)
            print("Dorsal:", self.dorsal)
            print("Posición:", self.posicion)
            print("Tarjetas amarillas:", self.total_tarjetas_amarillas)
            print("Tarjetas rojas:", self.total_tarjetas_rojas)
            print("Goles:", self.goles)
            print("Asistencias:", self.asistencias)
            print("Puntaje individual:", self.puntaje_individual)

    """
    Nombre: actualizar_datos
    Entradas: dorsal, posicion, total_tarjetas_amarillas, total_tarjetas_rojas, goles, asistencias, puntaje_individual
    Salidas: permite modificar los atributos del futbolista
    Restricciones:
        Los valores de texto deben ser de tipo String
        Los valores numéricos deben ser enteros y positivos
    """
    def actualizar_datos(self, dorsal, posicion, total_tarjetas_amarillas, total_tarjetas_rojas, goles, asistencias, puntaje_individual):
        if dorsal != 0:
            if not isinstance(dorsal, int):
                return "Error: El dorsal debe ser de tipo entero"
            if dorsal <= 0 or dorsal > 99:
                return "Error: El dorsal debe estar entre 1 y 99"
            else:
                self.dorsal = dorsal
                
        if posicion != "":
            if not isinstance(posicion, str):
                return "Error: La posición debe ser de tipo String"
            else:
                self.posicion = posicion
                
        if total_tarjetas_amarillas != 0:
            if not isinstance(total_tarjetas_amarillas, int):
                return "Error: Las tarjetas amarillas deben ser un número entero"
            if total_tarjetas_amarillas < 0:
                return "Error: Las tarjetas amarillas no pueden ser un número negativo"
            else:
                self.total_tarjetas_amarillas = total_tarjetas_amarillas
                
        if total_tarjetas_rojas != 0:
            if not isinstance(total_tarjetas_rojas, int):
                return "Error: Las tarjetas rojas deben ser un número entero"
            if total_tarjetas_rojas < 0:
                return "Error: Las tarjetas rojas no pueden ser un número negativo"
            else:
                self.total_tarjetas_rojas = total_tarjetas_rojas

        if goles != 0:
            if not isinstance(goles, int):
                return "Error: Los goles deben ser un número entero"
            if goles < 0:
                return "Error: Los goles no pueden ser un número negativo"
            else:
                self.goles = goles

        if asistencias != 0:
            if not isinstance(asistencias, int):
                return "Error: Las asistencias deben ser un número entero"
            if asistencias < 0:
                return "Error: Las asistencias no pueden ser un número negativo"
            else:
                self.asistencias = asistencias

        if puntaje_individual != 0:
            if not isinstance(puntaje_individual, int):
                return "Error: El puntaje individual debe ser de tipo entero"
            if puntaje_individual < 1 or puntaje_individual > 100:
                return "Error: El puntaje individual debe estar entre 1 y 100"
            else:
                self.puntaje_individual = puntaje_individual

        
        return "Los datos han sido actualizados correctamente"

    """
    Nombre: registrar_gol
    Entradas: ninguna
    Salidas: incrementa goles en 1
    Restricciones: ninguna
    """           
    def registrar_gol(self):
        self.goles += 1
        return "Gol registrado correctamente"

    """
    Nombre: registrar_asistencia
    Entradas: ninguna
    Salidas: incrementa asistencias en 1
    Restricciones: ninguna
    """
    def registrar_asistencia(self):
        self.asistencias += 1
        return "Asistencia registrada correctamente"

    """
    Nombre: registrar_tarjeta
    Entradas: tipo
    Salidas: incrementa el contador de tarjetas amarillas o rojas, según el tipo recibido
    Restricciones:
        tipo debe ser 'amarilla' o 'roja'
    """
    def registrar_tarjeta(self, tipo):
        if not isinstance(tipo, str):
            return "Error: El tipo de tarjeta debe ser de tipo String"
        if tipo == "amarilla":
            self.total_tarjetas_amarillas += 1
            return "Tarjeta amarilla registrada correctamente"
        elif tipo == "roja":
            self.total_tarjetas_rojas += 1
            return "Tarjeta roja registrada correctamente"
        else:
            return "Error: El tipo de tarjeta debe ser 'amarilla' o 'roja'" 
                
"""
Nombre: Seleccion
Atributos: codigo_equipo, pais, entrenador, jugadores, total_goles_favor, total_goles_contra, total_tarjetas_amarillas, total_tarjetas_rojas, fuerza_equipo
Métodos: constructor, mostrar_datos, agregar_jugador, eliminar_jugador, asignar_entrenador, registrar_resultado, calcular_fuerza_equipo
"""

class Seleccion:
    """
    Definición: Constructor
    Salidas:  inicializa los atributos (la lista de jugadores inicia vacía y los contadores en cero)
    """
    def __init__(self, codigo_equipo, pais, entrenador):
        self.codigo_equipo = codigo_equipo
        self.pais = pais
        self.entrenador = entrenador
        self.jugadores = []
        self.total_goles_favor = 0
        self.total_goles_contra = 0
        self.total_tarjetas_amarillas = 0
        self.total_tarjetas_rojas = 0
        self.fuerza_equipo = 0

    """
    Nombre: largoLista
    Entradas: una lista
    Salidas: la cantidad de elementos que posee la lista
    Restricciones:
        El objeto debe ser una lista
    """
    def largoLista(self, lista):
        if not isinstance(lista, list):
            return "Error: El objeto de entrada debe ser de tipo lista"
        else:
            contador = 0
            for elemento in lista:
                contador = contador + 1
            return contador

    """
    Nombre: validar_jugadores
    Entradas: ninguna
    Salidas: devuelve "Jugadores válidos" si todos los elementos de la lista son objetos de Futbolista; de lo contrario devuelve un mensaje de error
    Restricciones:
        la lista de jugadores debe existir
        cada elemento de la lista debe ser un objeto Futbolista
    """
    def validar_jugadores(self):
        indice = 0
        total = self.largoLista(self.jugadores)
        while indice < total:
            if not isinstance(self.jugadores[indice], Futbolista):
                return "Error: todos los jugadores deben ser objetos de Futbolista"
            indice += 1
        return "Jugadores válidos"
        
    """
    Nombre: mostrar_datos
    Entradas: codigo_equipo, pais, entrenador, jugadores, total_goles_favor, total_goles_contra, total_tarjetas_amarillas, total_tarjetas_rojas, fuerza_equipo
    Salidas: muestra la información de la selección, incluyendo país, entrenador y plantilla
    Restricciones:
        codigo_equipo debe ser de tipo String
        pais debe ser un objeto Pais
        entrenador debe ser un objeto Entrenador
        jugadores debe ser una lista de futbolistas con mínimo 11 y máximo 23
        los totales deben ser enteros no negativos
    """
    def mostrar_datos(self):
        if not isinstance(self.codigo_equipo, str):
            return "Error: El código del equipo debe ser de tipo String"
        try:
            valor = self.pais.codigo_fifa
        except Exception:
            return "Error: El país debe ser un objeto de Pais"
        try:
            valor = self.entrenador.licencia
        except Exception:
            return "Error: El entrenador debe ser un objeto de Entrenador"
        if not isinstance(self.jugadores, list):
            return "Error: Los jugadores deben estar en una lista"

        resultado_validacion = self.validar_jugadores()
        if resultado_validacion != "Jugadores válidos":
            return resultado_validacion
        
        elif self.largoLista(self.jugadores) < 11:
            return "Error: La selección debe tener al menos 11 jugadores"
        elif self.largoLista(self.jugadores) > 23:
            return "Error: La selección no puede tener más de 23 jugadores"
        elif not isinstance(self.total_goles_favor, int):
            return "Error: total_goles_favor debe ser un número entero"
        elif self.total_goles_favor < 0:
            return "Error: total_goles_favor no puede ser negativo"
        elif not isinstance(self.total_goles_contra, int):
            return "Error: total_goles_contra debe ser un número entero"
        elif self.total_goles_contra < 0:
            return "Error: total_goles_contra no puede ser negativo"
        elif not isinstance(self.total_tarjetas_amarillas, int):
            return "Error: total_tarjetas_amarillas debe ser un número entero"
        elif self.total_tarjetas_amarillas < 0:
            return "Error: total_tarjetas_amarillas no puede ser negativo"
        elif not isinstance(self.total_tarjetas_rojas, int):
            return "Error: total_tarjetas_rojas debe ser un número entero"
        elif self.total_tarjetas_rojas < 0:
            return "Error: total_tarjetas_rojas no puede ser negativo"
        elif not isinstance(self.fuerza_equipo, (int, float)):
            return "Error: fuerza_equipo debe ser un número decimal o entero"
        else:
            print("Código equipo:", self.codigo_equipo)
            print("País:", self.pais.nombre)
            print("Entrenador:", self.entrenador.nombre, self.entrenador.apellido)
            print("Total goles favor:", self.total_goles_favor)
            print("Total goles contra:", self.total_goles_contra)
            print("Total tarjetas amarillas:", self.total_tarjetas_amarillas)
            print("Total tarjetas rojas:", self.total_tarjetas_rojas)
            print("Fuerza equipo:", self.fuerza_equipo)
            print("Jugadores convocados:")
            for jugador in self.jugadores:
                print("  -", jugador.dorsal, jugador.nombre, jugador.apellido, jugador.posicion)

        
    """
    Nombre: agregar_jugador
    Entradas: futbolista
    Salidas: agrega un futbolista a la lista, validando que no se exceda el máximo de 23
    Restricciones:
        futbolista debe ser un objeto Futbolista
        la lista no debe exceder 23 jugadores
        no debe haber dos jugadores con el mismo dorsal

    """
    def agregar_jugador(self, futbolista):
        if not isinstance(futbolista, Futbolista):
            return "Error: El parámetro debe ser un objeto de Futbolista"
        
        try:
            valor = futbolista.dorsal
        except Exception:
            return "Error: El jugador debe ser un objeto de Futbolista"
        if self.largoLista(self.jugadores) >= 23:
            return "Error: No se puede agregar más de 23 jugadores"
        i = 0
        total = self.largoLista(self.jugadores)
        while i < total:
            if self.jugadores[i].dorsal == futbolista.dorsal:
                return "Error: Ya existe un jugador con ese dorsal"
            i += 1

        nueva_lista = [0] * (total + 1)
        i = 0
        while i < total:
            nueva_lista[i] = self.jugadores[i]
            i += 1
        nueva_lista[total] = futbolista
        self.jugadores = nueva_lista
        return "Jugador agregado correctamente"

    """
    Nombre: eliminar_jugador
    Entradas: dorsal
    Salidas: elimina un futbolista de la lista según su dorsal
    Restricciones:
        dorsal debe ser entero
    """
    def eliminar_jugador(self, dorsal):
        if not isinstance(dorsal, int):
            return "Error: El dorsal debe ser de tipo entero"
        indice = -1
        i = 0
        total = self.largoLista(self.jugadores)
        while i < total:
            if self.jugadores[i].dorsal == dorsal:
                indice = i
            i += 1

        if indice == -1:
            return "Error: No se encontró un jugador con ese dorsal"

        nueva_lista = [0] * (total - 1)
        i = 0
        j = 0
        while i < total:
            if i != indice:
                nueva_lista[j] = self.jugadores[i]
                j += 1
            i += 1

        self.jugadores = nueva_lista
        return "Jugador eliminado correctamente"

    """
    Nombre: asignar_entrenador
    Entradas: entrenador
    Salidas: asigna o reemplaza el entrenador del equipo
    Restricciones:
        entrenador debe ser un objeto Entrenador
    """
    def asignar_entrenador(self, entrenador):
        if not isinstance(entrenador, Entrenador):
            return "Error: El parámetro debe ser un objeto de Entrenador"
        try:
            valor = entrenador.licencia
        except Exception:
            return "Error: El entrenador debe ser un objeto Entrenador"
        self.entrenador = entrenador
        return "Entrenador asignado correctamente"

    """
    Nombre: registrar_resultado
    Entradas: goles_favor, goles_contra, tarjetas_am, tarjetas_rojas
    Salidas:  actualiza los totales del equipo tras un partido
    Restricciones:
        todos los valores deben ser enteros no negativos
    """
    def registrar_resultado(self, goles_favor, goles_contra, tarjetas_am, tarjetas_rojas):
        if not isinstance(goles_favor, int):
            return "Error: goles_favor debe ser un número entero"
        elif goles_favor < 0:
            return "Error: goles_favor no puede ser negativo"
        elif not isinstance(goles_contra, int):
            return "Error: goles_contra debe ser un número entero"
        elif goles_contra < 0:
            return "Error: goles_contra no puede ser negativo"
        elif not isinstance(tarjetas_am, int):
            return "Error: tarjetas_am debe ser un número entero"
        elif tarjetas_am < 0:
            return "Error: tarjetas_am no puede ser negativo"
        elif not isinstance(tarjetas_rojas, int):
            return "Error: tarjetas_rojas debe ser un número entero"
        elif tarjetas_rojas < 0:
            return "Error: tarjetas_rojas no puede ser negativo"
        else:
            self.total_goles_favor += goles_favor
            self.total_goles_contra += goles_contra
            self.total_tarjetas_amarillas += tarjetas_am
            self.total_tarjetas_rojas += tarjetas_rojas
            return "Resultado registrado correctamente"

    """
    Nombre: calcular_fuerza_equipo
    Entradas: ninguna
    Salidas: calcula y actualiza el atributo fuerza_equipo (ver fórmula en sección 5)
    Restricciones:
        debe haber al menos 11 jugadores convocados
    """
    def calcular_fuerza_equipo(self):
        if not isinstance(self.jugadores, list):
            return "Error: Los jugadores deben estar en una lista"

        resultado_validacion = self.validar_jugadores()
        if resultado_validacion != "Jugadores válidos":
            return resultado_validacion
        
        total_jugadores = self.largoLista(self.jugadores)
        if self.largoLista(self.jugadores) < 11:
            return "Error: La selección debe tener al menos 11 jugadores para calcular la fuerza"

        puntajes = [0] * total_jugadores
        indice_jugador = 0
        while indice_jugador < total_jugadores:
            puntajes[indice_jugador] = self.jugadores[indice_jugador].puntaje_individual
            indice_jugador += 1

        #Acá ordeno de mayor a menor manualmente
        num_pasada = 0
        while num_pasada < total_jugadores:
            indice_actual = 0
            while indice_actual < total_jugadores - num_pasada - 1:
                if puntajes[indice_actual] < puntajes[indice_actual + 1]:
                    #Realizo el intercambio
                    puntaje_temporal = puntajes[indice_actual]
                    puntajes[indice_actual] = puntajes[indice_actual + 1]
                    puntajes[indice_actual + 1] = puntaje_temporal
                indice_actual += 1
            num_pasada += 1
        #Calculo el promedio de los 11 titulares
        suma_titulares = 0
        contador_titulares = 0
        while contador_titulares < 11:
            suma_titulares += puntajes[contador_titulares]
            contador_titulares += 1
        promedio_jugadores = suma_titulares / 11

        factor_entrenador = self.entrenador.experiencia_anios * 4
        if factor_entrenador > 100:
            factor_entrenador = 100

        factor_ranking = 100 - self.pais.ranking_fifa
        fuerza = (promedio_jugadores * 0.6) + (factor_entrenador * 0.25) + (factor_ranking * 0.15)
        self.fuerza_equipo = fuerza
        return "Fuerza de equipo calculada correctamente"
    

"""
Nombre: Partido
Atributos: id_partido, equipo_1, equipo_2, goles_equipo1, goles_equipo2, fase, fecha
Métodos: Constuctor, simular, generar_ganador, mostrar_resultado
"""
class Partido:
    """
    Definición: Constructor
    Salidas: inicializa los atributos (los goles inician en 0)
    """
    def __init__(self, id_partido, equipo_1, equipo_2, fase, fecha):
        self.id_partido = id_partido
        self.equipo_1 = equipo_1
        self.equipo_2 = equipo_2
        self.goles_equipo1 = 0
        self.goles_equipo2 = 0
        self.fase = fase
        self.fecha = fecha
        self.penales_equipo1 = None
        self.penales_equipo2 = None

    """
    Nombre: simular
    Entradas: usa los atributos del partido y las selecciones
    Salidas:  ejecuta el algoritmo de simulación (sección 5) y asigna los goles de cada equipo
    Restricciones:
        los equipos deben ser objetos Seleccion válidos
        id_partido debe ser entero
        fase y fecha deben ser Strings
    """
    def simular(self):
        if not isinstance(self.id_partido, int):
            return "Error: id_partido debe ser un número entero"
        if not isinstance(self.fase, str):
            return "Error: La fase debe ser de tipo String"
        if not isinstance(self.fecha, str):
            return "Error: La fecha debe ser de tipo String"
        
        try:
            fuerza1 = self.equipo_1.fuerza_equipo
        except Exception:
            return "Error: equipo_1 debe ser un objeto de Seleccion válido"
        try:
            fuerza2 = self.equipo_2.fuerza_equipo
        except Exception:
            return "Error: equipo_2 debe ser un objeto de Seleccion válido"
        
        if not isinstance(fuerza1, (int, float)):
            return "Error: fuerza_equipo de equipo_1 debe ser un número decimal o entero"
        if not isinstance(fuerza2, (int, float)):
            return "Error: fuerza_equipo de equipo_2 debe ser un número decimal o entero"


        if fuerza1 > fuerza2:
            diferencia = fuerza1 - fuerza2

            if diferencia > 30:
                self.goles_equipo1 = random.randint(2, 7) #Fuerte
                self.goles_equipo2 = random.randint(0, 3) #Débil
                
            elif diferencia > 15:
                self.goles_equipo1 = random.randint(1, 5) #Fuerte
                self.goles_equipo2 = random.randint(0, 4) #Débil
                
            else:
                self.goles_equipo1 = random.randint(0, 4) #Parejos
                self.goles_equipo2 = random.randint(0, 4)
                
        elif fuerza2 > fuerza1:
            diferencia = fuerza2 - fuerza1

            if diferencia > 30:
                self.goles_equipo1 = random.randint(0, 3) #Dèbil
                self.goles_equipo2 = random.randint(2, 7) #Fuerte
                
            elif diferencia > 15:
                self.goles_equipo1 = random.randint(0, 4) #Débil
                self.goles_equipo2 = random.randint(1, 5) #Fuerte

            else:
                self.goles_equipo1 = random.randint(0, 4) #Parejos
                self.goles_equipo2 = random.randint(0, 4)
        else:
            #Fuerza exactamente igual
            self.goles_equipo1 = random.randint(0, 4)
            self.goles_equipo2 = random.randint(0, 4)

        return "Partido simulado correctamente"

    """
    Nombre: generar_ganador
    Entradas: usa goles_equipo1 y goles_equipo2
    Salidas:  retorna la selección ganadora, o None en caso de empate (solo válido en fase de grupos)
    Restricciones:
        los goles deben ser entero
    """
    def generar_ganador(self):
        if not isinstance(self.goles_equipo1, int):
            return "Error: goles_equipo1 debe ser un número entero"
        if not isinstance(self.goles_equipo2, int):
            return "Error: goles_equipo2 debe ser un número entero"
        if self.goles_equipo1 > self.goles_equipo2:
            return self.equipo_1
        elif self.goles_equipo2 > self.goles_equipo1:
            return self.equipo_2
        else:
            penales1 = self.penales_equipo1
            penales2 = self.penales_equipo2

            if penales1 is None or penales2 is None:
                return None
            if penales1 > penales2:
                return self.equipo_1
            elif penales2 > penales1:
                return self.equipo_2
        return None

    """
    Nombre: mostrar_resultado
    Entradas: usa los atributos del partido
    Salidas: muestra el resultado del partido en formato legible
    Restricciones:
        fase y fecha deben ser Strings
        goles_equipo1 y goles_equipo2 deben ser entero
    """
    def mostrar_resultado(self):
        if not isinstance(self.fase, str):
            return "Error: La fase debe ser de tipo String"
        if not isinstance(self.fecha, str):
            return "Error: La fecha debe ser de tipo String"
        if not isinstance(self.goles_equipo1, int):
            return "Error: goles_equipo1 debe ser un número entero"
        if not isinstance(self.goles_equipo2, int):
            return "Error: goles_equipo2 debe ser un número entero"
        try:
            codigo1 = self.equipo_1.codigo_equipo
        except Exception:
            return "Error: equipo_1 debe ser un objeto de Seleccion válido"
        try:
            codigo2 = self.equipo_2.codigo_equipo
        except Exception:
            return "Error: equipo_2 debe ser un objeto de Seleccion válido"

        print("Resultado:", codigo1, self.goles_equipo1, "-", self.goles_equipo2, codigo2)
        
"""
Nombre: Grupo
Atributos: nombre_grupo, equipos, partidos
Métodos: Constructor, agregar_equipo, jugar_partidos, calcular_tabla, obtener_clasificados, mostrar_tabla
"""
#Los nombres de las variables son largos porque me ayuda a orientarme (son muchas variables)
class Grupo:
    """
    Definición: Constructor
    Salidas: inicializa los atributos (listas vacías)
    """
    def __init__(self, nombre_grupo):
        self.nombre_grupo = nombre_grupo
        self.fecha = "01/01/2024"
        self.equipos = []
        self.partidos = []
        self.tabla_equipos = []
        self.tabla_puntos = []
        self.tabla_goles_favor = []
        self.tabla_goles_contra = []
        self.tabla_diferencia = []

    """
    Nombre: largoLista
    Entradas: una lista
    Salidas: devuelve el largo de la lista
    Restricciones:
        El objeto debe ser una lista
    """
    def largoLista(self, lista):
        if not isinstance(lista, list):
            return "Error: El objeto de entrada debe ser de tipo lista"
        else:
            contador = 0
            for elemento in lista:
                contador = contador + 1
            return contador

    """
    Nombre: agregar_equipo
    Entradas: seleccion
    Salidas: agrega una selección al grupo, validando que no se exceda el máximo de 4
    Restricciones:
        seleccion debe ser un objeto Seleccion
        no debe exceder 4 equipos
    """
    def agregar_equipo(self, seleccion):
        try:
            codigo = seleccion.codigo_equipo
        except Exception:
            return "Error: La selección debe ser un objeto de Seleccion"

        if self.largoLista(self.equipos) >= 4:
            return "Error: No se puede exceder el máximo de 4 equipos"

        total_equipos = self.largoLista(self.equipos)
        indice_equipo = 0
        while indice_equipo < total_equipos:
            if self.equipos[indice_equipo].codigo_equipo == codigo:
                return "Error: La selección ya está en el grupo"
            indice_equipo += 1

        nueva_lista_equipos = [0] * (total_equipos + 1)
        indice_equipo = 0
        while indice_equipo < total_equipos:
            nueva_lista_equipos[indice_equipo] = self.equipos[indice_equipo]
            indice_equipo += 1

        nueva_lista_equipos[total_equipos] = seleccion
        self.equipos = nueva_lista_equipos

        return "Selección agregada correctamente"
        

    """
    Nombre: jugar_partidos
    Entradas: ninguna
    Salidas: genera y simula todos los partidos de todos contra todos dentro del grupo
    Restricciones:
        debe haber al menos 2 equipos en el grupo
    """
    def jugar_partidos(self):
        if self.largoLista(self.equipos) < 2:
            return "Error: Debe haber al menos 2 equipos para jugar partidos"

        total_equipos = self.largoLista(self.equipos)
        total_partidos_actuales = self.largoLista(self.partidos)
        id_partido = total_partidos_actuales + 1

        indice_equipo_uno = 0
        while indice_equipo_uno < total_equipos:
            indice_equipo_dos = indice_equipo_uno + 1
            while indice_equipo_dos < total_equipos:
                equipo_uno = self.equipos[indice_equipo_uno]
                equipo_dos = self.equipos[indice_equipo_dos]

                partido = Partido(id_partido, equipo_uno, equipo_dos, self.nombre_grupo, self.fecha)
                resultado_partido = partido.simular()
                
                if resultado_partido != "Partido simulado correctamente":
                    return resultado_partido

                equipo_uno.registrar_resultado(partido.goles_equipo1, partido.goles_equipo2, 0, 0)

                equipo_dos.registrar_resultado(partido.goles_equipo2, partido.goles_equipo1, 0, 0)

                total_partidos_actuales = self.largoLista(self.partidos)
                nueva_lista_partidos = [0] * (total_partidos_actuales + 1)
                indice_partido_actual = 0
                while indice_partido_actual < total_partidos_actuales:
                    nueva_lista_partidos[indice_partido_actual] = self.partidos[indice_partido_actual]
                    indice_partido_actual += 1
            
                nueva_lista_partidos[total_partidos_actuales] = partido
                self.partidos = nueva_lista_partidos
            
                id_partido += 1
                indice_equipo_dos += 1
            
            indice_equipo_uno += 1
        
        return "Partidos simulados correctamente"

    """
    Nombre: calcular_tabla
    Entradas: ninguna
    Salidas: calcula puntos, diferencia de goles y posiciones de cada equipo del grupo
    Restricciones:
        debe haber al menos 2 equipos en el grupo
    """
    def calcular_tabla(self):
        total_equipos = self.largoLista(self.equipos)
        if total_equipos < 2:
            return "Error: No hay suficientes equipos para calcular la tabla"

        self.tabla_equipos = [0] * total_equipos
        self.tabla_puntos = [0] * total_equipos
        self.tabla_goles_favor = [0] * total_equipos
        self.tabla_goles_contra = [0] * total_equipos
        self.tabla_diferencia = [0] * total_equipos

        indice_equipo = 0
        while indice_equipo < total_equipos:
            self.tabla_equipos[indice_equipo] = self.equipos[indice_equipo]
            self.tabla_puntos[indice_equipo] = 0
            self.tabla_goles_favor[indice_equipo] = 0
            self.tabla_goles_contra[indice_equipo] = 0
            self.tabla_diferencia[indice_equipo] = 0
            indice_equipo += 1

        total_partidos = self.largoLista(self.partidos)
        indice_partido = 0
        while indice_partido < total_partidos:
            partido = self.partidos[indice_partido]

            if not isinstance(partido.goles_equipo1, int):
                return "Error: goles_equipo1 debe ser un número entero"
            if not isinstance(partido.goles_equipo2, int):
                return "Error: goles_equipo2 debe ser un número entero"

            equipo_uno = partido.equipo_1
            equipo_dos = partido.equipo_2
            indice_equipo_uno = -1
            indice_equipo_dos = -1

            indice_equipo = 0
            while indice_equipo < total_equipos:
                if self.tabla_equipos[indice_equipo].codigo_equipo == equipo_uno.codigo_equipo:
                    indice_equipo_uno = indice_equipo
                if self.tabla_equipos[indice_equipo].codigo_equipo == equipo_dos.codigo_equipo:
                    indice_equipo_dos = indice_equipo
                indice_equipo += 1

            if indice_equipo_uno == -1 or indice_equipo_dos == -1:
                return "Error: Partido con selección no válida"

            self.tabla_goles_favor[indice_equipo_uno] += partido.goles_equipo1
            self.tabla_goles_contra[indice_equipo_uno] += partido.goles_equipo2
            self.tabla_goles_favor[indice_equipo_dos] += partido.goles_equipo2
            self.tabla_goles_contra[indice_equipo_dos] += partido.goles_equipo1

            if partido.goles_equipo1 > partido.goles_equipo2:
                self.tabla_puntos[indice_equipo_uno] += 3
            elif partido.goles_equipo2 > partido.goles_equipo1:
                self.tabla_puntos[indice_equipo_dos] += 3
            else:
                self.tabla_puntos[indice_equipo_uno] += 1
                self.tabla_puntos[indice_equipo_dos] += 1

            indice_partido += 1

        indice_equipo = 0
        while indice_equipo < total_equipos:
            self.tabla_diferencia[indice_equipo] = self.tabla_goles_favor[indice_equipo] - self.tabla_goles_contra[indice_equipo]
            indice_equipo += 1

        
        indice_equipo = 0
        while indice_equipo < total_equipos:
            mejor_indice = indice_equipo
            indice_equipo_comparado = indice_equipo + 1
            while indice_equipo_comparado < total_equipos:
                if self.tabla_puntos[indice_equipo_comparado] > self.tabla_puntos[mejor_indice]:
                    mejor_indice = indice_equipo_comparado
                elif self.tabla_puntos[indice_equipo_comparado] == self.tabla_puntos[mejor_indice]:
                    if self.tabla_diferencia[indice_equipo_comparado] > self.tabla_diferencia[mejor_indice]:
                        mejor_indice = indice_equipo_comparado
                    elif self.tabla_diferencia[indice_equipo_comparado] == self.tabla_diferencia[mejor_indice]:
                        if self.tabla_goles_favor[indice_equipo_comparado] > self.tabla_goles_favor[mejor_indice]:
                            mejor_indice = indice_equipo_comparado

                #Único incremento del ciclo interno
                indice_equipo_comparado += 1

                

                if mejor_indice != indice_equipo:
                    equipo_temporal = self.tabla_equipos[indice_equipo]
                    puntos_temporales = self.tabla_puntos[indice_equipo]
                    goles_favor_temporal = self.tabla_goles_favor[indice_equipo]
                    goles_contra_temporal = self.tabla_goles_contra[indice_equipo]
                    diferencia_temporal = self.tabla_diferencia[indice_equipo]

                    self.tabla_equipos[indice_equipo] = self.tabla_equipos[mejor_indice]
                    self.tabla_puntos[indice_equipo] = self.tabla_puntos[mejor_indice]
                    self.tabla_goles_favor[indice_equipo] = self.tabla_goles_favor[mejor_indice]
                    self.tabla_goles_contra[indice_equipo] = self.tabla_goles_contra[mejor_indice]
                    self.tabla_diferencia[indice_equipo] = self.tabla_diferencia[mejor_indice]

                    self.tabla_equipos[mejor_indice] = equipo_temporal
                    self.tabla_puntos[mejor_indice] = puntos_temporales
                    self.tabla_goles_favor[mejor_indice] = goles_favor_temporal
                    self.tabla_goles_contra[mejor_indice] = goles_contra_temporal
                    self.tabla_diferencia[mejor_indice] = diferencia_temporal
                
            indice_equipo += 1

        return "Tabla calculada correctamente"

    """
    Nombre: obtener_clasificados
    Entradas: ninguna
    Salidas: retorna los 2 mejores equipos del grupo según la tabla
    Restricciones:
        debe calcularse la tabla antes de obtener los clasificados 
    """
    def obtener_clasificados(self):
        
        resultado_tabla = "Tabla calculada correctamente"
        
        if self.largoLista(self.tabla_equipos) < 2:
            resultado_tabla = self.calcular_tabla()
        if resultado_tabla != "Tabla calculada correctamente":
            return resultado_tabla

        total_tabla = self.largoLista(self.tabla_equipos)

        if total_tabla >= 2:
            clasificados = [0] * 2
            clasificados[0] = self.tabla_equipos[0]
            clasificados[1] = self.tabla_equipos[1]
        elif total_tabla == 1:
            clasificados = [0] * 1
            clasificados[0] = self.tabla_equipos[0]
        else:
            clasificados = []

        for equipo in clasificados:
            print(equipo.codigo_equipo, "-", equipo.pais.nombre)

        return clasificados
        
    """
    Nombre: mostrar_tabla
    Entradas: ninguna
    Salidas: muestra la tabla de posiciones ordenada del grupo
    Restricciones:
        debe calcularse la tabla antes de mostrarla
    """
    def mostrar_tabla(self):
        if self.largoLista(self.tabla_equipos) < 1:
            resultado_tabla = self.calcular_tabla()
            if resultado_tabla != "Tabla calculada correctamente":
                return resultado_tabla

        print("Tabla del grupo", self.nombre_grupo)
        print("Equipo | Puntos | GF | GC | Dif")
        indice_equipo = 0
        total_tabla = self.largoLista(self.tabla_equipos)
        while indice_equipo < total_tabla:
            equipo = self.tabla_equipos[indice_equipo]
            print(equipo.codigo_equipo, "|", self.tabla_puntos[indice_equipo], "|", self.tabla_goles_favor[indice_equipo], "|", self.tabla_goles_contra[indice_equipo], "|", self.tabla_diferencia[indice_equipo])

            indice_equipo += 1

"""
Nombre: Fase 
Atributos: nombre_fase, partidos
Métodos: Constructor, registrar_juego, jugar_fase, mostrar_juegos, obtener_clasificados
"""
class Fase:
    """
    Definición: Constructor
    Salidas: inicializa los atributos (lista de partidos vacía)
    """
    def __init__(self, nombre_fase):
        self.nombre_fase = nombre_fase
        self.grupos = []
        self.partidos = []
        self.clasificados = []

    """
    Nombre: largoLista
    Entradas: una lista
    Salidas: la cantidad de elementos que posee la lista
    Restricciones:
        El objeto debe ser una lista
    """
    def largoLista(self, lista):
        if not isinstance(lista, list):
            return "Error: El objeto de entrada debe ser de tipo lista"
        else:
            contador = 0
            for elemento in lista:
                contador = contador + 1
            return contador

    """
    Nombre: registrar_juego
    Entradas: equipo1, equipo2
    Salidas: crea un nuevo Partido entre los dos equipos y lo agrega a la fase
    Restricciones:
        ambos equipos deben ser objetos de Seleccion y deben ser diferentes
    """
    def registrar_juego(self, equipo1, equipo2):
        if not isinstance(equipo1, Seleccion):
            return "Error: equipo1 debe ser un objeto de Seleccion"
        if not isinstance(equipo2, Seleccion):
            return "Error: equipo2 debe ser un objeto de Seleccion"
        if equipo1.codigo_equipo == equipo2.codigo_equipo:
            return "Error: los equipos deben ser diferentes"

        total = self.largoLista(self.partidos)
        id_partido = total + 1

        partido = Partido(id_partido, equipo1, equipo2, self.nombre_fase, "Sin fecha")

        nueva_lista = [0] * (total + 1)
        indice = 0
        while indice < total:
            nueva_lista[indice] = self.partidos[indice]
            indice += 1

        nueva_lista[total] = partido
        self.partidos = nueva_lista

        return "Juego registrado correctamente"

    """
    Nombre: jugar_fase
    Entradas: ninguna
    Salidas: simula todos los partidos de la fase. En caso de empate, simula penales
    Restricciones:
        Debe haber partidos registrados
    """
    def jugar_fase(self):
        total = self.largoLista(self.partidos)

        if total == 0:
            return "Error: No hay partidos registrados en la fase"

        indice = 0
        while indice < total:
            partido = self.partidos[indice]

            resultado = partido.simular()

            if resultado != "Partido simulado correctamente":
                return resultado

            if partido.goles_equipo1 == partido.goles_equipo2:
                fuerza1 = partido.equipo_1.fuerza_equipo
                fuerza2 = partido.equipo_2.fuerza_equipo

                if not isinstance(fuerza1, (int, float)):
                    return "Error: fuerza_equipo de equipo_1 debe ser un número decimal o entero"
                if not isinstance(fuerza2, (int, float)):
                    return "Error: fuerza_equipo de equipo_2 debe ser un número decimal o entero"

                penales1 = 0
                penales2 = 0
                hay_empate = True

                while hay_empate:
                    penales1 = random.randint(2, 5)
                    penales2 = random.randint(2, 5)

                    if penales1 != penales2:
                        hay_empate = False

                partido.penales_equipo1 = penales1
                partido.penales_equipo2 = penales2

            indice += 1

        return "Fase jugada correctamente"

    """
    Nombre: mostrar_juegos
    Entradas: ninguna
    Salidas: muestra los resultados de todos los partidos de la fase
    Restricciones:
        Debe haber partidos registrados 
    """
    def mostrar_juegos(self):
        total = self.largoLista(self.partidos)

        if total == 0:
            return "Error: No hay partidos registrados"

        print("Juegos de la fase:", self.nombre_fase)

        indice = 0
        while indice < total:
            partido = self.partidos[indice]
            texto_juego = "Juego " + str(indice + 1) + " : " + partido.equipo_1.codigo_equipo + " " + str(partido.goles_equipo1) + " - " + str(partido.goles_equipo2) + " " + partido.equipo_2.codigo_equipo

            penales1 = partido.penales_equipo1
            penales2 = partido.penales_equipo2
            if penales1 is not None and penales2 is not None:
                texto_juego += " (Penales: " + str(penales1) + " - " + str(penales2) + ")"

            print(texto_juego)
            indice += 1

        return "Juegos mostrados correctamente"

    """
    Nombre: obtener_clasificados
    Entradas: ninguna
    Salidas: retorna la lista de equipos ganadores que avanzan a la siguiente fase
    Restricciones:
        debe haber partidos registrados
    """
    def obtener_clasificados(self):
        total = self.largoLista(self.partidos)

        if total == 0:
            return "Error: No hay partidos registrados"
        clasificados = []

        indice = 0
        while indice < total:
            partido = self.partidos[indice]
            ganador = partido.generar_ganador()

            if ganador is None:
                return "Error: El partido terminó en empate"

            if self.largoLista(clasificados) == 0:
                clasificados = [0] * 1
                clasificados[0] = ganador
            else:
                total_actual = self.largoLista(clasificados)
                nueva_lista = [0] * (total_actual + 1)

                indice_clas = 0
                while indice_clas < total_actual:
                    nueva_lista[indice_clas] = clasificados[indice_clas]
                    indice_clas += 1

                nueva_lista[total_actual] = ganador
                clasificados = nueva_lista

            indice += 1

        self.clasificados = clasificados

        for equipo in clasificados:
            print(equipo.codigo_equipo, "-", equipo.pais.nombre)
        
        return clasificados

"""
Nombre: Mundial
Atributos: nombre, anio, paises, selecciones, grupos, fases, campeon
Métodos: Constructor, registrar_pais, registrar_seleccion, crear_grupos, jugar_fase_grupos, armar_fase_eliminatoria, determinar_campeon, mostrar_tabla_general, generar_reporte
"""
class Mundial:
    """
    Definición: Constructor
    Salidas:
    """
    def __init__(self, nombre, anio):
        self.nombre = nombre
        self.anio = anio
        self.paises = []
        self.selecciones = []
        self.grupos = []
        self.fases = []
        self.campeon = None

    """
    Nombre: largoLista
    Entradas: una lista
    Salidas: la cantidad de elementos que posee la lista
    Restricciones:
        El objeto debe ser una lista
    """
    def largoLista(self, lista):
        if not isinstance(lista, list):
            return "Error: El objeto de entrada debe ser de tipo lista"
        else:
            contador = 0
            for elemento in lista:
                contador = contador + 1
            return contador
        
    """
    Nombre: registrar_pais
    Entradas: pais
    Salidas: agrega un país a la lista de países
    Restricciones:
        el parámetro pais debe ser un objeto de la clase Pais
    """
    def registrar_pais(self, pais):
        if not isinstance(pais, Pais):
            return "Error: El país debe ser un objeto de Pais"

        total = self.largoLista(self.paises)
        nueva_lista = [0] * (total + 1)

        indice = 0
        while indice < total:
            nueva_lista[indice] = self.paises[indice]
            indice += 1

        nueva_lista[total] = pais
        self.paises = nueva_lista

        return "País registrado correctamente"

    """
    Nombre: registrar_seleccion
    Entradas: seleccion
    Salidas: agrega una selección a la lista de selecciones
    Restricciones:
        el parámetro seleccion debe ser un objeto de la clase Seleccion
    """
    def registrar_seleccion(self, seleccion):
        if not isinstance(seleccion, Seleccion):
            return "Error: La selección debe ser un objeto de Seleccion"

        total = self.largoLista(self.selecciones)
        nueva_lista = [0] * (total + 1)

        indice = 0
        while indice < total:
            nueva_lista[indice] = self.selecciones[indice]
            indice += 1

        nueva_lista[total] = seleccion
        self.selecciones = nueva_lista

        return "Selección registrada correctamente"

    """
    Nombre: crear_grupos
    Entradas: cantidad_grupos
    Salidas: organiza las selecciones registradas en la cantidad de grupos indicada, de forma equilibrada
    Restricciones:
        debe ser un número entero
        debe ser mayor que cero
        debe haber selecciones registradas
        la cantidad de grupos no puede ser mayor que la cantidad de selecciones
    """
    def crear_grupos(self, cantidad_grupos):
        if not isinstance(cantidad_grupos, int):
            return "Error: cantidad_grupos debe ser un número entero"
        if cantidad_grupos <= 0:
            return "Error: cantidad_grupos debe ser mayor que cero"

        total_selecciones = self.largoLista(self.selecciones)

        if total_selecciones == 0:
            return "Error: No hay selecciones registradas"
        if cantidad_grupos > total_selecciones:
            return "Error: No se pueden crear más grupos que selecciones"

        nueva_lista_grupos = [0] * cantidad_grupos

        indice = 0
        while indice < cantidad_grupos:
            nombre_grupo = "Grupo " + str(indice + 1)
            nuevo_grupo = Grupo(nombre_grupo)
            nueva_lista_grupos[indice] = nuevo_grupo
            indice += 1

        self.grupos = nueva_lista_grupos

        indice_seleccion = 0
        total_grupos = self.largoLista(self.grupos)

        while indice_seleccion < total_selecciones:
            indice_grupo = indice_seleccion % total_grupos
            grupo_actual = self.grupos[indice_grupo]
            resultado = grupo_actual.agregar_equipo(self.selecciones[indice_seleccion])

            if resultado != "Selección agregada correctamente":
                return resultado

            indice_seleccion += 1

        return "Grupos creados correctamente"

        
    """
    Nombre: jugar_fase_grupos
    Entradas: ninguna
    Salidas:  ejecuta jugar_partidos() de cada grupo y calcula sus tablas
    Restricciones:
        debe existir al menos un grupo creado
        cada grupo debe poder ejecutar jugar_partidos() y calcular_tabla()
    """
    def jugar_fase_grupos(self):
        total_grupos = self.largoLista(self.grupos)

        if total_grupos == 0:
            return "Error: No hay grupos creados"

        indice = 0
        while indice < total_grupos:
            resultado_partidos = self.grupos[indice].jugar_partidos()

            if resultado_partidos != "Partidos simulados correctamente":
                return resultado_partidos

            resultado_tabla = self.grupos[indice].calcular_tabla()

            if resultado_tabla != "Tabla calculada correctamente":
                return resultado_tabla

            indice += 1

        return "Fase de grupos jugada correctamente"

    
    """
    Nombre: armar_fase_eliminatoria
    Entradas: nombre_fase, clasificados
    Salidas:  crea los enfrentamientos de la fase eliminatoria a partir de los equipos clasificados
    Restricciones:
        nombre_fase debe ser texto
        clasificados debe ser una lista #se valida en largoLista
        la cantidad de equipos clasificados debe ser par
    """
    def armar_fase_eliminatoria(self, nombre_fase, clasificados):
        if not isinstance(nombre_fase, str):
            return "Error: El nombre de la fase debe ser de tipo String"

        total_clasificados = self.largoLista(clasificados)

        if total_clasificados == 0:
            return "Error: No hay equipos clasificados"

        if total_clasificados % 2 != 0:
            return "Error: La cantidad de equipos clasificados debe ser par"

        fase_nueva = Fase(nombre_fase)

        indice = 0
        while indice < total_clasificados:
            equipo1 = clasificados[indice]
            equipo2 = clasificados[indice + 1]

            resultado = fase_nueva.registrar_juego(equipo1, equipo2)

            if resultado != "Juego registrado correctamente":
                return resultado

            indice += 2

        total_fases = self.largoLista(self.fases)
        nueva_lista_fases = [0] * (total_fases + 1)

        indice = 0
        while indice < total_fases:
            nueva_lista_fases[indice] = self.fases[indice]
            indice += 1

        nueva_lista_fases[total_fases] = fase_nueva
        self.fases = nueva_lista_fases

        return fase_nueva

    """
    Nombre: jugar_fase_eliminatoria
    Entradas: fase
    Salidas: ejecuta jugar_fase() de la fase indicada y retorna los clasificados a la siguiente ronda
    Restricciones:
        fase debe ser un objeto de la clase Fase
    """
    def jugar_fase_eliminatoria(self, fase):
        if not isinstance(fase, Fase):
            return "Error: La fase debe ser un objeto de Fase"

        resultado_fase = fase.jugar_fase()

        if resultado_fase != "Fase jugada correctamente":
            return resultado_fase

        resultado_clasificados = fase.obtener_clasificados()

        if isinstance(resultado_clasificados, str):
            return resultado_clasificados

        return resultado_clasificados

    """
    Nombre: determinar_campeon
    Entradas: ninguuna
    Salidas: ejecuta el flujo completo desde octavos (o dieciseisavos) hasta la final y asigna el atributo campeon
    Restricciones:
        deben existir al menos 2 selecciones
        debe poder crear los grupos si aún no existen
        debe existir una fase de grupos para obtener los clasificados
    """
    def determinar_campeon(self):
        total_selecciones = self.largoLista(self.selecciones)

        if total_selecciones < 2:
            return "Error: Deben existir al menos 2 selecciones"
        if self.largoLista(self.grupos) == 0:
            if total_selecciones >= 16:
                cantidad_grupos = total_selecciones // 4
                resultado = self.crear_grupos(cantidad_grupos)
            else:
                resultado = self.crear_grupos(2)

            if resultado != "Grupos creados correctamente":
                return resultado

        resultado_fase_grupos = self.jugar_fase_grupos()

        if resultado_fase_grupos != "Fase de grupos jugada correctamente":
            return resultado_fase_grupos

        clasificados_iniciales = []

        indice_grupo = 0
        total_grupos = self.largoLista(self.grupos)

        while indice_grupo < total_grupos:
            resultado_grupo = self.grupos[indice_grupo].obtener_clasificados()

            if isinstance(resultado_grupo, str):
                return resultado_grupo

            total_actual = self.largoLista(clasificados_iniciales)
            total_nuevo = total_actual + self.largoLista(resultado_grupo)

            nueva_lista = [0] * total_nuevo

            indice = 0
            while indice < total_actual:
                nueva_lista[indice] = clasificados_iniciales[indice]
                indice += 1

            indice_resultado = 0
            while indice_resultado < self.largoLista(resultado_grupo):
                nueva_lista[total_actual + indice_resultado] = resultado_grupo[indice_resultado]
                indice_resultado += 1

            clasificados_iniciales = nueva_lista

            indice_grupo += 1

        equipos_actuales = clasificados_iniciales

        while self.largoLista(equipos_actuales) > 1:
            if self.largoLista(equipos_actuales) == 16:
                nombre_ronda = "Octavos de Final"
            elif self.largoLista(equipos_actuales) == 8:
                nombre_ronda = "Cuartos de Final"
            elif self.largoLista(equipos_actuales) == 4:
                nombre_ronda = "Semifinales"
            elif self.largoLista(equipos_actuales) == 2:
                nombre_ronda = "Final"
            else:
                nombre_ronda = "Ronda Eliminatoria"

            fase_actual = self.armar_fase_eliminatoria(nombre_ronda, equipos_actuales)

            if isinstance(fase_actual, str):
                return fase_actual

            resultado_eliminatoria = self.jugar_fase_eliminatoria(fase_actual)

            if isinstance(resultado_eliminatoria, str):
                return resultado_eliminatoria

            equipos_actuales = resultado_eliminatoria

        self.campeon = equipos_actuales[0]
        return self.campeon

        
    """
    Nombre: mostrar_tabla_general
    Entradas: ninguna
    Salidas: muestra las tablas de posiciones de todos los grupos
    Restricciones:
        deben existir grupos creados
    """
    def mostrar_tabla_general(self):
        total_grupos = self.largoLista(self.grupos)

        if total_grupos == 0:
            return "Error: No hay grupos creados"

        indice = 0
        while indice < total_grupos:
            print("Tabla del", self.grupos[indice].nombre_grupo)
            self.grupos[indice].mostrar_tabla()
            print(" ")
            indice += 1

        return "Tablas mostradas correctamente"

    """
    Nombre: generar_reporte
    Entradas: ninguna
    Salidas: genera el archivo de estadísticas generales del torneo
    Restricciones:
        debe poder crear y escribir el archivo
    """
    def generar_reporte(self):
        archivo = open("reporte_mundial.txt", "w")

        archivo.write("REPORTE DEL TORNEO\n")
        archivo.write("Nombre: " + self.nombre + "\n")
        archivo.write("Año: " + str(self.anio) + "\n")
        archivo.write("Selecciones registradas: " + str(self.largoLista(self.selecciones)) + "\n")
        archivo.write("Grupos creados: " + str(self.largoLista(self.grupos)) + "\n")

        if self.campeon is not None:
            archivo.write("Campeón: " + self.campeon.codigo_equipo + "\n")
        else:
            archivo.write("Campeón: Sin definir\n")

        archivo.close()

        return "Reporte generado correctamente"

    """
    Nombre: guardar_datos
    Entradas: ninguna
    Salidas: escribe los 6 archivos txt con la información actual
    Restricciones: ninguna
    """
    def guardar_datos(self):
        archivo_paises = open("paises.txt", "w", encoding="utf-8")
        indice = 0
        total_p = self.largoLista(self.paises)
        while indice < total_p:
            p = self.paises[indice]
            archivo_paises.write(p.codigo_fifa + "|" + p.nombre + "|" + p.continente + "|" + str(p.ranking_fifa) + "\n")
            indice += 1
        archivo_paises.close()

        archivo_selecciones = open("selecciones.txt", "w", encoding="utf-8")
        indice = 0
        total_s = self.largoLista(self.selecciones)
        while indice < total_s:
            s = self.selecciones[indice]
            archivo_selecciones.write(s.codigo_equipo + "|" + s.pais.codigo_fifa + "|" + s.entrenador.nombre + "|" + s.entrenador.apellido + "|" + s.entrenador.fecha_nacimiento + "|" + s.entrenador.nacionalidad + "|" + s.entrenador.licencia + "|" + str(s.entrenador.experiencia_anios) + "|" + s.entrenador.sistema_juego + "|" + str(s.fuerza_equipo) + "|" + str(s.total_goles_favor) + "|" + str(s.total_goles_contra) + "|" + str(s.total_tarjetas_amarillas) + "|" + str(s.total_tarjetas_rojas) + "\n")
            indice += 1
        archivo_selecciones.close()

        archivo_jugadores = open("jugadores.txt", "w", encoding="utf-8")
        indice_s = 0
        while indice_s < total_s:
            s = self.selecciones[indice_s]
            indice_j = 0
            total_j = self.largoLista(s.jugadores)
            while indice_j < total_j:
                f = s.jugadores[indice_j]
                archivo_jugadores.write(s.codigo_equipo + "|" + f.nombre + "|" + f.apellido + "|" + f.fecha_nacimiento + "|" + f.nacionalidad + "|" + str(f.dorsal) + "|" + f.posicion + "|" + str(f.total_tarjetas_amarillas) + "|" + str(f.total_tarjetas_rojas) + "|" + str(f.goles) + "|" + str(f.asistencias) + "|" + str(f.puntaje_individual) + "\n")
                indice_j += 1
            indice_s += 1
        archivo_jugadores.close()

        archivo_partidos = open("partidos.txt", "w", encoding="utf-8")
        indice_g = 0
        total_g = self.largoLista(self.grupos)
        while indice_g < total_g:
            grupo = self.grupos[indice_g]
            indice_p = 0
            total_partidos = self.largoLista(grupo.partidos)
            while indice_p < total_partidos:
                p = grupo.partidos[indice_p]
                penales1 = p.penales_equipo1
                penales2 = p.penales_equipo2
                if penales1 is None:
                    penales1 = ""
                if penales2 is None:
                    penales2 = ""
                archivo_partidos.write(p.fase + "|" + p.equipo_1.codigo_equipo + "|" + str(p.goles_equipo1) + "|" + str(p.goles_equipo2) + "|" + p.equipo_2.codigo_equipo + "|" + p.fecha + "|" + str(penales1) + "|" + str(penales2) + "\n")
                indice_p += 1
            indice_g += 1

        indice_f = 0
        total_f = self.largoLista(self.fases)
        while indice_f < total_f:
            fase = self.fases[indice_f]
            indice_p = 0
            total_partidos = self.largoLista(fase.partidos)
            while indice_p < total_partidos:
                p = fase.partidos[indice_p]
                penales1 = p.penales_equipo1
                penales2 = p.penales_equipo2
                if penales1 is None:
                    penales1 = ""
                if penales2 is None:
                    penales2 = ""
                archivo_partidos.write(p.fase + "|" + p.equipo_1.codigo_equipo + "|" + str(p.goles_equipo1) + "|" + str(p.goles_equipo2) + "|" + p.equipo_2.codigo_equipo + "|" + p.fecha + "|" + str(penales1) + "|" + str(penales2) + "\n")
                indice_p += 1
            indice_f += 1
        archivo_partidos.close()

        lista_goleadores = []
        indice_s = 0
        while indice_s < total_s:
            s = self.selecciones[indice_s]
            indice_j = 0
            while indice_j < self.largoLista(s.jugadores):
                lista_goleadores = lista_goleadores + [s.jugadores[indice_j]]
                indice_j += 1
            indice_s += 1

        total_goleadores = self.largoLista(lista_goleadores)
        pasada = 0
        while pasada < total_goleadores:
            indice_orden = 0
            while indice_orden < total_goleadores - pasada - 1:
                if lista_goleadores[indice_orden].goles < lista_goleadores[indice_orden + 1].goles:
                    temporal = lista_goleadores[indice_orden]
                    lista_goleadores[indice_orden] = lista_goleadores[indice_orden + 1]
                    lista_goleadores[indice_orden + 1] = temporal
                indice_orden += 1
            pasada += 1

        archivo_goleadores = open("ranking_goleadores.txt", "w", encoding="utf-8")
        indice = 0
        while indice < self.largoLista(lista_goleadores):
            jug = lista_goleadores[indice]
            archivo_goleadores.write(jug.nombre + "|" + jug.apellido + "|" + str(jug.dorsal) + "|" + jug.posicion + "|" + str(jug.goles) + "|" + str(jug.asistencias) + "\n")
            indice += 1
        archivo_goleadores.close()

        lista_selecciones = []
        indice = 0
        while indice < total_s:
            lista_selecciones = lista_selecciones + [self.selecciones[indice]]
            indice += 1
        total_ranking = self.largoLista(lista_selecciones)
        pasada = 0
        while pasada < total_ranking:
            indice_orden = 0
            while indice_orden < total_ranking - pasada - 1:
                seleccion_actual = lista_selecciones[indice_orden]
                seleccion_siguiente = lista_selecciones[indice_orden + 1]
                diferencia_actual = seleccion_actual.total_goles_favor - seleccion_actual.total_goles_contra
                diferencia_siguiente = seleccion_siguiente.total_goles_favor - seleccion_siguiente.total_goles_contra
                cambiar = False
                if diferencia_actual < diferencia_siguiente:
                    cambiar = True
                elif diferencia_actual == diferencia_siguiente:
                    if seleccion_actual.total_goles_favor < seleccion_siguiente.total_goles_favor:
                        cambiar = True
                    elif seleccion_actual.total_goles_favor == seleccion_siguiente.total_goles_favor:
                        if seleccion_actual.fuerza_equipo < seleccion_siguiente.fuerza_equipo:
                            cambiar = True
                if cambiar:
                    temporal = lista_selecciones[indice_orden]
                    lista_selecciones[indice_orden] = lista_selecciones[indice_orden + 1]
                    lista_selecciones[indice_orden + 1] = temporal
                indice_orden += 1
            pasada += 1

        archivo_ranking_sel = open("ranking_selecciones.txt", "w", encoding="utf-8")
        indice = 0
        while indice < self.largoLista(lista_selecciones):
            sel = lista_selecciones[indice]
            diferencia = sel.total_goles_favor - sel.total_goles_contra
            archivo_ranking_sel.write(sel.codigo_equipo + "|" + sel.pais.nombre + "|" + str(sel.total_goles_favor) + "|" + str(sel.total_goles_contra) + "|" + str(diferencia) + "|" + str(sel.fuerza_equipo) + "\n")
            indice += 1
        archivo_ranking_sel.close()

        return "Datos guardados correctamente en archivos de texto"

    """
    Nombre: cargar_datos
    Entradas: ninguna
    Salidas: lee los archivos txt y restaura los datos(objetos) manualmente
    Restricciones: ninguna
    """
    def cargar_datos(self):
        try:
            self.paises = []
            self.selecciones = []
            self.grupos = []
            self.fases = []
            self.campeon = None

            archivo = open("paises.txt", "r", encoding="utf-8")
            lineas = archivo.readlines()
            archivo.close()
            indice = 0
            while indice < self.largoLista(lineas):
                datos = lineas[indice].strip().split("|")
                if self.largoLista(datos) >= 4:
                    self.registrar_pais(Pais(datos[0], datos[1], datos[2], int(datos[3])))
                indice += 1

            archivo = open("selecciones.txt", "r", encoding="utf-8")
            lineas = archivo.readlines()
            archivo.close()
            indice = 0
            while indice < self.largoLista(lineas):
                datos = lineas[indice].strip().split("|")
                if self.largoLista(datos) >= 5:
                    pais_encontrado = None
                    indice_p = 0
                    while indice_p < self.largoLista(self.paises):
                        if self.paises[indice_p].codigo_fifa == datos[1]:
                            pais_encontrado = self.paises[indice_p]
                        indice_p += 1

                    if pais_encontrado is not None:
                        if self.largoLista(datos) >= 10:
                            entrenador = Entrenador(datos[2], datos[3], datos[4], datos[5], datos[6], int(datos[7]), datos[8])
                            fuerza = float(datos[9])
                        else:
                            entrenador = Entrenador(datos[2], datos[3], "No registrada", "No registrada", "Licencia Base", 5, "4-4-2")
                            fuerza = float(datos[4])
                        seleccion = Seleccion(datos[0], pais_encontrado, entrenador)
                        seleccion.fuerza_equipo = fuerza
                        if self.largoLista(datos) >= 14:
                            seleccion.total_goles_favor = int(datos[10])
                            seleccion.total_goles_contra = int(datos[11])
                            seleccion.total_tarjetas_amarillas = int(datos[12])
                            seleccion.total_tarjetas_rojas = int(datos[13])
                        self.registrar_seleccion(seleccion)
                indice += 1

            archivo = open("jugadores.txt", "r", encoding="utf-8")
            lineas = archivo.readlines()
            archivo.close()
            indice = 0
            while indice < self.largoLista(lineas):
                datos = lineas[indice].strip().split("|")
                if self.largoLista(datos) >= 12:
                    seleccion_encontrada = None
                    indice_s = 0
                    while indice_s < self.largoLista(self.selecciones):
                        if self.selecciones[indice_s].codigo_equipo == datos[0]:
                            seleccion_encontrada = self.selecciones[indice_s]
                        indice_s += 1
                    if seleccion_encontrada is not None:
                        futbolista = Futbolista(datos[1], datos[2], datos[3], datos[4], int(datos[5]), datos[6], int(datos[7]), int(datos[8]), int(datos[9]), int(datos[10]), int(datos[11]))
                        seleccion_encontrada.agregar_jugador(futbolista)
                indice += 1

            return "Datos recuperados correctamente de los archivos de texto."
        except FileNotFoundError:
            return "No se encontraron archivos de sesiones previas. Iniciando sistema limpio."
        except Exception as error:
            return "Error al cargar datos: " + str(error)

#--------------Interfaz gráfica-------------------#

class InterfazMundial:
    """
    Nombre: InterfazMundial
    Descripción: Interfaz gráfica del proyecto Copa Mundial.
    """
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Copa Mundial FIFA 2026")
        self.ventana.geometry("1180x720")
        self.ventana.minsize(1050, 650)

        self.color_fondo = "#071C2F"
        self.color_panel = "#123C69"
        self.color_panel_claro = "#1E5F8C"
        self.color_dorado = "#D8A31A"
        self.color_verde = "#0B6B43"
        self.color_rojo = "#A51C30"
        self.color_texto = "white"

        self.mundial = Mundial("Mundial FIFA 2026", 2026)
        self.equipos_eliminatoria_actuales = []
        self.texto_paises = None
        self.texto_jugadores = None
        self.texto_grupos = None
        self.texto_resultados = None
        self.texto_rankings = None

        self.imagen_copa = None
        self.cargar_imagen()

        self.crear_estructura_principal()
        self.mostrar_pantalla_principal()

    def cargar_imagen(self):
        try:
            self.imagen_copa = tk.PhotoImage(file="copa_mundial_campeon.png")
        except Exception:
            try:
                self.imagen_copa = tk.PhotoImage(file="copa_mundial.png")
            except Exception:
                self.imagen_copa = None

    def largoLista(self, lista):
        contador = 0
        for elemento in lista:
            contador += 1
        return contador

    def agregar_a_lista(self, lista, elemento):
        return lista + [elemento]

    def convertir_decimal_dos_digitos(self, numero):
        if not isinstance(numero, (int, float)):
            return str(numero)

        negativo = False
        if numero < 0:
            negativo = True
            numero = numero * -1

        numero_por_cien = numero * 100
        parte_entera = int(numero_por_cien)
        parte_decimal = numero_por_cien - parte_entera

        if parte_decimal >= 0.5:
            parte_entera += 1

        entero_principal = parte_entera // 100
        decimal_final = parte_entera - (entero_principal * 100)

        texto_decimal = str(decimal_final)
        if decimal_final < 10:
            texto_decimal = "0" + texto_decimal

        texto_final = str(entero_principal) + "." + texto_decimal
        if negativo == True:
            texto_final = "-" + texto_final

        return texto_final

    def existe_caja_texto(self, caja):
        if caja is None:
            return False
        return True

    def ordenar_goleadores_lista(self, jugadores):
        total = self.largoLista(jugadores)
        pasada = 0
        while pasada < total:
            indice = 0
            while indice < total - pasada - 1:
                jugador_actual = jugadores[indice]
                jugador_siguiente = jugadores[indice + 1]
                cambiar = False
                if jugador_actual.goles < jugador_siguiente.goles:
                    cambiar = True
                elif jugador_actual.goles == jugador_siguiente.goles:
                    if jugador_actual.asistencias < jugador_siguiente.asistencias:
                        cambiar = True
                    elif jugador_actual.asistencias == jugador_siguiente.asistencias:
                        if jugador_actual.puntaje_individual < jugador_siguiente.puntaje_individual:
                            cambiar = True
                if cambiar:
                    temporal = jugadores[indice]
                    jugadores[indice] = jugadores[indice + 1]
                    jugadores[indice + 1] = temporal
                indice += 1
            pasada += 1
        return jugadores

    def ordenar_selecciones_lista(self, selecciones):
        total = self.largoLista(selecciones)
        pasada = 0
        while pasada < total:
            indice = 0
            while indice < total - pasada - 1:
                seleccion_actual = selecciones[indice]
                seleccion_siguiente = selecciones[indice + 1]
                diferencia_actual = seleccion_actual.total_goles_favor - seleccion_actual.total_goles_contra
                diferencia_siguiente = seleccion_siguiente.total_goles_favor - seleccion_siguiente.total_goles_contra
                cambiar = False
                if diferencia_actual < diferencia_siguiente:
                    cambiar = True
                elif diferencia_actual == diferencia_siguiente:
                    if seleccion_actual.total_goles_favor < seleccion_siguiente.total_goles_favor:
                        cambiar = True
                    elif seleccion_actual.total_goles_favor == seleccion_siguiente.total_goles_favor:
                        if seleccion_actual.fuerza_equipo < seleccion_siguiente.fuerza_equipo:
                            cambiar = True
                if cambiar:
                    temporal = selecciones[indice]
                    selecciones[indice] = selecciones[indice + 1]
                    selecciones[indice + 1] = temporal
                indice += 1
            pasada += 1
        return selecciones

    def crear_estructura_principal(self):
        self.ventana.configure(bg=self.color_fondo)

        self.frame_general = tk.Frame(self.ventana, bg=self.color_fondo)
        self.frame_general.pack(fill="both", expand=True)

        self.frame_menu = tk.Frame(self.frame_general, bg="#04101F", width=245)
        self.frame_menu.pack(side="left", fill="y")
        self.frame_menu.pack_propagate(False)

        self.frame_contenido = tk.Frame(self.frame_general, bg=self.color_fondo)
        self.frame_contenido.pack(side="left", fill="both", expand=True)

        titulo = tk.Label(self.frame_menu, text="COPA\nMUNDIAL", bg="#04101F", fg=self.color_dorado, font=("Arial", 23, "bold"))
        titulo.pack(pady=25)

        subtitulo = tk.Label(self.frame_menu, text="FIFA 2026", bg="#04101F", fg="white", font=("Arial", 14, "bold"))
        subtitulo.pack(pady=5)

        self.crear_boton_menu("Inicio", self.mostrar_pantalla_principal)
        self.crear_boton_menu("Países y Selecciones", self.mostrar_paises_selecciones)
        self.crear_boton_menu("Entrenadores y Jugadores", self.mostrar_entrenadores_jugadores)
        self.crear_boton_menu("Configurar Mundial", self.mostrar_configuracion_mundial)
        self.crear_boton_menu("Jugar Mundial", self.mostrar_jugar_mundial)
        self.crear_boton_menu("Estadísticas / Rankings", self.mostrar_estadisticas_rankings)

        separador = tk.Label(self.frame_menu, text="Archivos", bg="#04101F", fg=self.color_dorado, font=("Arial", 11, "bold"))
        separador.pack(pady=(20, 5))

        self.crear_boton_menu("Guardar datos", self.guardar_datos_interfaz)
        self.crear_boton_menu("Cargar datos", self.cargar_datos_interfaz)
        self.crear_boton_menu("Datos de prueba", self.cargar_datos_prueba)

    def crear_boton_menu(self, texto, comando):
        boton = tk.Button(self.frame_menu, text=texto, command=comando, bg=self.color_panel, fg="white", activebackground=self.color_dorado, activeforeground="black", font=("Arial", 10, "bold"), relief="flat", cursor="hand2")
        boton.pack(fill="x", padx=14, pady=5, ipady=8)

    def limpiar_contenido(self):
        self.texto_paises = None
        self.texto_jugadores = None
        self.texto_grupos = None
        self.texto_resultados = None
        self.texto_rankings = None
        for widget in self.frame_contenido.winfo_children():
            widget.destroy()

    def crear_titulo(self, titulo, subtitulo):
        encabezado = tk.Frame(self.frame_contenido, bg=self.color_fondo)
        encabezado.pack(fill="x", padx=20, pady=(16, 8))

        etiqueta_titulo = tk.Label(encabezado, text=titulo, bg=self.color_fondo, fg=self.color_dorado, font=("Arial", 25, "bold"))
        etiqueta_titulo.pack(anchor="w")

        etiqueta_subtitulo = tk.Label(encabezado, text=subtitulo, bg=self.color_fondo, fg="white", font=("Arial", 11))
        etiqueta_subtitulo.pack(anchor="w", pady=(4, 0))

    def crear_panel(self, padre, titulo):
        panel = tk.LabelFrame(padre, text=titulo, bg=self.color_panel, fg=self.color_dorado, font=("Arial", 12, "bold"), labelanchor="n")
        panel.pack(fill="both", expand=True, padx=10, pady=10)
        return panel

    def crear_entrada(self, padre, texto):
        fila = tk.Frame(padre, bg=self.color_panel)
        fila.pack(fill="x", padx=10, pady=4)

        etiqueta = tk.Label(fila, text=texto, bg=self.color_panel, fg="white", font=("Arial", 10, "bold"), width=18, anchor="w")
        etiqueta.pack(side="left")

        entrada = tk.Entry(fila, font=("Arial", 10))
        entrada.pack(side="left", fill="x", expand=True, padx=5)
        return entrada

    def crear_combo(self, padre, texto, valores):
        fila = tk.Frame(padre, bg=self.color_panel)
        fila.pack(fill="x", padx=10, pady=4)

        etiqueta = tk.Label(fila, text=texto, bg=self.color_panel, fg="white", font=("Arial", 10, "bold"), width=18, anchor="w")
        etiqueta.pack(side="left")

        combo = ttk.Combobox(fila, values=valores, state="readonly", font=("Arial", 10))
        combo.pack(side="left", fill="x", expand=True, padx=5)
        if self.largoLista(valores) > 0:
            combo.current(0)
        return combo

    def crear_boton_accion(self, padre, texto, comando, color=None):
        if color is None:
            color = self.color_verde
        boton = tk.Button(padre, text=texto, command=comando, bg=color, fg="white", activebackground=self.color_dorado, activeforeground="black", font=("Arial", 10, "bold"), relief="flat", cursor="hand2")
        boton.pack(fill="x", padx=10, pady=6, ipady=6)
        return boton

    def crear_area_texto(self, padre):
        marco = tk.Frame(padre, bg=self.color_panel)
        marco.pack(fill="both", expand=True, padx=10, pady=10)

        barra = tk.Scrollbar(marco)
        barra.pack(side="right", fill="y")

        texto = tk.Text(marco, bg="#02111F", fg="white", insertbackground="white", font=("Consolas", 10), wrap="word", yscrollcommand=barra.set)
        texto.pack(side="left", fill="both", expand=True)
        barra.config(command=texto.yview)
        return texto

    def escribir_texto(self, area, texto):
        area.config(state="normal")
        area.delete("1.0", "end")
        area.insert("end", texto)
        area.config(state="normal")

    def mensaje(self, titulo, mensaje):
        messagebox.showinfo(titulo, mensaje)

    def mensaje_error(self, mensaje):
        messagebox.showerror("Error", mensaje)

    def obtener_entero(self, entrada, nombre):
        texto = entrada.get().strip()
        if texto == "":
            self.mensaje_error(nombre + " debe tener un valor entero")
            return None
        try:
            return int(texto)
        except Exception:
            self.mensaje_error(nombre + " debe ser un número entero")
            return None

    def obtener_entero_opcional(self, entrada, valor_defecto):
        texto = entrada.get().strip()
        if texto == "":
            return valor_defecto
        try:
            return int(texto)
        except Exception:
            return valor_defecto

    def obtener_codigo_combo(self, combo):
        texto = combo.get()
        partes = texto.split(" - ")
        if self.largoLista(partes) > 0:
            return partes[0]
        return texto

    def lista_paises_combo(self):
        valores = []
        indice = 0
        while indice < self.mundial.largoLista(self.mundial.paises):
            p = self.mundial.paises[indice]
            valores = valores + [p.codigo_fifa + " - " + p.nombre]
            indice += 1
        return valores

    def lista_selecciones_combo(self):
        valores = []
        indice = 0
        while indice < self.mundial.largoLista(self.mundial.selecciones):
            s = self.mundial.selecciones[indice]
            valores = valores + [s.codigo_equipo + " - " + s.pais.nombre]
            indice += 1
        return valores

    def buscar_pais(self, codigo):
        indice = 0
        while indice < self.mundial.largoLista(self.mundial.paises):
            if self.mundial.paises[indice].codigo_fifa == codigo:
                return self.mundial.paises[indice]
            indice += 1
        return None

    def buscar_seleccion(self, codigo):
        indice = 0
        while indice < self.mundial.largoLista(self.mundial.selecciones):
            if self.mundial.selecciones[indice].codigo_equipo == codigo:
                return self.mundial.selecciones[indice]
            indice += 1
        return None

    def buscar_jugador(self, seleccion, dorsal):
        indice = 0
        while indice < seleccion.largoLista(seleccion.jugadores):
            if seleccion.jugadores[indice].dorsal == dorsal:
                return seleccion.jugadores[indice]
            indice += 1
        return None

    def calcular_fuerzas_posibles(self):
        indice = 0
        while indice < self.mundial.largoLista(self.mundial.selecciones):
            s = self.mundial.selecciones[indice]
            if s.largoLista(s.jugadores) >= 11:
                s.calcular_fuerza_equipo()
            indice += 1

    def validar_selecciones_para_jugar(self):
        if self.mundial.largoLista(self.mundial.selecciones) < 2:
            return "Debe registrar al menos 2 selecciones."
        indice = 0
        while indice < self.mundial.largoLista(self.mundial.selecciones):
            s = self.mundial.selecciones[indice]
            if s.largoLista(s.jugadores) < 11:
                return "La selección " + s.codigo_equipo + " debe tener al menos 11 jugadores."
            indice += 1
        return "OK"

    def mostrar_pantalla_principal(self):
        self.limpiar_contenido()
        self.crear_titulo("Copa Mundial FIFA 2026", "Sistema orientado a objetos para gestionar y simular el torneo")

        panel = tk.Frame(self.frame_contenido, bg=self.color_fondo)
        panel.pack(fill="both", expand=True, padx=20, pady=10)

        panel_izq = tk.Frame(panel, bg=self.color_panel)
        panel_izq.pack(side="left", fill="both", expand=True, padx=10, pady=10)

        if self.imagen_copa is not None:
            etiqueta_img = tk.Label(panel_izq, image=self.imagen_copa, bg=self.color_panel)
            etiqueta_img.pack(pady=18)

        descripcion = "Bienvenido al sistema de Copa Mundial.\n\nDesde este menú se pueden registrar países, crear selecciones, asignar entrenadores y jugadores, crear grupos, simular partidos, avanzar fases eliminatorias, consultar rankings y guardar los datos en archivos de texto."
        etiqueta = tk.Label(panel_izq, text=descripcion, bg=self.color_panel, fg="white", font=("Arial", 13), justify="left", wraplength=520)
        etiqueta.pack(padx=25, pady=18, anchor="w")

        panel_der = tk.Frame(panel, bg=self.color_panel)
        panel_der.pack(side="left", fill="both", expand=True, padx=10, pady=10)

        resumen = self.obtener_resumen_general()
        tk.Label(panel_der, text="Resumen actual", bg=self.color_panel, fg=self.color_dorado, font=("Arial", 18, "bold")).pack(pady=15)
        tk.Label(panel_der, text=resumen, bg=self.color_panel, fg="white", font=("Consolas", 12), justify="left").pack(padx=20, pady=10, anchor="w")

        self.crear_boton_accion(panel_der, "Cargar datos de prueba", self.cargar_datos_prueba, self.color_panel_claro)
        self.crear_boton_accion(panel_der, "Ir a jugar mundial", self.mostrar_jugar_mundial, self.color_verde)

    def obtener_resumen_general(self):
        texto = "Países registrados: " + str(self.mundial.largoLista(self.mundial.paises)) + "\n"
        texto += "Selecciones registradas: " + str(self.mundial.largoLista(self.mundial.selecciones)) + "\n"
        texto += "Grupos creados: " + str(self.mundial.largoLista(self.mundial.grupos)) + "\n"
        texto += "Fases jugadas: " + str(self.mundial.largoLista(self.mundial.fases)) + "\n"
        if self.mundial.campeon is not None:
            texto += "Campeón: " + self.mundial.campeon.codigo_equipo + " - " + self.mundial.campeon.pais.nombre + "\n"
        else:
            texto += "Campeón: Sin definir\n"
        return texto

    def mostrar_paises_selecciones(self):
        self.limpiar_contenido()
        self.crear_titulo("Países y Selecciones", "Registre países participantes y cree selecciones nacionales asociadas")

        contenedor = tk.Frame(self.frame_contenido, bg=self.color_fondo)
        contenedor.pack(fill="both", expand=True, padx=12, pady=8)

        columna_izq = tk.Frame(contenedor, bg=self.color_fondo)
        columna_izq.pack(side="left", fill="both", expand=True)
        columna_der = tk.Frame(contenedor, bg=self.color_fondo)
        columna_der.pack(side="left", fill="both", expand=True)

        panel_pais = self.crear_panel(columna_izq, "Registrar / actualizar país")
        self.entrada_codigo_pais = self.crear_entrada(panel_pais, "Código FIFA")
        self.entrada_nombre_pais = self.crear_entrada(panel_pais, "Nombre")
        self.entrada_continente_pais = self.crear_entrada(panel_pais, "Continente")
        self.entrada_ranking_pais = self.crear_entrada(panel_pais, "Ranking FIFA")
        self.crear_boton_accion(panel_pais, "Registrar país", self.registrar_pais_interfaz)
        self.crear_boton_accion(panel_pais, "Actualizar país por código", self.actualizar_pais_interfaz, self.color_panel_claro)

        panel_seleccion = self.crear_panel(columna_der, "Crear selección")
        self.entrada_codigo_seleccion = self.crear_entrada(panel_seleccion, "Código selección")
        self.combo_pais_seleccion = self.crear_combo(panel_seleccion, "País asociado", self.lista_paises_combo())
        self.crear_boton_accion(panel_seleccion, "Crear selección", self.crear_seleccion_interfaz)

        panel_listado = self.crear_panel(self.frame_contenido, "Listado")
        self.texto_paises = self.crear_area_texto(panel_listado)
        self.actualizar_texto_paises()

    def registrar_pais_interfaz(self):
        codigo = self.entrada_codigo_pais.get().strip().upper()
        nombre = self.entrada_nombre_pais.get().strip()
        continente = self.entrada_continente_pais.get().strip()
        ranking = self.obtener_entero(self.entrada_ranking_pais, "Ranking FIFA")
        if ranking is None:
            return
        if codigo == "" or nombre == "" or continente == "":
            self.mensaje_error("Debe completar todos los datos del país")
            return
        if self.buscar_pais(codigo) is not None:
            self.mensaje_error("Ya existe un país con ese código FIFA")
            return

        pais = Pais(codigo, nombre, continente, ranking)
        resultado = self.mundial.registrar_pais(pais)
        self.mensaje("País", resultado)
        self.mostrar_paises_selecciones()

    def actualizar_pais_interfaz(self):
        codigo = self.entrada_codigo_pais.get().strip().upper()
        pais = self.buscar_pais(codigo)
        if pais is None:
            self.mensaje_error("No se encontró un país con ese código FIFA")
            return

        nombre = self.entrada_nombre_pais.get().strip()
        continente = self.entrada_continente_pais.get().strip()
        ranking_texto = self.entrada_ranking_pais.get().strip()
        ranking = 0
        if ranking_texto != "":
            try:
                ranking = int(ranking_texto)
            except Exception:
                self.mensaje_error("Ranking FIFA debe ser entero")
                return
        resultado = pais.actualizar_datos(nombre, "", continente, ranking)
        self.mensaje("País", resultado)
        self.mostrar_paises_selecciones()

    def crear_seleccion_interfaz(self):
        codigo = self.entrada_codigo_seleccion.get().strip().upper()
        codigo_pais = self.obtener_codigo_combo(self.combo_pais_seleccion)
        pais = self.buscar_pais(codigo_pais)
        if codigo == "":
            self.mensaje_error("Debe escribir el código de la selección")
            return
        if pais is None:
            self.mensaje_error("Debe registrar y seleccionar un país")
            return
        if self.buscar_seleccion(codigo) is not None:
            self.mensaje_error("Ya existe una selección con ese código")
            return

        entrenador_base = Entrenador("Sin", "Entrenador", "00/00/0000", pais.nombre, "Base", 0, "4-4-2")
        seleccion = Seleccion(codigo, pais, entrenador_base)
        resultado = self.mundial.registrar_seleccion(seleccion)
        self.mensaje("Selección", resultado)
        self.mostrar_paises_selecciones()

    def actualizar_texto_paises(self):
        texto = "PAÍSES REGISTRADOS\n"
        texto += "==================\n"
        indice = 0
        while indice < self.mundial.largoLista(self.mundial.paises):
            p = self.mundial.paises[indice]
            texto += p.codigo_fifa + " | " + p.nombre + " | " + p.continente + " | Ranking: " + str(p.ranking_fifa) + "\n"
            indice += 1

        texto += "\nSELECCIONES REGISTRADAS\n"
        texto += "========================\n"
        indice = 0
        while indice < self.mundial.largoLista(self.mundial.selecciones):
            s = self.mundial.selecciones[indice]
            texto += s.codigo_equipo + " | País: " + s.pais.nombre + " | Entrenador: " + s.entrenador.nombre + " " + s.entrenador.apellido + " | Jugadores: " + str(s.largoLista(s.jugadores)) + " | Fuerza: " + self.convertir_decimal_dos_digitos(s.fuerza_equipo) + "\n"
            indice += 1

        self.escribir_texto(self.texto_paises, texto)

    def mostrar_entrenadores_jugadores(self):
        self.limpiar_contenido()
        self.crear_titulo("Entrenadores y Jugadores", "Asigne entrenadores y gestione la plantilla de cada selección")

        contenedor = tk.Frame(self.frame_contenido, bg=self.color_fondo)
        contenedor.pack(fill="both", expand=True, padx=12, pady=8)

        parte_superior = tk.Frame(contenedor, bg=self.color_fondo)
        parte_superior.pack(fill="x")

        panel_selector = self.crear_panel(parte_superior, "Selección")
        self.combo_seleccion_personas = self.crear_combo(panel_selector, "Selección", self.lista_selecciones_combo())
        self.crear_boton_accion(panel_selector, "Ver plantilla", self.actualizar_texto_jugadores, self.color_panel_claro)

        parte_forms = tk.Frame(contenedor, bg=self.color_fondo)
        parte_forms.pack(fill="both", expand=True)

        columna_izq = tk.Frame(parte_forms, bg=self.color_fondo)
        columna_izq.pack(side="left", fill="both", expand=True)
        columna_der = tk.Frame(parte_forms, bg=self.color_fondo)
        columna_der.pack(side="left", fill="both", expand=True)

        panel_entrenador = self.crear_panel(columna_izq, "Asignar entrenador")
        self.entrada_nombre_entrenador = self.crear_entrada(panel_entrenador, "Nombre")
        self.entrada_apellido_entrenador = self.crear_entrada(panel_entrenador, "Apellido")
        self.entrada_fecha_entrenador = self.crear_entrada(panel_entrenador, "Fecha nac.")
        self.entrada_nacionalidad_entrenador = self.crear_entrada(panel_entrenador, "Nacionalidad")
        self.entrada_licencia_entrenador = self.crear_entrada(panel_entrenador, "Licencia")
        self.entrada_experiencia_entrenador = self.crear_entrada(panel_entrenador, "Experiencia")
        self.entrada_sistema_entrenador = self.crear_entrada(panel_entrenador, "Sistema juego")
        self.crear_boton_accion(panel_entrenador, "Asignar entrenador", self.asignar_entrenador_interfaz)

        panel_jugador = self.crear_panel(columna_der, "Registrar / actualizar jugador")
        self.entrada_nombre_jugador = self.crear_entrada(panel_jugador, "Nombre")
        self.entrada_apellido_jugador = self.crear_entrada(panel_jugador, "Apellido")
        self.entrada_fecha_jugador = self.crear_entrada(panel_jugador, "Fecha nac.")
        self.entrada_nacionalidad_jugador = self.crear_entrada(panel_jugador, "Nacionalidad")
        self.entrada_dorsal_jugador = self.crear_entrada(panel_jugador, "Dorsal")
        self.combo_posicion_jugador = self.crear_combo(panel_jugador, "Posición", ["Portero", "Defensa", "Mediocampista", "Delantero"])
        self.entrada_puntaje_jugador = self.crear_entrada(panel_jugador, "Puntaje 1-100")
        self.entrada_goles_jugador = self.crear_entrada(panel_jugador, "Goles")
        self.entrada_asistencias_jugador = self.crear_entrada(panel_jugador, "Asistencias")
        self.entrada_amarillas_jugador = self.crear_entrada(panel_jugador, "Amarillas")
        self.entrada_rojas_jugador = self.crear_entrada(panel_jugador, "Rojas")
        self.crear_boton_accion(panel_jugador, "Agregar jugador", self.agregar_jugador_interfaz)
        self.crear_boton_accion(panel_jugador, "Actualizar jugador por dorsal", self.actualizar_jugador_interfaz, self.color_panel_claro)
        self.crear_boton_accion(panel_jugador, "Eliminar jugador por dorsal", self.eliminar_jugador_interfaz, self.color_rojo)
        self.crear_boton_accion(panel_jugador, "Calcular fuerza de equipo", self.calcular_fuerza_interfaz, self.color_dorado)

        panel_lista = self.crear_panel(self.frame_contenido, "Plantilla")
        self.texto_jugadores = self.crear_area_texto(panel_lista)
        self.actualizar_texto_jugadores()

    def obtener_seleccion_personas(self):
        codigo = self.obtener_codigo_combo(self.combo_seleccion_personas)
        return self.buscar_seleccion(codigo)

    def asignar_entrenador_interfaz(self):
        seleccion = self.obtener_seleccion_personas()
        if seleccion is None:
            self.mensaje_error("Debe seleccionar una selección")
            return
        experiencia = self.obtener_entero(self.entrada_experiencia_entrenador, "Experiencia")
        if experiencia is None:
            return
        nombre = self.entrada_nombre_entrenador.get().strip()
        apellido = self.entrada_apellido_entrenador.get().strip()
        fecha = self.entrada_fecha_entrenador.get().strip()
        nacionalidad = self.entrada_nacionalidad_entrenador.get().strip()
        licencia = self.entrada_licencia_entrenador.get().strip()
        sistema = self.entrada_sistema_entrenador.get().strip()
        if nombre == "" or apellido == "" or fecha == "" or nacionalidad == "" or licencia == "" or sistema == "":
            self.mensaje_error("Debe completar todos los datos del entrenador")
            return

        entrenador = Entrenador(nombre, apellido, fecha, nacionalidad, licencia, experiencia, sistema)
        resultado = seleccion.asignar_entrenador(entrenador)
        if seleccion.largoLista(seleccion.jugadores) >= 11:
            seleccion.calcular_fuerza_equipo()
        self.mensaje("Entrenador", resultado)
        self.actualizar_texto_jugadores()

    def agregar_jugador_interfaz(self):
        seleccion = self.obtener_seleccion_personas()
        if seleccion is None:
            self.mensaje_error("Debe seleccionar una selección")
            return
        dorsal = self.obtener_entero(self.entrada_dorsal_jugador, "Dorsal")
        puntaje = self.obtener_entero(self.entrada_puntaje_jugador, "Puntaje")
        if dorsal is None or puntaje is None:
            return

        nombre = self.entrada_nombre_jugador.get().strip()
        apellido = self.entrada_apellido_jugador.get().strip()
        fecha = self.entrada_fecha_jugador.get().strip()
        nacionalidad = self.entrada_nacionalidad_jugador.get().strip()
        posicion = self.combo_posicion_jugador.get()
        goles = self.obtener_entero_opcional(self.entrada_goles_jugador, 0)
        asistencias = self.obtener_entero_opcional(self.entrada_asistencias_jugador, 0)
        amarillas = self.obtener_entero_opcional(self.entrada_amarillas_jugador, 0)
        rojas = self.obtener_entero_opcional(self.entrada_rojas_jugador, 0)

        if nombre == "" or apellido == "" or fecha == "" or nacionalidad == "" or posicion == "":
            self.mensaje_error("Debe completar los datos principales del jugador")
            return

        jugador = Futbolista(nombre, apellido, fecha, nacionalidad, dorsal, posicion, amarillas, rojas, goles, asistencias, puntaje)
        resultado = seleccion.agregar_jugador(jugador)
        if resultado == "Jugador agregado correctamente" and seleccion.largoLista(seleccion.jugadores) >= 11:
            seleccion.calcular_fuerza_equipo()
        self.mensaje("Jugador", resultado)
        self.actualizar_texto_jugadores()

    def actualizar_jugador_interfaz(self):
        seleccion = self.obtener_seleccion_personas()
        if seleccion is None:
            self.mensaje_error("Debe seleccionar una selección")
            return
        dorsal = self.obtener_entero(self.entrada_dorsal_jugador, "Dorsal")
        if dorsal is None:
            return
        jugador = self.buscar_jugador(seleccion, dorsal)
        if jugador is None:
            self.mensaje_error("No se encontró un jugador con ese dorsal")
            return

        if self.entrada_nombre_jugador.get().strip() != "":
            jugador.nombre = self.entrada_nombre_jugador.get().strip()
        if self.entrada_apellido_jugador.get().strip() != "":
            jugador.apellido = self.entrada_apellido_jugador.get().strip()
        if self.entrada_fecha_jugador.get().strip() != "":
            jugador.fecha_nacimiento = self.entrada_fecha_jugador.get().strip()
        if self.entrada_nacionalidad_jugador.get().strip() != "":
            jugador.nacionalidad = self.entrada_nacionalidad_jugador.get().strip()

        posicion = self.combo_posicion_jugador.get()
        puntaje = self.obtener_entero_opcional(self.entrada_puntaje_jugador, 0)
        goles = self.obtener_entero_opcional(self.entrada_goles_jugador, 0)
        asistencias = self.obtener_entero_opcional(self.entrada_asistencias_jugador, 0)
        amarillas = self.obtener_entero_opcional(self.entrada_amarillas_jugador, 0)
        rojas = self.obtener_entero_opcional(self.entrada_rojas_jugador, 0)
        resultado = jugador.actualizar_datos(0, posicion, amarillas, rojas, goles, asistencias, puntaje)
        if seleccion.largoLista(seleccion.jugadores) >= 11:
            seleccion.calcular_fuerza_equipo()
        self.mensaje("Jugador", resultado)
        self.actualizar_texto_jugadores()

    def eliminar_jugador_interfaz(self):
        seleccion = self.obtener_seleccion_personas()
        if seleccion is None:
            self.mensaje_error("Debe seleccionar una selección")
            return
        dorsal = self.obtener_entero(self.entrada_dorsal_jugador, "Dorsal")
        if dorsal is None:
            return
        resultado = seleccion.eliminar_jugador(dorsal)
        if seleccion.largoLista(seleccion.jugadores) >= 11:
            seleccion.calcular_fuerza_equipo()
        else:
            seleccion.fuerza_equipo = 0
        self.mensaje("Jugador", resultado)
        self.actualizar_texto_jugadores()

    def calcular_fuerza_interfaz(self):
        seleccion = self.obtener_seleccion_personas()
        if seleccion is None:
            self.mensaje_error("Debe seleccionar una selección")
            return
        resultado = seleccion.calcular_fuerza_equipo()
        self.mensaje("Fuerza", resultado)
        self.actualizar_texto_jugadores()

    def actualizar_texto_jugadores(self):
        if self.existe_caja_texto(self.texto_jugadores) == False:
            return
        seleccion = self.obtener_seleccion_personas()
        texto = ""
        if seleccion is None:
            texto = "No hay selección seleccionada.\n"
            self.escribir_texto(self.texto_jugadores, texto)
            return

        texto += "SELECCIÓN: " + seleccion.codigo_equipo + " - " + seleccion.pais.nombre + "\n"
        texto += "Entrenador: " + seleccion.entrenador.nombre + " " + seleccion.entrenador.apellido + " | Licencia: " + seleccion.entrenador.licencia + " | Sistema: " + seleccion.entrenador.sistema_juego + "\n"
        texto += "Fuerza del equipo: " + self.convertir_decimal_dos_digitos(seleccion.fuerza_equipo) + "\n"
        texto += "Jugadores: " + str(seleccion.largoLista(seleccion.jugadores)) + "\n\n"
        texto += "Dorsal | Nombre | Posición | Puntaje | Goles | Asistencias | TA | TR\n"
        texto += "=====================================================================\n"
        indice = 0
        while indice < seleccion.largoLista(seleccion.jugadores):
            j = seleccion.jugadores[indice]
            texto += str(j.dorsal) + " | " + j.nombre + " " + j.apellido + " | " + j.posicion + " | " + str(j.puntaje_individual) + " | " + str(j.goles) + " | " + str(j.asistencias) + " | " + str(j.total_tarjetas_amarillas) + " | " + str(j.total_tarjetas_rojas) + "\n"
            indice += 1
        self.escribir_texto(self.texto_jugadores, texto)

    def mostrar_configuracion_mundial(self):
        self.limpiar_contenido()
        self.crear_titulo("Configuración del Mundial", "Cree los grupos y revise la distribución de selecciones")

        contenedor = tk.Frame(self.frame_contenido, bg=self.color_fondo)
        contenedor.pack(fill="both", expand=True, padx=12, pady=8)

        panel_config = self.crear_panel(contenedor, "Crear grupos")
        self.entrada_cantidad_grupos = self.crear_entrada(panel_config, "Cantidad de grupos")
        self.entrada_cantidad_grupos.insert(0, "2")
        self.crear_boton_accion(panel_config, "Crear grupos", self.crear_grupos_interfaz)
        self.crear_boton_accion(panel_config, "Calcular fuerzas de equipos", self.calcular_todas_fuerzas_interfaz, self.color_panel_claro)
        self.crear_boton_accion(panel_config, "Reiniciar torneo", self.reiniciar_torneo_interfaz, self.color_rojo)

        panel_grupos = self.crear_panel(contenedor, "Grupos formados")
        self.texto_grupos = self.crear_area_texto(panel_grupos)
        self.actualizar_texto_grupos()

    def calcular_todas_fuerzas_interfaz(self):
        self.calcular_fuerzas_posibles()
        self.mensaje("Fuerzas", "Se calcularon las fuerzas de las selecciones que tienen al menos 11 jugadores")
        if self.existe_caja_texto(self.texto_grupos) == True:
            self.actualizar_texto_grupos()

    def crear_grupos_interfaz(self):
        validacion = self.validar_selecciones_para_jugar()
        if validacion != "OK":
            self.mensaje_error(validacion)
            return
        texto_cantidad = self.entrada_cantidad_grupos.get().strip()
        if texto_cantidad == "":
            total_selecciones = self.mundial.largoLista(self.mundial.selecciones)
            if total_selecciones >= 8:
                cantidad = 2
            else:
                cantidad = 1
        else:
            cantidad = self.obtener_entero(self.entrada_cantidad_grupos, "Cantidad de grupos")
            if cantidad is None:
                return
        self.calcular_fuerzas_posibles()
        resultado = self.mundial.crear_grupos(cantidad)
        self.equipos_eliminatoria_actuales = []
        self.mensaje("Grupos", resultado)
        self.actualizar_texto_grupos()

    def actualizar_texto_grupos(self):
        if self.existe_caja_texto(self.texto_grupos) == False:
            return
        texto = "GRUPOS DEL MUNDIAL\n"
        texto += "==================\n\n"
        if self.mundial.largoLista(self.mundial.grupos) == 0:
            texto += "No hay grupos creados.\n"
        indice = 0
        while indice < self.mundial.largoLista(self.mundial.grupos):
            grupo = self.mundial.grupos[indice]
            texto += grupo.nombre_grupo + "\n"
            texto += "------------------\n"
            indice_e = 0
            while indice_e < grupo.largoLista(grupo.equipos):
                s = grupo.equipos[indice_e]
                texto += s.codigo_equipo + " - " + s.pais.nombre + " | Fuerza: " + self.convertir_decimal_dos_digitos(s.fuerza_equipo) + " | Jugadores: " + str(s.largoLista(s.jugadores)) + "\n"
                indice_e += 1
            texto += "\n"
            indice += 1
        self.escribir_texto(self.texto_grupos, texto)

    def reiniciar_torneo_interfaz(self):
        self.mundial.grupos = []
        self.mundial.fases = []
        self.mundial.campeon = None
        self.equipos_eliminatoria_actuales = []
        indice = 0
        while indice < self.mundial.largoLista(self.mundial.selecciones):
            s = self.mundial.selecciones[indice]
            s.total_goles_favor = 0
            s.total_goles_contra = 0
            s.total_tarjetas_amarillas = 0
            s.total_tarjetas_rojas = 0
            indice += 1
        self.mensaje("Torneo", "Se reiniciaron grupos, fases y campeón")
        if self.existe_caja_texto(self.texto_grupos) == True:
            self.actualizar_texto_grupos()

    def mostrar_jugar_mundial(self):
        self.limpiar_contenido()
        self.crear_titulo("Jugar Mundial", "Simule la fase de grupos, avance las rondas eliminatorias y determine el campeón")

        contenedor = tk.Frame(self.frame_contenido, bg=self.color_fondo)
        contenedor.pack(fill="both", expand=True, padx=12, pady=8)

        panel_botones = self.crear_panel(contenedor, "Acciones del torneo")
        self.crear_boton_accion(panel_botones, "Simular fase de grupos", self.simular_fase_grupos_interfaz)
        self.crear_boton_accion(panel_botones, "Avanzar siguiente fase eliminatoria", self.avanzar_siguiente_fase_interfaz, self.color_panel_claro)
        self.crear_boton_accion(panel_botones, "Simular mundial completo", self.simular_mundial_completo_interfaz, self.color_dorado)
        self.crear_boton_accion(panel_botones, "Mostrar campeón", self.mostrar_campeon_interfaz, self.color_verde)
        self.crear_boton_accion(panel_botones, "Generar reporte", self.generar_reporte_interfaz, self.color_panel_claro)

        panel_resultados = self.crear_panel(contenedor, "Resultados")
        self.texto_resultados = self.crear_area_texto(panel_resultados)
        self.actualizar_texto_resultados()

    def grupos_ya_jugados(self):
        indice = 0
        while indice < self.mundial.largoLista(self.mundial.grupos):
            if self.mundial.grupos[indice].largoLista(self.mundial.grupos[indice].partidos) > 0:
                return True
            indice += 1
        return False

    def simular_fase_grupos_interfaz(self):
        validacion = self.validar_selecciones_para_jugar()
        if validacion != "OK":
            self.mensaje_error(validacion)
            return
        if self.mundial.largoLista(self.mundial.grupos) == 0:
            self.mensaje_error("Debe crear los grupos primero en Configurar Mundial")
            return
        if self.grupos_ya_jugados():
            self.mensaje_error("La fase de grupos ya fue simulada. Use Reiniciar torneo si desea jugar otra vez.")
            return
        self.calcular_fuerzas_posibles()
        resultado = self.mundial.jugar_fase_grupos()
        if resultado != "Fase de grupos jugada correctamente":
            self.mensaje_error(resultado)
            return
        self.mensaje("Fase de grupos", resultado)
        self.actualizar_texto_resultados()

    def obtener_clasificados_grupos_interfaz(self):
        clasificados = []
        indice = 0
        while indice < self.mundial.largoLista(self.mundial.grupos):
            resultado = self.mundial.grupos[indice].obtener_clasificados()
            if isinstance(resultado, str):
                return resultado
            indice_r = 0
            while indice_r < self.largoLista(resultado):
                clasificados = clasificados + [resultado[indice_r]]
                indice_r += 1
            indice += 1
        return clasificados

    def nombre_ronda(self, cantidad):
        if cantidad == 32:
            return "Dieciseisavos de Final"
        elif cantidad == 16:
            return "Octavos de Final"
        elif cantidad == 8:
            return "Cuartos de Final"
        elif cantidad == 4:
            return "Semifinales"
        elif cantidad == 2:
            return "Final"
        return "Ronda Eliminatoria"

    def avanzar_siguiente_fase_interfaz(self):
        if self.mundial.largoLista(self.mundial.grupos) == 0:
            self.mensaje_error("Debe crear grupos y jugar la fase de grupos primero")
            return
        if not self.grupos_ya_jugados():
            self.mensaje_error("Debe simular la fase de grupos primero")
            return

        if self.largoLista(self.equipos_eliminatoria_actuales) == 0:
            resultado = self.obtener_clasificados_grupos_interfaz()
            if isinstance(resultado, str):
                self.mensaje_error(resultado)
                return
            self.equipos_eliminatoria_actuales = resultado

        if self.largoLista(self.equipos_eliminatoria_actuales) == 1:
            self.mundial.campeon = self.equipos_eliminatoria_actuales[0]
            self.mostrar_campeon_interfaz()
            return

        nombre = self.nombre_ronda(self.largoLista(self.equipos_eliminatoria_actuales))
        fase = self.mundial.armar_fase_eliminatoria(nombre, self.equipos_eliminatoria_actuales)
        if isinstance(fase, str):
            self.mensaje_error(fase)
            return
        resultado = self.mundial.jugar_fase_eliminatoria(fase)
        if isinstance(resultado, str):
            self.mensaje_error(resultado)
            return
        self.equipos_eliminatoria_actuales = resultado

        if self.largoLista(self.equipos_eliminatoria_actuales) == 1:
            self.mundial.campeon = self.equipos_eliminatoria_actuales[0]
            self.mostrar_campeon_interfaz()
        else:
            self.mensaje("Fase", nombre + " jugada correctamente")
        self.actualizar_texto_resultados()

    def simular_mundial_completo_interfaz(self):
        validacion = self.validar_selecciones_para_jugar()
        if validacion != "OK":
            self.mensaje_error(validacion)
            return
        if self.mundial.largoLista(self.mundial.grupos) == 0:
            total = self.mundial.largoLista(self.mundial.selecciones)
            if total >= 4:
                cantidad = total // 4
                if cantidad < 2:
                    cantidad = 2
            else:
                cantidad = 2
            resultado = self.mundial.crear_grupos(cantidad)
            if resultado != "Grupos creados correctamente":
                self.mensaje_error(resultado)
                return
        if not self.grupos_ya_jugados():
            self.calcular_fuerzas_posibles()
            resultado = self.mundial.jugar_fase_grupos()
            if resultado != "Fase de grupos jugada correctamente":
                self.mensaje_error(resultado)
                return

        while self.mundial.campeon is None:
            antes = self.largoLista(self.equipos_eliminatoria_actuales)
            self.avanzar_siguiente_fase_interfaz()
            despues = self.largoLista(self.equipos_eliminatoria_actuales)
            if self.mundial.campeon is not None:
                break
            if antes == despues and despues == 0:
                break
        self.actualizar_texto_resultados()

    def texto_partido(self, partido):
        texto = partido.equipo_1.codigo_equipo + " " + str(partido.goles_equipo1) + " - " + str(partido.goles_equipo2) + " " + partido.equipo_2.codigo_equipo
        penales1 = partido.penales_equipo1
        penales2 = partido.penales_equipo2
        if penales1 is not None and penales2 is not None:
            texto += " (Penales: " + str(penales1) + " - " + str(penales2) + ")"
        return texto

    def actualizar_texto_resultados(self):
        if self.existe_caja_texto(self.texto_resultados) == False:
            return
        texto = "RESULTADOS DEL TORNEO\n"
        texto += "======================\n\n"

        if self.mundial.largoLista(self.mundial.grupos) == 0:
            texto += "No hay grupos creados.\n"
        else:
            indice_g = 0
            while indice_g < self.mundial.largoLista(self.mundial.grupos):
                grupo = self.mundial.grupos[indice_g]
                texto += grupo.nombre_grupo + "\n"
                texto += "------------------\n"
                indice_p = 0
                while indice_p < grupo.largoLista(grupo.partidos):
                    texto += self.texto_partido(grupo.partidos[indice_p]) + "\n"
                    indice_p += 1
                if grupo.largoLista(grupo.tabla_equipos) > 0:
                    texto += "\nTabla:\n"
                    indice_t = 0
                    while indice_t < grupo.largoLista(grupo.tabla_equipos):
                        s = grupo.tabla_equipos[indice_t]
                        texto += str(indice_t + 1) + ". " + s.codigo_equipo + " | Pts: " + str(grupo.tabla_puntos[indice_t]) + " | GF: " + str(grupo.tabla_goles_favor[indice_t]) + " | GC: " + str(grupo.tabla_goles_contra[indice_t]) + " | Dif: " + str(grupo.tabla_diferencia[indice_t]) + "\n"
                        indice_t += 1
                texto += "\n"
                indice_g += 1

        if self.mundial.largoLista(self.mundial.fases) > 0:
            texto += "FASES ELIMINATORIAS\n"
            texto += "===================\n"
            indice_f = 0
            while indice_f < self.mundial.largoLista(self.mundial.fases):
                fase = self.mundial.fases[indice_f]
                texto += "\n" + fase.nombre_fase + "\n"
                texto += "------------------\n"
                indice_p = 0
                while indice_p < fase.largoLista(fase.partidos):
                    texto += self.texto_partido(fase.partidos[indice_p]) + "\n"
                    indice_p += 1
                indice_f += 1

        if self.mundial.campeon is not None:
            texto += "\nCAMPEÓN: " + self.mundial.campeon.codigo_equipo + " - " + self.mundial.campeon.pais.nombre + "\n"

        self.escribir_texto(self.texto_resultados, texto)

    def mostrar_campeon_interfaz(self):
        if self.mundial.campeon is None:
            self.mensaje_error("Aún no hay campeón definido")
            return
        campeon = self.mundial.campeon
        ventana = tk.Toplevel(self.ventana)
        ventana.title("Campeón del Mundial")
        ventana.geometry("720x560")
        ventana.configure(bg=self.color_fondo)

        tk.Label(ventana, text="¡CAMPEÓN DEL MUNDIAL FIFA 2026!", bg=self.color_fondo, fg=self.color_dorado, font=("Arial", 22, "bold")).pack(pady=20)
        if self.imagen_copa is not None:
            tk.Label(ventana, image=self.imagen_copa, bg=self.color_fondo).pack(pady=10)
        tk.Label(ventana, text=campeon.codigo_equipo + " - " + campeon.pais.nombre, bg=self.color_fondo, fg="white", font=("Arial", 24, "bold")).pack(pady=15)
        tk.Label(ventana, text="Fuerza del equipo: " + self.convertir_decimal_dos_digitos(campeon.fuerza_equipo), bg=self.color_fondo, fg="white", font=("Arial", 13)).pack(pady=5)
        tk.Button(ventana, text="Cerrar", command=ventana.destroy, bg=self.color_rojo, fg="white", font=("Arial", 11, "bold"), relief="flat").pack(pady=20, ipadx=20, ipady=6)

    def generar_reporte_interfaz(self):
        resultado = self.mundial.generar_reporte()
        self.mensaje("Reporte", resultado + "\nArchivo: reporte_mundial.txt")

    def mostrar_estadisticas_rankings(self):
        self.limpiar_contenido()
        self.crear_titulo("Estadísticas y Rankings", "Consulte goleadores, desempeño de selecciones y datos generales")

        contenedor = tk.Frame(self.frame_contenido, bg=self.color_fondo)
        contenedor.pack(fill="both", expand=True, padx=12, pady=8)

        panel_botones = self.crear_panel(contenedor, "Acciones")
        self.crear_boton_accion(panel_botones, "Actualizar rankings", self.actualizar_rankings_interfaz)
        self.crear_boton_accion(panel_botones, "Guardar rankings en TXT", self.guardar_datos_interfaz, self.color_panel_claro)

        panel_texto = self.crear_panel(contenedor, "Rankings")
        self.texto_rankings = self.crear_area_texto(panel_texto)
        self.actualizar_rankings_interfaz()

    def actualizar_rankings_interfaz(self):
        if self.existe_caja_texto(self.texto_rankings) == False:
            return
        texto = "RANKING DE GOLEADORES\n"
        texto += "====================\n"
        jugadores = []
        indice_s = 0
        while indice_s < self.mundial.largoLista(self.mundial.selecciones):
            s = self.mundial.selecciones[indice_s]
            indice_j = 0
            while indice_j < s.largoLista(s.jugadores):
                jugadores = jugadores + [s.jugadores[indice_j]]
                indice_j += 1
            indice_s += 1
        jugadores = self.ordenar_goleadores_lista(jugadores)
        indice = 0
        while indice < self.largoLista(jugadores):
            j = jugadores[indice]
            texto += str(indice + 1) + ". " + j.nombre + " " + j.apellido + " | Goles: " + str(j.goles) + " | Asistencias: " + str(j.asistencias) + " | Puntaje: " + str(j.puntaje_individual) + "\n"
            indice += 1

        texto += "\nRANKING DE SELECCIONES\n"
        texto += "======================\n"
        selecciones = []
        indice = 0
        while indice < self.mundial.largoLista(self.mundial.selecciones):
            selecciones = selecciones + [self.mundial.selecciones[indice]]
            indice += 1
        selecciones = self.ordenar_selecciones_lista(selecciones)
        indice = 0
        while indice < self.largoLista(selecciones):
            s = selecciones[indice]
            diferencia = s.total_goles_favor - s.total_goles_contra
            texto += str(indice + 1) + ". " + s.codigo_equipo + " - " + s.pais.nombre + " | GF: " + str(s.total_goles_favor) + " | GC: " + str(s.total_goles_contra) + " | Dif: " + str(diferencia) + " | Fuerza: " + self.convertir_decimal_dos_digitos(s.fuerza_equipo) + "\n"
            indice += 1

        texto += "\nESTADÍSTICAS GENERALES\n"
        texto += "======================\n"
        seleccion_mas_goles = None
        indice = 0
        while indice < self.mundial.largoLista(self.mundial.selecciones):
            s = self.mundial.selecciones[indice]
            if seleccion_mas_goles is None or s.total_goles_favor > seleccion_mas_goles.total_goles_favor:
                seleccion_mas_goles = s
            indice += 1
        if seleccion_mas_goles is not None:
            texto += "Selección con más goles: " + seleccion_mas_goles.codigo_equipo + " - " + seleccion_mas_goles.pais.nombre + " (" + str(seleccion_mas_goles.total_goles_favor) + ")\n"
        if self.mundial.campeon is not None:
            texto += "Campeón: " + self.mundial.campeon.codigo_equipo + " - " + self.mundial.campeon.pais.nombre + "\n"
        else:
            texto += "Campeón: Sin definir\n"

        self.escribir_texto(self.texto_rankings, texto)

    def guardar_datos_interfaz(self):
        resultado = self.mundial.guardar_datos()
        self.mensaje("Guardar datos", resultado)

    def cargar_datos_interfaz(self):
        nuevo_mundial = Mundial("Mundial FIFA 2026", 2026)
        resultado = nuevo_mundial.cargar_datos()
        self.mundial = nuevo_mundial
        self.equipos_eliminatoria_actuales = []
        self.mensaje("Cargar datos", resultado)
        self.mostrar_pantalla_principal()

    def cargar_datos_prueba(self):
        self.mundial = Mundial("Mundial FIFA 2026", 2026)
        self.equipos_eliminatoria_actuales = []

        datos_paises = [
            ["ARG", "Argentina", "CONMEBOL", 1],
            ["BRA", "Brasil", "CONMEBOL", 5],
            ["CRC", "Costa Rica", "CONCACAF", 52],
            ["FRA", "Francia", "UEFA", 2],
            ["ESP", "España", "UEFA", 8],
            ["GER", "Alemania", "UEFA", 12],
            ["JPN", "Japón", "AFC", 18],
            ["USA", "Estados Unidos", "CONCACAF", 11]
        ]

        indice = 0
        while indice < self.largoLista(datos_paises):
            d = datos_paises[indice]
            pais = Pais(d[0], d[1], d[2], d[3])
            self.mundial.registrar_pais(pais)
            entrenador = Entrenador("Entrenador", d[1], "01/01/1970", d[1], "Pro", 10 + indice, "4-3-3")
            seleccion = Seleccion(d[0], pais, entrenador)
            self.mundial.registrar_seleccion(seleccion)
            jugador = 1
            while jugador <= 11:
                puntaje = 60 + random.randint(0, 35)
                if jugador == 1:
                    posicion = "Portero"
                elif jugador <= 5:
                    posicion = "Defensa"
                elif jugador <= 8:
                    posicion = "Mediocampista"
                else:
                    posicion = "Delantero"
                f = Futbolista("Jugador" + str(jugador), d[0], "01/01/2000", d[1], jugador, posicion, 0, 0, random.randint(0, 5), random.randint(0, 3), puntaje)
                seleccion.agregar_jugador(f)
                jugador += 1
            seleccion.calcular_fuerza_equipo()
            indice += 1

        self.mensaje("Datos de prueba", "Se cargaron 8 selecciones con 11 jugadores cada una")
        self.mostrar_pantalla_principal()


if __name__ == "__main__":
    ventana_principal = tk.Tk()
    aplicacion = InterfazMundial(ventana_principal)
    ventana_principal.mainloop()
