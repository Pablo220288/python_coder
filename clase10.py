def dividir(a, b):
    if b == 0:
        return None
    else:
        return print(f"{a} dividido {b} es: {a // b}")

# prueba error
#print(dividir(2, 0))

# prueba ok
print(dividir(4, 2))
