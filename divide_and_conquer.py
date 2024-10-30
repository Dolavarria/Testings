def minimizar_tiempo_maximo_dc(tableros, pintores):
    # Función para verificar si es posible pintar con tiempo máximo tiempo_max
    def es_posible(tiempo_max):
        pintores_usados = 1
        tiempo_actual = 0

        for tablero in tableros:
            tiempo_actual += tablero

            if tiempo_actual > tiempo_max:
                # Se necesita un nuevo pintor
                pintores_usados += 1
                tiempo_actual = tablero

                # Si se usan más pintores que disponibles, no es posible
                if pintores_usados > pintores:
                    return False
        return True

    # Búsqueda binaria de la solución óptima
    inicio, fin = max(tableros), sum(tableros)
    tiempo_minimo = fin

    while inicio <= fin:
        mid = (inicio + fin) // 2
        if es_posible(mid):
            tiempo_minimo = mid
            fin = mid - 1
        else:
            inicio = mid + 1

    return tiempo_minimo