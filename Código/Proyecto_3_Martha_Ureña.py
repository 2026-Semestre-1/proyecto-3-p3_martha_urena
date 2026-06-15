#Proyecto 3
"""
Nombre: Pais
Atributos: codigo_fifa, nombre, continente, ranking_fifa
Métodos: mostrar_datos, 
"""
class Pais:
    def __init__(self, codigo_fifa, nombre, continente, ranking_fifa):
        self.codigo_fifa = codigo_fifa
        self.nombre = nombre
        self.continente = continente
        self.ranking_fifa = ranking_fifa

    def mostrar_datos(self):
        if not isinstance(self.nombre, str):
            return "Error: El nombre debe ser de tipo String"
        elif not isinstance(self.codigo_fifa, str):
            return "Error: El código fifa debe ser de tipo String"
        elif not isinstance(self.continente, str):
            return "Error: El continente debe ser de tipo String"
        elif not isinstance(self.ranking_fifa, int):
            return "Error: 
