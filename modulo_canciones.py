canciones_list = []  # BD


# -------- validaciones ---------------------
# para el titulo y artista
def validar_texto_vacio(texto):
    if len(texto.strip()) > 0:
        return True
    else:
        print("Error NO puede ser vacio")
        return False  # --> NO valido!!


def validar_duracion(duracion):
    if duracion > 0:
        return True
    else:
        print("ERROR debe ser mayor a cero!")
        return False


def imprimir_cancion(cancion):
    es_favorita = "Si" if cancion["favorita"] == True else "No"
    print(f"""
    --------------------------  
    Titulo: {cancion["titulo"]}
    Artista: {cancion["artista"]}
    Duración: {cancion["duracion"]}
    Favorita: {es_favorita}      """)


# -------- transacciones ----------------------
def agregar_cancion():
    titulo = str(input("Ingrese titulo:")).strip()
    while not validar_texto_vacio(titulo):
        titulo = str(input("Ingrese titulo:")).strip()

    artista = str(input("Ingrese artista:")).strip()
    while not validar_texto_vacio(artista):
        artista = str(input("Ingrese artista:")).strip()

    while True:
        try:
            duracion = int(input("Ingrese duraciónm:"))
            while not validar_duracion(duracion):
                duracion = int(input("Ingrese duraciónm:"))
            break
        except:
            print("Error debe ser un N°")

    # ------ armamos json cancion -------------------
    cancion = {
        "titulo": titulo,
        "artista": artista,
        "duracion": duracion,
        "favorita": False,
    }
    # ----- almacemos en la lista ------------------
    canciones_list.append(cancion)
    print(" <<< registro almacenado >>>")


def mostrar_canciones():
    # este es un listar!
    pass


def buscar_cancion():
    # se ingresa el título de la canción y
    # se busca en la BD
    pass
