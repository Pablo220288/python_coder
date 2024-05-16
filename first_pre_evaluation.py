data = {}

# Abrimos el .txt y cargamos los valores existentes en "data" local
# Si el archivo no existe, lo creamos.
def read_file():
    try:
        file = open("DB.txt", "r")
        step = ":"
        for linea in file:
            key, value = linea.split(step)
            data[key.strip()] = value.strip()
        file.close()

    except FileNotFoundError:
        file = open("DB.txt", "w")
        for key, value in data.items():
            file.write("%s: %s\n" % (key, value))
        file.close()


# Agergamos los usuarios de la "data" local al .txt
def add_user():
    with open("DB.txt", "a") as adduser:
        for key, value in data.items():
            adduser.write("%s: %s\n" % (key, value))


# Consultamos los usuarios existente en el .txt
def get_user():
    read_file()
    if len(data) == 0:
        return print("No existen Usuarios registrados")
    else:
        list_user = []
        for key in data.keys():
            list_user.append(key.title())
        return print(f"Lista de Usuarios registrados: \n{list_user}")


# Funcion de Registro de Usuarios
def register():
    read_file()

    user = input("Ingrese un Usuario: ")

    if user.isnumeric():
        print("El Usuario no puede ser un Numero, reintente..")
        return

    if user in data.keys():
        print("El usuario ya exite. Inicie Secion")
        return

    password = input("Ingrese un Password: ")
    data[user] = password

    print("Usuario creado Exitosamente")
    add_user()

    return get_user()


# Funcion de Login de Usuarios
def login():
    read_file()

    attempts_limit = 3
    attempts = 0

    for i in range(0, attempts_limit):
        user = input("Ingrese su Usuario: ")
        if user in data.keys():
            for i in range(0, attempts_limit):
                password = input("Ingrese su Password: ")
                if password == data[user]:
                    return print("Login de Usuario Exitoso")
                else:
                    attempts += 1
                    if attempts == attempts_limit:
                        return print("Supero la Cantidad de intentos fallidos")
                    else:
                        print(
                            f"Password Incorrecto. Intentelo de Nuevo. Te quedan {attempts_limit - attempts} intentos"
                        )
        else:
            attempts += 1
            if attempts == attempts_limit:
                return print("Supero la Cantidad de intentos fallidos")
            else:
                print(
                    f"Usuario Incorrecto. Intentelo de Nuevo. Te quedan {attempts_limit - attempts} intentos"
                )


register()
# get_user()
# login()
