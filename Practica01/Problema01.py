import random 

"""
Autor:
Hermes Alberto Delgado Díaz
319258613
"""
def mayoriaSecuencua(V,C, intentos):
    """
        Función que busca un elemento mayoritario en una secuencia V.
        
        La mayoría de una secuencia:
            Dada una secuencia V, de n números tomador del conjunto C, con n>k, encontrar al elemento
            que sea mayoría en V, si es que tal existe.
            
        Parámetros:
            - V: lista de números que representan la secuencia.
            - C: lista de posibles valores en la secuencia V.
            - intentos: Número máximo de intentos para encontrar el elemento mayoritario.
            
        Retorno:
            - El número con la condición de mayoría si se encuentra en los intentos permitidos.
            - None si no se encontró un elemento mayoritario.
    """
    for i in range(intentos):
        candidato = random.choice(C)
        print(f"Intento {i+1}: Elemento candidato: {candidato}")
        contador = V.count(candidato)
        
        if contador > len(V)/2:
            print(f"El elemento {candidato} es mayoritario (aparece {contador} veces en {len(V)} elementos).")
            return candidato
        else:
            print(f"El elemento {candidato} no es mayoritario (aparece {contador} veces en {len(V)} elementos).")
            
    print("No se encontró un candidato mayoritario válido en los intentos realizados.")
    return None

# Ejemplo de ejecución
V = [1,2,6,6,3,4,5,6,7,8,6,6,6,6,4,6,6,6,6,6,6,6,6,6,6,6,6,6,6,9,11,16,8,16,16,6,6,16,1,16,6,16,6,16,16,14]
C = [1,2,3,4,5,6,7,8,9,11,12,13,14,15,16]

resultado = mayoriaSecuencua(V,C,5)
if(resultado != None):
    print("Resultado: ", resultado)