from sqlite3 import Cursor
import notas.nota as modelo

class Acciones:

    def crear(self, usuario):
        print(f"ok {usuario[1]}, vamos a crear una nueva nota ")
        
        titulo = input("introduce el titulo de tu nota: ")
        descripcion = input("introduce la descripcion de tu nota: ")
        
        nota = modelo.Nota(usuario[0], titulo, descripcion)
        guardar = nota.guardar()

        if guardar[0] >= 1:
            print(f"se ha guardado la nota: {nota.titulo} ")

        else:
            print(f"lo siento {usuario[0]} no se ha guardado la nota... ")

    def mostrar(self, usuario):

        print(f"\n{usuario[1]} estas son tus notas: ")

        nota = modelo.Nota(usuario[0])
        notas = nota.listar()

        #print(notas)
        for nota in notas:
            print("\n")
            print("(++++++++++++++++++++++++++++++++++++)")
            print(nota[2])
            print(nota[3])
            print("(------------------------------------)")
            print("\n")

    def borrar(self, usuario):
        print(f"\nperfecto {usuario[1]} vamos a borrar notas ")

        titulo = input("introduce el tiulo de la nota a borrar: ")

        nota = modelo.Nota(usuario[0], titulo)
        eliminar = nota.eliminar()

        if eliminar[0] >= 1:
            print(f"Hemos borrado la nota: {nota.titulo} ")
        else:
            print("no se pudo borrar la nota, intenta luego... ")