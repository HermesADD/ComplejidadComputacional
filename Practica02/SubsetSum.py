def merge_list(L1, L2):
    """
    Fusiona dos listas L1 y L2, elimina duplicados y devuelve una lista ordenada.

    Args:
        L1 (list): Primera lista de enteros.
        L2 (list): Segunda lista de enteros.

    Returns:
        list: Lista ordenada y sin duplicados que contiene los elementos de L1 y L2. 
    """
    
    merged = sorted(set(L1 + L2))
    return merged

def trim(L, delta):
    """
    Recorta una lista ordenada eliminando elementos que no aportan significativamente nuevos valores.

    Args:
        L (list): Lista ordenada de enteros.
        delta (float): Factor tolerancia para el recorte.

    Returns:
        list: Lista recortada donde no hay dos elementos demasiado cercanos entre si.
    """
    if not L:
        return []
    
    result = [L[0]]
    last = L[0]
    
    for i in range(1, len(L)):
        if L[i] > last * (1 + delta):  
            result.append(L[i])
            last = L[i]
    
    return result

def approx_subset_sum(S, t , epsilon):
    """
    Aproxima la suma más grande de un subconjunto de S que no exceda t, permitiendo un error de epsilon.
    Args:
        S (list): Lista de enteros positivos.
        t (int): Valor objetivo.
        epsilon (float): Factor de aproximación permitido.
    Returns:
        int: Valor de la suma aproximada más grande sin exceder t.
    """
    
    n = len(S)
    L = [0]
    for i in range(n):
        L = merge_list(L,[x + S[i] for x in L])
        L = trim(L, epsilon / (2*n))
        L = [x for x in L if x <= t]
        
    return max(L)

if __name__ == "__main__":
    S = [104, 102, 201, 101]
    t = 308
    epsilon = 0.40
    resultado = approx_subset_sum(S,t,epsilon)
    print("Resultado aproximado: ", resultado)