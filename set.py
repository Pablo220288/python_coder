# Crear Conjunto
conjunto = {"Rojo", "Blanco", "Azul"}
print(conjunto)

#Agregamos Colores
colors = ["Violeta", "Dorado"]
conjunto.update(colors)
print(conjunto)

#Lista de Colores a Eliminar
colors_delete = ["Celeste", "Blanco", "Dorado"]

#Eliminamos Colores del Conjunto
conjunto.discard(colors_delete[0])
conjunto.discard(colors_delete[1])
conjunto.discard(colors_delete[2])

print(conjunto)

#Eliminamos Colores version PRO
conjunto ={"Rojo", "Blanco", "Azul","Violeta", "Dorado"}
len_colors_delete = len(colors_delete)

for i in range(0, len_colors_delete):
    if colors_delete[i] in conjunto:
        conjunto.remove(colors_delete[i])

print(conjunto)