notas = [0.0,0.0,0.0]
notas_len = len(notas)
peso = [20, 30, 50]

for i in range(0, notas_len):
    notas[i] = float(input("Ingrese la Nota" + str(i+1) + ": "))

prom = 0

for i in range(0, notas_len):
    prom += notas[i] * peso[i]

prom_peso = prom/100
aprobado = 6

if prom_peso > aprobado:
    print("Felicitaciones, tu promedio es:  ",prom_peso)
else:
    print("Lo lamento, tu promedio es:  ",prom_peso)

