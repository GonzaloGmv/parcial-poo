class libro():
    def __init__(self, autor, titulo, editorial, isbn):
        self.autor = autor
        self.titulo = titulo
        self.editorial = editorial
        self.isbn = isbn
    
    def libro(self):
        print("Libro:", self.titulo, "de", self.autor, "con ISBN", self.isbn, "de la editorial", self.editorial)
 
ejercicio = libro("Cervantes", "El Quijote", "Editorial", "123456789")
ejercicio.libro()