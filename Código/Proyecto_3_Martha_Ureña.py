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
        El parámetro de entrada debe ser una lista
    """
    def largoLista(self, lista):
        if not isinstance(lista, list):
            return "Error: El parámetro de entrada debe ser de tipo lista"
        else:
            contador = 0
            for elemento in lista:
                contador = contador + 1
            return contador
        
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
            return "Error: El país debe ser un objeto Pais"
        try:
            valor = self.entrenador.licencia
        except Exception:
            return "Error: El entrenador debe ser un objeto Entrenador"
        if not isinstance(self.jugadores, list):
            return "Error: Los jugadores deben estar en una lista"
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
        elif not isinstance(self.fuerza_equipo, int):
            return "Error: fuerza_equipo debe ser un número entero"
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
        try:
            valor = futbolista.dorsal
        except Exception:
            return "Error: El jugador debe ser un objeto Futbolista"
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
    def registar_resultado(self, goles_favor, goles_contra, tarjetas_am, tarjetas_rojas):
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
        if self.largoLista(self.jugadores) < 11:
            return "Error: La selección debe tener al menos 11 jugadores para calcular la fuerza"
        else:
            suma_puntaje = 0
            i = 0
            total = self.largoLista(self.jugadores)
            while i < total:
                suma_puntaje += self.jugadores[i].puntaje_individual
                i += 1
            self.fuerza_equipo = suma_puntaje + self.total_goles_favor - self.total_goles_contra
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
    def __init__(self, id_partido, equipo_1, equipo_2, goles_equipo1, holes_equipo2, fase, fecha):
        self.id_partido = id_partido
        self.equipo_1 = equipo_1
        self.equipo_2 = equipo_2
        self.goles_equipo1 = 0
        self.goles_equipo2 = 0
        self.fase = fase
        self.fecha = fecha

    """
    Nombre: simular
    Entradas: usa los atributos del partido y las selecciones
    Salidas:  ejecuta el algoritmo de simulación (sección 5) y asigna los goles de cada equipo
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
            return "Error: equipo_1 debe ser un objeto Seleccion válido"
        try:
            fuerza2 = self.equipo_2.fuerza_equipo
        except Exception:
            return "Error: equipo_2 debe ser un objeto Seleccion válido"
        
        if not isinstance(fuerza1, int):
            return "Error: fuerza_equipo de equipo_1 debe ser un número entero"
        if not isinstance(fuerza2, int):
            return "Error: fuerza_equipo de equipo_2 debe ser un número entero"
        
        if fuerza1 > fuerza2:
            self.goles_equipo1 = 2
            self.goles_equipo2 = 1
        elif fuerza1 < fuerza2:
            self.goles_equipo1 = 1
            self.goles_equipo2 = 2
        else:
            self.goles_equipo1 = 1
            self.goles_equipo2 = 1

        return "Partido simulado correctamente"

    """
    Nombre: generar_ganador
    Entradas: usa goles_equipo1 y goles_equipo2
    Salidas:  retorna la selección ganadora, o None en caso de empate (solo válido en fase de grupos)
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
            return None

    """
    Nombre: mostrar_resultado
    Entradas: usa los atributos del partido
    Salidas: muestra el resultado del partido en formato legible
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
            return "Error: equipo_1 debe ser un objeto Seleccion válido"
        try:
            codigo2 = self.equipo_2.codigo_equipo
        except Exception:
            return "Error: equipo_2 debe ser un objeto Seleccion válido"

        print("Resultado:", codigo1, self.goles_equipo1, "-", self.goles_equipo2, codigo2)
        
        





    
        
