## CLASES USERS 

class Users:
     
    # Método constructor:
    
    def __init__(self, nombre,email, edad, altura, alumno, cumple ): # Atributos
        
        self.nombre = nombre
        self.email = email
        self.edad = edad
        self.altura = altura
        self.alumno = alumno
        self.cumple = cumple
        
    
    def __str__(self):
        
        return f""" Users:

    Nombre: {self.nombre}
    Email: {self.email}
    Edad: {self.edad}
    Altura: {self.altura}
    Alumno: {self.alumno}
    Cumple: {self.cumple}
    
    """
    





        