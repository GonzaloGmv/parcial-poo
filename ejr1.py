class libro():
    def __init__(self, autor, titulo, editorial):
        self.autor = autor
        self.titulo = titulo
        self.editorial = editorial
    def libro(self):
        print("Libro:", self.titulo, "de", self.autor, "de la editorial", self.editorial)

ejercicio = libro("Cervantes", "El Quijote", "Anaya")
ejercicio.libro()