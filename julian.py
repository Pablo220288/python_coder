vendedores = {
    1: ("Julian"),
    2: ("Santiago"),
    3 : ("Andres")
}

mes = {
    1 : ("Enero"),
    2 : ("Febrero"),
    3 : ("Marzo"),
    4 : ("Abril"),
    5 : ("Mayo"),
    6 : ("Junio"),
    7 : ("Julio"),
    8 : ("Agosto"),
    9 : ("Septiembre"),
    10 : ("Octubre"),
    11 : ("Noviembre"),
    12 : ("Diciembre")
}

vendedor = int(input( "Ingrese Numero de vendedor: "))

if not vendedor in vendedores:
    print("No existe el vendedor") 
    vendedor = int(input( "Ingrese Numero de vendedor: "))
else:
    vendedor = vendedores[vendedor]


mes_de_balance = int(input( "Ingrese digito de mes [1..12]: "))

if not mes_de_balance in mes:
    print("Ingrese un Digito de Mes Valido") 
    mes_de_balance = int(input("Ingrese digito de mes [1..12]: "))
else:
    mes_de_balance = mes[mes_de_balance]


balance_mensual = input("Ingrese balance mensual: ")


print(vendedor, ", Segun tu Balance para el mes de ", mes_de_balance,", tus ventas anuales ascienden a: $", int(balance_mensual)*12)
