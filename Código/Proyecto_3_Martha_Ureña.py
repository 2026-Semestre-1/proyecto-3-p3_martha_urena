#Proyecto 3
"""
Nombre: Pais
Atributos: codigo_fifa, nombre, continente, ranking_fifa
Métodos: constructor, mostrar_datos, actualizar_datos
"""
class Pais:
    """
    Definición: Constructor
    """
    def __init__(self, codigo_fifa, nombre, continente, ranking_fifa):
        self.codigo_fifa = codigo_fifa
        self.nombre = nombre
        self.continente = continente
        self.ranking_fifa = ranking_fifa
    """
    Nombre: mostrar_datos
    Entradas: self.nombre, self.codigo, self.continente, self.ranking_fila
    Salidas: retornará los datos ingresados, de como un comprobante
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
        else:
            print("País: ", self.nombre)
            print("Código FIFA: ", self.codigo_fifa)
            print("Continente: ", self.continente)
            print("Ranking FIFA: " , self.ranking_fifa)
    """
    Nombre: actualizar_datos
    Entradas: nombre, self.codigo, self.continente, self.ranking_fila
    Salidas: se actualizarán los datos
    Restricciones:
        Los valores (self.nommbre, self.cofigo_fifa, self.contitente) deben ser de tipo String
        El valor self.ranking_fifa debe ser de tipo entero
    """
    def actualizar_datos(self, nombre, codigo_fifa, continente, ranking_fifa):
        if not isinstance(nombre, str):
            return "Error: El nombre del país debe ser de tipo String"
        if nombre == "":
            return "Error: El nombre del país no debe estar en blanco"
        if not isinstance(codigo_fifa, str):
            return "Error: El código fifa debe ser de tipo String"
        if codigo_fifa == "":
            return "Error: El código fifa no debe estar en blanco"
        if not isinstance(continente, str):
            return "Error: El continente debe ser de tipo String"
        if continente == "":
            return "Error: El continente no debe estar en blanco"
        if not isinstance(ranking_fifa, int):
            return "Error: El ranking fifa debe ser de tipo entero y numérico"
        if ranking_fifa <= 0:
            return "Error: El ranking fifa debe ser un número positivo"
        
        if nombre != "":
            self.nombre = nombre
            
        if codigo_fifa != "":
            if codigo_fifa[0:1] == "" or codigo_fifa[1:2] == "" or codigo_fifa[2:3] == "" or codigo_fifa[3:4] != "":
                return "Error: El código fifa debe tener 3 letras"
            else:
                self.codigo_fifa = codigo_fifa
                
        if continente != "":
            self.continente = continente
            
        if ranking_fifa != 0:
            self.ranking_fifa = ranking_fifa
        
        return "Los datos han sido actualizados correctamente"




                
            
                






















        
        
        
