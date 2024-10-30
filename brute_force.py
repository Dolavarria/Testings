# Función que recibe lista de tableros y número de pintores
def minimizar_tiempo_maximo(tableros, pintores):
    
    def particionar(tableros, pintores, particion_actual=None):
        if particion_actual is None:
            particion_actual = []
        # Si solo hay 1 pintor, la partición es la lista de tableros
        if pintores == 1:
            yield particion_actual + [tableros]
        else:
            # Itera desde 1 hasta len(tableros) - pintores + 2
            for i in range(1, len(tableros) - pintores + 2):
                # Llama recursivamente a particionar con los tableros restantes y un pintor menos
                for resultado in particionar(tableros[i:], pintores - 1, particion_actual + [tableros[:i]]):
                    yield resultado

    def calcular_tiempo_maximo(particion):
        # Calcula el tiempo máximo tomado por cualquier pintor en la partición
        return max(sum(parte) for parte in particion)

    tiempo_minimo = float('inf')
    # Itera sobre todas las particiones posibles
    for particion in particionar(tableros, pintores):
        tiempo_maximo = calcular_tiempo_maximo(particion)
        # Actualiza el tiempo mínimo si se encuentra un tiempo máximo menor
        if tiempo_maximo < tiempo_minimo:
            tiempo_minimo = tiempo_maximo

    return tiempo_minimo