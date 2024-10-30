import random
import time
import brute_force
import divide_and_conquer
import dynamic_programming

#Generación de 300 Arreglos con Longitudes entre 40 y 100

def generar_conjuntos_prueba(num_conjuntos, min_longitud_arreglo, max_longitud_arreglo, min_valor_elemento, max_valor_elemento):
    conjuntos = []
    for _ in range(num_conjuntos):
        longitud = random.randint(min_longitud_arreglo, max_longitud_arreglo)
        conjunto = [random.randint(min_valor_elemento, max_valor_elemento) for _ in range(longitud)]
        conjuntos.append(conjunto)
    return conjuntos

#obtener el tiempo de ejecución de cada implementación.
def medir_tiempo(func, L, k):
    inicio = time.time()
    resultado = func(L, k)
    fin = time.time()
    return fin - inicio, resultado


#Evaluación del Rendimiento de las Tres Implementaciones

def ejecutar_pruebas():
    conjuntos = generar_conjuntos_prueba(
        num_conjuntos=300,
        min_longitud_arreglo=40,
        max_longitud_arreglo=100,
        min_valor_elemento=1,
        max_valor_elemento=100
    )
    k = 5  # Número de pintores

    resultados = {
        "Fuerza Bruta": [],
        "Divide y Conquistar": [],
        "Programación Dinámica": []
    }

    for i, conjunto in enumerate(conjuntos):
        print(f"Ejecutando prueba {i+1}/300")

        tiempo_fb, resultado_fb = medir_tiempo(brute_force.minimizar_tiempo_maximo, conjunto, k)
        tiempo_dc, resultado_dc = medir_tiempo(divide_and_conquer.minimizar_tiempo_maximo_dc, conjunto, k)
        tiempo_pd, resultado_pd = medir_tiempo(dynamic_programming.minimizar_tiempo_maximo_dp, conjunto, k)

        resultados["Fuerza Bruta"].append(tiempo_fb)
        resultados["Divide y Conquistar"].append(tiempo_dc)
        resultados["Programación Dinámica"].append(tiempo_pd)

        # Verificar que todos los enfoques den el mismo resultado
        assert resultado_fb == resultado_dc == resultado_pd, f"Los resultados no coinciden en la prueba {i+1}"

    return resultados

if __name__ == "__main__":
    resultados = ejecutar_pruebas()

    for enfoque, tiempos in resultados.items():
        tiempo_promedio = sum(tiempos) / len(tiempos)
        print(f"{enfoque}: Tiempo promedio = {tiempo_promedio:.6f} segundos")
        
        
        
#Enfoques Implementados:

#Fuerza Bruta: brute_force.py explora todas las particiones posibles.
#Divide y Conquistar: divide_and_conquer.py utiliza búsqueda binaria para optimizar la asignación.
#Programación Dinámica: dynamic_programming.py construye una tabla de soluciones parciales.