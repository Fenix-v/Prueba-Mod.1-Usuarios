
import user as Users

# Lista Usuarios y atributos
alumnos = [
    Users("Luis Fernández", "luis@gmail.com", 54, 1.75, True, 12/6/1970),
    Users("Agata Abramzcyk", "Agata@gmail.com", 40, 1.80, False, 13/6/1986),
    Users("Leila fernández", "leila@gmail.com", 4, 1.40, True, 2/11/2020),
    Users("Cecilia Orosco", "cecilia@gmail.com", 54, 1.65, True, 27/11/1970),
    Users("Santiago Escobar", "santiago@gmail.com", 38, 1.85, False, 13/1/1984)
    
]

# Función no existen alumnos
print(" Has elegido la opción 1: ")
def print_usuarios():
   
    if not alumnos:
         print("No hay alumnos introducidos en la base de datos:")
         return
    for usuario in alumnos: 
        print(usuario)
        
 # Ordenar usuarios
print("Has elegido la opción 2: ")

def ordenar_usuarios():
      user_sort_by_nombre = sorted(alumnos, key=lambda u : u.nombre, reverse=True) # desc
                
#   user_sort_by_email = sorted(usuarios, key=lambda u : u.nombre) # asc
      for i in user_sort_by_nombre:
                print(i)
     

#Introducir un nombre
print("Has elegido la opción 3: ")

def print_nombre():
    print("Has elegido la opción 3: ") 
    name = input("Introduce nuevo alumno en la BD: ")
    
    for usuario in alumnos:
        if name.lower() == usuario.nombre.lower():
            print(usuario)
            return  
 
# Función creación de usuarios

def crea_usuarios():
    
    print(" Has elegido la opción 4: ")
    nombre = input("Introduce un nombre nuevo:")
    email = input("Introduce un nuevo email:")
    edad = int(input("Introduce una nueva edad:"))
    altura = float(input("Introduce una nueva altura:"))
    alumno = bool(input("Introduce 1 SI es alumno o 0 si NO:"))
    naci =input("Introduce una nueva fecha de nacimiento")
    
    #creamos un nuevo usuarrio
    new_usuario = Users(nombre, email, edad, altura, alumno, naci)
    
    #guardar el nuevo uisuario en una lista
    alumnos.append(new_usuario)
           
    
    print("Alumno creado correctamente")
     
      
# actualizar nombres de alumnos


def update_usuarios():
    print("Has elegido la opción 4: ")
    title = input(" Introduce el nombre del usuario a actualizar")
    nuevo_usuario = input(" Introduce el nuevo usuario:")
    nuevo_email = (input(" Introduce el nuevo email:"))
    nueva_edad = int(input(" Introduce una nueva edad:"))
    nueva_altura = float(input(" Introduce una nueva altura:"))
    nuevo_alumno = bool(input(" Introduce True o False :"))
    nuevo_naci = int(input(" Introduce una nueva fecha de nacimiento"))
            
              
            #actualizado = False
    for i in alumnos:
                if title.lower() == i.nombre.lower():
                    i.nombre = nuevo_usuario
                    i.email = nuevo_email
                    i.edad = nueva_edad
                    i.altura = nueva_altura
                    i.alumno = nuevo_alumno
                    i.naci = nuevo_naci
                    actualizado = True
                    break
                
    if actualizado:
        
        print("¡¡¡USUARIO ACTUALIZADO CORRECTAMENTE¡¡¡")
        
    else:
        print("No ha sido posible actualizar el nuevo Usuario")
        
                
    # Eliminar un alumno
    def borrar_usuario():
     print("Has elegido la opción 5: ")
    nombre_usuario = input(" Introduce  usuario a eliminar: ")
                  
    for i in alumnos:
     if nombre_usuario.lower() == i.nombre.lower():
        alumnos.remove(i)
        print(" ¡¡¡¡USUARIO ELIMINADO CORRECTAMENTE¡¡¡¡")
        break
            
    # Eliminar lista completa de alumnos
    def eliminar_lista():
      print("Has elegido la opción 6: ")
        
    print(" Eliminando lista de usuarios: ")  
    alumnos.clear()  
    print("Lista aliminada correctamente")
    
            
     

     

     

            
         
     
    