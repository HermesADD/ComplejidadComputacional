"""
Autor:
Hermes Alberto Delgado Díaz
319258613
"""

import copy
import random
import math

#####################################
# ALGORITMO GENÉTICO
#####################################

def fitness(tablero):
    """
    Calcula el número de colisiones entre reinas en el tablero del momento. 
    Una colisión ocurre si dos reinas están en la misma diagonal. 

    Args:
        tablero (list[int]): Lista que representa la posición de las reinas en columnas.
    Returns:
        int: Número de colisiones diagonales. 
    """
    colisiones = 0
    n = len(tablero)
    for i in range(n):
        for j in range(i+1, n):
            if abs(tablero[i] - tablero[j]) == abs(i - j):
                colisiones += 1
    return colisiones

def generar_poblacion(n, tam, base=None):
    """
    Genera una población inicial de tableros aleatorios.
    Si se proporciona una base, la población se genera a partir de la base dada.

    Args:
        n (int): Tamaño del tablero.
        tam (int): Tamaño de la población.
        base (list[int], optional): Tablero inicial base. 

    Returns:
        list[list[int]]: Lista de tableros(población).
    """
    if base:
        poblacion = [base[:]]
        while len(poblacion) < tam:
            ind = base[:]
            random.shuffle(ind)
            poblacion.append(ind)
        return poblacion
    return [random.sample(range(n), n) for _ in range(tam)]

def seleccion_ruleta(poblacion):
    """
    Selecciona dos individuos de la población usando el método de ruleta basado en la 
    función de aptitud inversa (menos colisiones es mejor).
    
    Args:
        poblacion (list[list[int]]): Población actual.

    Returns:
        list[list[int]]: Dos individuos seleccionados. 
    """
    puntuaciones = [1 / (1 + fitness(ind)) for ind in poblacion]
    total = sum(puntuaciones)
    probs = [p / total for p in puntuaciones]
    return random.choices(poblacion, weights=probs, k=2)

def cruce(ind1, ind2):
    """
    Realiza un cruce de orden entre dos individuos para generar descendientes.

    Args:
        ind1 (list[int]): Primer individuo.
        ind2 (list[int]): Segundo individuo.

    Returns:
        tuple[list[int], list[int]]: Dos descendientes generados.
    """
    n = len(ind1)
    punto = random.randint(1, n-2)
    hijo1 = ind1[:punto] + [g for g in ind2 if g not in ind1[:punto]]
    hijo2 = ind2[:punto] + [g for g in ind1 if g not in ind2[:punto]]
    return hijo1, hijo2

def mutacion(ind, tasa=0.1):
    """
    Aplica una mutación por intercambio entre dos posiciones del individuo con cierta probabilidad.

    Args:
        ind (list[int]): Individuo a mutar.
        tasa (float): Probabilidad de mutación.

    Returns:
        list[int]: Individuo mutado.
    """
    n = len(ind)
    if random.random() < tasa:
        i, j = random.sample(range(n), 2)
        ind[i], ind[j] = ind[j], ind[i]
    return ind

def algoritmo_genetico(n=8, generaciones=200, tam_poblacion=50, inicial=None):
    """
    Ejecuta el algoritmo genético para resolver el problema de las N-Reinas.

    Args:
        n (int): Tamaño del tablero.
        generaciones (int): Número máximo de generaciones.
        tam_poblacion (int): Tamaño de la población.
        inicial (list[int], optional): Configuración inicial base.

    Returns:
        tuple: Mejor solución, número de colisiones, iteración donde se encontró la solución óptima, total de generaciones.
    """
    poblacion = generar_poblacion(n, tam_poblacion, base=inicial)
    mejor = min(poblacion, key=fitness)
    iter_encontrada = -1

    for gen in range(generaciones):
        nueva_poblacion = []
        while len(nueva_poblacion) < tam_poblacion:
            p1, p2 = seleccion_ruleta(poblacion)
            h1, h2 = cruce(p1, p2)
            nueva_poblacion.extend([mutacion(h1), mutacion(h2)])
        poblacion = nueva_poblacion
        candidato = min(poblacion, key=fitness)
        if fitness(candidato) < fitness(mejor):
            mejor = candidato
        if fitness(mejor) == 0:
            iter_encontrada = gen + 1
            break
    return mejor, fitness(mejor), iter_encontrada, generaciones

