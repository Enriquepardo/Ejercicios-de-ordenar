
import random
t = []
for i in range (0,50):
    t.append(random.randint(0,100))

def ordenar_por_insercion(t):
    # Recorrer la tabla desde el segundo elemento hasta el final
    for i in range(1, len(t)):
        # Almacenar el elemento actual en una variable temporal
        temp = t[i]
        # Realizar una búsqueda dicotómica para encontrar la posición donde insertar el elemento
        j = i - 1
        while j >= 0 and t[j] > temp:
            t[j + 1] = t[j]
            j -= 1
        # Insertar el elemento en la posición encontrada
        t[j + 1] = temp
    return t

print(ordenar_por_insercion(t))
