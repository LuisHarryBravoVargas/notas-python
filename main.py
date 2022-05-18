"""
proyecto python y mysql

- abrir asistente
-login o registro
- si elegimos registro creara un usuario en la bbdd
- si elegimos login, identifica al usuario y nos preguntara
- creara nota, mostrar notas, borrarlas
"""


from usuarios import acciones

print("""
    Acciones disponibles:
        -registro
        -login
""")
hazEl = acciones.Acciones()
accion = input("¿Que quieres hacer?")
if accion == "registro":
    hazEl.registro()

elif accion == "login":
    hazEl.login()

