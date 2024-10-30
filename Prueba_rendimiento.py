import random
import time
import brute_force
import divide_and_conquer
import dynamic_programming
import pandas as pd

# Generación de 300 Arreglos con Longitudes entre 40 y 100
def generar_conjuntos_prueba(num_conjuntos, min_longitud_arreglo, max_longitud_arreglo, min_valor_elemento, max_valor_elemento):
    conjuntos = []
    for _ in range(num_conjuntos):
        longitud = random.randint(min_longitud_arreglo, max_longitud_arreglo)
        conjunto = [random.randint(min_valor_elemento, max_valor_elemento) for _ in range(longitud)]
        conjuntos.append(conjunto)
    return conjuntos

# Obtener el tiempo de ejecución de cada implementación usando perf_counter
def medir_tiempo(func, L, k):
    inicio = time.perf_counter()
    resultado = func(L, k)
    fin = time.perf_counter()
    tiempo_total = fin - inicio
    return tiempo_total, resultado

# Evaluación del Rendimiento de las Tres Implementaciones
def ejecutar_pruebas():
    conjuntos = generar_conjuntos_prueba(
        num_conjuntos=5,  # Número de conjuntos de prueba
        min_longitud_arreglo=40,  # Longitud mínima de los arreglos
        max_longitud_arreglo=100,  # Longitud máxima de los arreglos
        min_valor_elemento=1,
        max_valor_elemento=100
    )

    k = 5  # Número de pintores

    resultados = {
        "Prueba": [],
        "Fuerza Bruta": [],
        "Divide y Conquistar": [],
        "Programación Dinámica": []
    }

    for i, conjunto in enumerate(conjuntos):
        print(f"Ejecutando prueba {i+1}/{len(conjuntos)}")

        tiempo_fb, resultado_fb = medir_tiempo(brute_force.minimizar_tiempo_maximo, conjunto, k)
        tiempo_dc, resultado_dc = medir_tiempo(divide_and_conquer.minimizar_tiempo_maximo_dc, conjunto, k)
        tiempo_pd, resultado_pd = medir_tiempo(dynamic_programming.minimizar_tiempo_maximo_dp, conjunto, k)

        print(f"Prueba {i+1}:")
        print(f"  Fuerza Bruta: {tiempo_fb:.9f} segundos, Resultado: {resultado_fb}")
        print(f"  Divide y Conquistar: {tiempo_dc:.9f} segundos, Resultado: {resultado_dc}")
        print(f"  Programación Dinámica: {tiempo_pd:.9f} segundos, Resultado: {resultado_pd}")

        resultados["Prueba"].append(f"Prueba {i+1}")
        resultados["Fuerza Bruta"].append(tiempo_fb)
        resultados["Divide y Conquistar"].append(tiempo_dc)
        resultados["Programación Dinámica"].append(tiempo_pd)

        # Verificar que todos los enfoques den el mismo resultado
        assert resultado_fb == resultado_dc == resultado_pd, f"Los resultados no coinciden en la prueba {i+1}"

    return resultados

def exportar_a_excel(resultados):
    df = pd.DataFrame(resultados)
    promedio = df.mean(numeric_only=True).to_frame().T
    promedio['Prueba'] = 'Promedio:'
    cols = df.columns.tolist()
    promedio = promedio[cols]
    df = pd.concat([df, promedio], ignore_index=True)
    df.to_excel("resultados_pruebas.xlsx", index=False)

if __name__ == "__main__":
    resultados = ejecutar_pruebas()
    exportar_a_excel(resultados)

    for enfoque, tiempos in resultados.items():
        if enfoque != "Prueba":
            tiempo_promedio = sum(tiempos) / len(tiempos)
            print(f"{enfoque}: Tiempo promedio = {tiempo_promedio:.9f} segundos")