#####################################
# BÚSQUEDA TABÚ 
#####################################

def evaluar(tablero):
    """
    Alias de la función de evaluación (fitness).

    Args:
        tablero (list[int]): Representación de un tablero.

    Returns:
        int: Número de colisiones diagonales.
    """
    
    return fitness(tablero)

def generar_vecindario(sol):
    """
    Genera el vecindario del tablero dado mediante intercambios de pares de reinas.

    Args:
        sol (list[int]): Tablero actual.

    Returns:
        list[tuple[list[int], tuple[int, int]]]: Lista de vecinos con sus movimientos.
    """
    
    vecinos = []
    n = len(sol)
    for i in range(n):
        for j in range(i + 1, n):
            v = sol[:]
            v[i], v[j] = v[j], v[i]
            vecinos.append((v, (i, j)))
    return vecinos

def busqueda_tabu(n=8, max_iter=100, tabu_tenure=5, inicial=None):
    """
    Ejecuta la búsqueda tabú para encontrar una solución al problema de las N-Reinas.

    Args:
        n (int): Tamaño del tablero.
        max_iter (int): Número máximo de iteraciones.
        tabu_tenure (int): Tamaño de la lista tabú.
        inicial (list[int], optional): Solución inicial.

    Returns:
        tuple: Mejor solución encontrada, número de colisiones, iteración donde se encontró la solución óptima, iteración máxima.
    """
    
    sol_actual = inicial[:] if inicial else random.sample(range(n), n)
    mejor_sol = sol_actual[:]
    lista_tabu = []
    iter_encontrada = -1

    for iteracion in range(max_iter):
        vecinos = generar_vecindario(sol_actual)
        vecinos = sorted(vecinos, key=lambda x: evaluar(x[0]))
        for vecino, movimiento in vecinos:
            if movimiento not in lista_tabu or evaluar(vecino) < evaluar(mejor_sol):
                sol_actual = vecino
                if evaluar(sol_actual) < evaluar(mejor_sol):
                    mejor_sol = sol_actual[:]
                lista_tabu.append(movimiento)
                if len(lista_tabu) > tabu_tenure:
                    lista_tabu.pop(0)
                break
        if evaluar(mejor_sol) == 0:
            iter_encontrada = iteracion + 1
            break

    return mejor_sol, evaluar(mejor_sol), iter_encontrada, max_iter

#####################################
# IMPRESIÓN DE TABLERO 
#####################################

def imprimir_tablero(solucion):
    """
    Imprime el tablero con 'Q' indicando la posición de cada reina.

    Args:
        solucion (list[int]): Representación de un tablero.
    """
    
    n = len(solucion)
    for fila in range(n):
        linea = ""
        for col in range(n):
            if solucion[col] == fila:
                linea += "Q "
            else:
                linea += ". "
        print(linea)

#####################################
# PRUEBAS DE LOS DOS ALGORITMOS CON DISTINTAS N's
#####################################
def ejecutar_prueba(n):
    print(f"\n=== Prueba con n = {n} ===")
    tablero_inicial = random.sample(range(n), n)
    print("\n--- Tablero Inicial Aleatorio ---")
    print("Configuración:", tablero_inicial)
    imprimir_tablero(tablero_inicial)

    print("\n--- Algoritmo Genético ---")
    sol_ag, costo_ag, iter_ag, max_iter_ag = algoritmo_genetico(n, inicial=tablero_inicial)
    print("Solución:", sol_ag)
    print("Colisiones:", costo_ag)
    print("Iteración encontrada:", iter_ag if iter_ag != -1 else "No se alcanzó solución óptima")
    print("Iteración máxima permitida:", max_iter_ag)
    imprimir_tablero(sol_ag)

    print("\n--- Búsqueda Tabú ---")
    sol_bt, costo_bt, iter_bt, max_iter_bt = busqueda_tabu(n, inicial=tablero_inicial)
    print("Solución:", sol_bt)
    print("Colisiones:", costo_bt)
    print("Iteración encontrada:", iter_bt if iter_bt != -1 else "No se alcanzó solución óptima")
    print("Iteración máxima permitida:", max_iter_bt)
    imprimir_tablero(sol_bt)

if __name__ == "__main__":
    for n in [8, 10, 15]:
        ejecutar_prueba(n)

