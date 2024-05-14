
data = {}

"""Abrimos el TXT y cargamos los valores existentes en la DB"""
def upload():
  with open('DB.txt',"r") as archivo:
    step = ":"
    for linea in archivo:
        key, value = linea.split(step)
        data[key.strip()] = value.strip()

""" Funcion para Agergar Usuarios a la DB """
def add():
   with open('DB.txt',"w") as adduser:
      for key, value in data.items():
         adduser.write("%s: %s\n" %(key, value) )

""" Funcion de Consulta de Usuarios """
def get_user():
   upload()
   return print(data)

""" Funcion de Registro de Usuarios """     
def register():
  upload()

  user = input("Ingrese un Usuario :")
  if user in data.keys():
    print("El usuario ya exite. Inicie Secion")
    return

  password = input("Ingrese un Password :")
  data[user]=password

  print("Usuario creado Exitosamente")
  add()

  return(get_user())

""" Funcion de Login de Usuarios """
def login():
   upload()

   attempts_limit = 3
   attempts = 0

   for i in range(0, attempts_limit):
      user = input("Ingrese su Usuario :")
      if user in data.keys():
         for i in range(0, attempts_limit):
            password = input("Ingrese su Password :")
            if password == data[user]:
               return print("Login de Usuario Exitoso")
            else:
               attempts += 1
               if(attempts == attempts_limit):   
                  return print("Supero la Cantidad de intentos fallidos")
               else:
                  print(f"Password Incorrecto. Intentelo de Nuevo. Te quedan {attempts_limit - attempts} intentos")
      else:
         attempts += 1
         if(attempts == attempts_limit):
            return print("Supero la Cantidad de intentos fallidos")
         else:
            print(f"Usuario Incorrecto. Intentelo de Nuevo. Te quedan {attempts_limit - attempts} intentos")
         

""" register() """
""" get_user() """
login()