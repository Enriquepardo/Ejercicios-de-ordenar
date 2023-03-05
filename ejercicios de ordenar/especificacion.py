

def explorar_segmentos(t, inicio, fin):
    k = 0
    i = inicio
    
    while i <= fin:
        # Buscar el segmento actual y su máximo
        j = i
        maximo = t[i]
        while j <= fin and t[j] >= maximo:
            maximo = t[j]
            j += 1
        k += 1
        
        # Hacer copia de seguridad del maximo del segmento
        mi = maximo
        
        # Desplazar los elementos de t[di+1 .. fi] una celda hacia la izquierda
        for m in range(j-1, i, -1):
            if m >= 1:
                t[m] = t[m-1]
        
        # Colocar el elemento más grande del segmento «en lo alto»
        t[i] = mi
        
        # Actualizar el índice i para buscar el siguiente segmento
        i = j
    
    return t


# Prueba

t = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(explorar_segmentos(t, 0, 9))
