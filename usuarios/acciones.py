#import imp
import usuarios.usuario as modelo
import notas.acciones
class Acciones:

    def registro(self):

        print("\n Ok!!! hagamos el registro en el sistema...")
        nombre = input("¿Cual es tu nombre?: ")
        apellidos = input("¿Cuales son tus apellidos?: ")
        email = input("Introduce tu email: ")
        password = input("Introduce tu contraseña: ")

        usuario = modelo.Usuario(nombre, apellidos, email, password)
        registro = usuario.registrar()

        if registro[0] >= 1:
            print(f"\n Perfecto {registro[1].nombre} te has registrado con el {registro[1].email}")
        else:
            print("\n No te has registrado correctamente")

    def login(self):

        print("Vale!! ingresa tus datos...")

        try:
            email = input("Introduce tu email: ")
            password = input("Introduce tu contraseña: ")

            usuario = modelo.Usuario('', '', email, password)
            login = usuario.identificar()
            if email == login[3]:
                print(f"\n bienvenido {login[1]}, te has registrado correctamente")
                self.proximasAcciones(login)

        except Exception as e:
            #print(type(e))
            #print(type(e).__name__)
            print(f"login incorrecto este")
    
    def proximasAcciones(self, usuario):
        print("""
        Acciones disponibles
        - Crear nota(crear)
        - Mostrar tus notas(mostrar)
        - Eliminar nota(eliminar)
        - Salir (salir)
        """)

        accion = input("¿Que quieres hacer?... ")
        hazEl = notas.acciones.Acciones()

        if accion == "crear":
            #print("vamos a crear")
            hazEl.crear(usuario)
            self.proximasAcciones(usuario)
        elif accion == "mostrar":
            #print("vamos a mostrar")
            hazEl.mostrar(usuario)
            self.proximasAcciones(usuario)
        elif accion == "eliminar":
            #print("vamos a eliminar")
            hazEl.borrar(usuario)
            self.proximasAcciones(usuario)
        elif accion == "salir":
            print("ok")
            print(f"{usuario[1]}, hasta pronto ")
            exit
        return None