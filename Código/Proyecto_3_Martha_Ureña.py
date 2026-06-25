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
        if len(codigo_fifa) != 3:
            return False

        indice = 0
        while indice < 3:
            letra = codigo_fifa[indice]
            if letra < "A" or letra > "Z":
                if letra < "a" or letra > "z":
                    return False
            indice += 1

        try:
            letra_extra = codigo_fifa[3]
        except Exception:
            return True

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
    def __init__(self, id_partido, equipo_1, equipo_2, fase, fecha):
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
                partido = Partido(id_partido, self.equipos[indice_equipo_uno], self.equipos[indice_equipo_dos], self.nombre_grupo, self.fecha)
                resultado_partido = partido.simular()
                if resultado_partido != "Partido simulado correctamente":
                    return resultado_partido

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
            indice_equipo_comparado = indice_equipo + 1
            while indice_equipo_comparado < total_equipos:
                mejor_indice = indice_equipo
                if self.tabla_puntos[indice_equipo_comparado] > self.tabla_puntos[mejor_indice]:
                    mejor_indice = indice_equipo_comparado
                elif self.tabla_puntos[indice_equipo_comparado] == self.tabla_puntos[mejor_indice]:
                    if self.tabla_diferencia[indice_equipo_comparado] > self.tabla_diferencia[mejor_indice]:
                        mejor_indice = indice_equipo_comparado
                    elif self.tabla_diferencia[indice_equipo_comparado] == self.tabla_diferencia[mejor_indice]:
                        if self.tabla_goles_favor[indice_equipo_comparado] > self.tabla_goles_favor[mejor_indice]:
                            mejor_indice = indice_equipo_comparado

                

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
                indice_equipo_comparado += 1
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

                if not isinstance(fuerza1, int):
                    return "Error: fuerza_equipo de equipo_1 debe ser un número entero"
                if not isinstance(fuerza2, int):
                    return "Error: fuerza_equipo de equipo_2 debe ser un número entero"
                if fuerza1 > fuerza2:
                    partido.goles_equipo1 += 1
                elif fuerza2 > fuerza1:
                    partido.goles_equipo2 += 1
                else:
                    partido.goles_equipo1 += 1

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
            print("Juego", indice + 1, ":", partido.equipo_1.codigo_equipo, partido.goles_equipo1, "-", partido.goles_equipo2, partido.equipo_2.codigo_equipo)
            indice += 1

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
        self.campeon = ""

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
                resultado = self.crear_grupos(4)
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

        if self.campeon != "":
            archivo.write("Campeón: " + self.campeon.codigo_equipo + "\n")
        else:
            archivo.write("Campeón: Sin definir\n")

        archivo.close()

        return "Reporte generado correctamente"
