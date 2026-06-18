#Proyecto 3
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
Nombre: Persona
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



                
            
                






















        
        
        
