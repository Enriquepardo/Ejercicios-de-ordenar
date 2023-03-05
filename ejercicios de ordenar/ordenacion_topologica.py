

def ordenar_topologico(n, restricciones):
    # Calcular el número de predecesores de cada tarea
    en_orden = [0] * n
    for (i, j) in restricciones:
        en_orden[j - 1] += 1
    # Inicializar la lista de tareas sin predecesores
    zero_in_degree = [i + 1 for i in range(n) if en_orden[i] == 0]
    # Calcular la ordenación topológica
    resultado = []
    while zero_in_degree:
        # Seleccionar una tarea sin predecesores
        task = zero_in_degree.pop(0)
        resultado.append(task)
        # Decrementar el número de predecesores de las tareas siguientes
        for (i, j) in restricciones:
            if i == task:
                en_orden[j - 1] -= 1
                # Si una tarea no tiene más predecesores, añadirla a la lista de tareas sin predecesores
                if en_orden[j - 1] == 0:
                    zero_in_degree.append(j)
    # Si quedan tareas con predecesores, hay un ciclo y la ordenación topológica no es posible
    if len(resultado) != n:
        return None
    else:
        return resultado

# Prueba
print(ordenar_topologico(6, [(1, 2), (1, 3), (2, 4), (3, 4), (4, 5), (4, 6), (5, 6)]))
