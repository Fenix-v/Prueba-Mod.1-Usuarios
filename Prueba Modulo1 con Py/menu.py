
import usuario as crud


while True:
    option = int(input(menu))
    match option:
        case 1:
            crud.print_usuarios(alumnos)
        case 2:
            crud.ordenar_usuarios(alumnos)
        case 3:
            crud.introduce_nombre(alumnos)
        case 4:
            crud.crea_usuarios(alumnos)
        case 5:
            crud.update_usuarios(alumnos)
        case 6:
            crud.borrar_usuario(alumnos)
        case 7:
            crud.eliminar_lista(alumnos)
        case 8:
            print("¡¡¡¡ HASTA PRONTO ¡¡¡¡")
            break
        case _:
            print("Opción incorrecta")


import usuario as crud

# Menu de entrada para el usuario

menu = """Te damos la bienvenida a la app de Alumnos, estas son las opciones:
          1 - Ver todos los Usuarios
          2 - Ver todos los Usuarios ordenados 
          3 - Ver un Usuario por su nombre
          4 - Crear nuevo Usuario
          5 - Actualizar Usuario existente
          6 - Borrar un Usuario 
          7 - Borrar todos los Usuarios
          8 - Salir
          """

while True:
    option = int(input(menu))
    match option:
        case 1:
            crud.print_usuarios()
        case 2:
            crud.ordenar_usuarios()
        case 3:
            crud.introduce_nombre()
        case 4:
            crud.crea_usuarios()
        case 5:
            crud.update_usuarios()
        case 6:
            crud.borrar_usuario()
        case 7:
            crud.eliminar_lista()
        case 8:
            print("¡¡¡¡ HASTA PRONTO ¡¡¡¡")
            break
        case _:
            print("Opción incorrecta")
