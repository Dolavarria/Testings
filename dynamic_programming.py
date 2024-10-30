import sys

def minimizar_tiempo_maximo_dp(tableros, pintores):
    n = len(tableros)
    
    # Matriz de DP: dp[i][j] es el tiempo mínimo para que j pintores pinten los primeros i tableros
    dp = [[0] * (pintores + 1) for _ in range(n + 1)]
    
    # Suma acumulada de longitudes de tableros para cálculos rápidos
    suma_tableros = [0] * (n + 1)
    for i in range(1, n + 1):
        suma_tableros[i] = suma_tableros[i - 1] + tableros[i - 1]
    
    # Inicializar el caso base: con un solo pintor, el tiempo es la suma de los tableros hasta i
    for i in range(1, n + 1):
        dp[i][1] = suma_tableros[i]
    
    # Llenar la matriz DP para casos con más pintores
    for j in range(2, pintores + 1):  # Número de pintores
        for i in range(1, n + 1):  # Número de tableros
            dp[i][j] = sys.maxsize  # Inicializar con un valor muy grande
            # Probar diferentes particiones para asignar tableros al pintor j
            for p in range(1, i + 1):  # p es el número de tableros asignados al pintor j
                tiempo_actual = suma_tableros[i] - suma_tableros[p - 1]  # Suma de tableros de p a i
                dp[i][j] = min(dp[i][j], max(dp[p - 1][j - 1], tiempo_actual))
    
    return dp[n][pintores]