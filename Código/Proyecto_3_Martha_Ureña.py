#Proyecto 3
"""
*APUNTES:
-super() me lo enseño a usar el tutor de taller, me funciona para poder llamar el constructor de la clase que se heredan los atributos.
"""
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
        elif not isinstance(self.codigo_fifa, str):
            return "Error: El código fifa debe ser de tipo String"
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
            if codigo_fifa[0:1] == "" or codigo_fifa[1:2] == "" or codigo_fifa[2:3] == "" or codigo_fifa[3:4] != "":
                return "Error: El código fifa debe tener 3 letras"
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
                















        
        
        
