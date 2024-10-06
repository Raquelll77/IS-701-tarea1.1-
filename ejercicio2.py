class Libro:
    def __init__(self, titulo:str, autor:str, anio_publicacion:int, numero_paginas:int):
        self.titulo = titulo
        self.autor = autor
        self.anio_publicacion = anio_publicacion
        self.numero_paginas = numero_paginas

    def mostrar_informacion(self):
        print(f"La informacion del libro es la siguiente:\n Titulo: {self.titulo}\n Autor: {self.autor}\n Año de publicación: {self.anio_publicacion}\n Número de páginas: {self.numero_paginas}")

MiLibro = Libro("Cien años de soledad", "Gabriel García Márquez", 1967, 432)

MiLibro.mostrar_informacion()