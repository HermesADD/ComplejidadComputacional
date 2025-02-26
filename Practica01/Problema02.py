import random

"""
Autor:
Hermes Alberto Delgado Díaz
319258613
"""
def DM3(B, G, H, T, n,intentos):
    """
    Simula el problema  3-Dimensional Matching

    Parámetros:
        - B: Lista de elementos del conjunto B.
        - G: Lista de elementos del conjunto G.
        - H: Lista de elementos del conjunto H.
        - T: Lista de triplas que conforman la relación T. 
        - n: Número de tripletas que debe tener el subconjunto M.
        - Intentos: Número de intentos

    Retona:
        - El subconjunto M válido, o None si no se encontró uno en los intentos.
    """
    
    if len(T) < n:
        print("No es posible seleccionar n triplas de T.")
        return None
    
    for i in range(intentos):
        M = random.sample(T, n)
        print(f"Intento {i+1}: Conjunto candidato (M): {M}")
            
        auxB = set()
        auxG = set()
        auxH = set()
        valido = True
            
        for (b, g, h) in M:
            if b in auxB or g in auxG or h in auxH:
                valido = False
                print("La verificación falla: se repite algún elemento en las tripletas.")
                break
            auxB.add(b)
            auxG.add(g)
            auxH.add(h)
            
        if valido:
            print("La verificación es exitosa. M es un 3DM válido.")
            return M
    
    print("No se encontró un conjunto candidato válido en los intentos realizados.")
    return None

# Ejemplo de uso:
B = ['Fernanda','Julieta','Ana' ]
G = ['Juan', 'Alan','Gustavo']
H = ['Casa1', 'Casa2','Casa3']
T = [
    ('Fernanda', 'Juan', 'Casa1'),
    ('Fernanda', 'Juan', 'Casa2'),
    ('Fernanda', 'Juan', 'Casa3'),
    ('Fernanda', 'Alan', 'Casa1'),
    ('Fernanda', 'Alan', 'Casa2'),
    ('Fernanda', 'Alan', 'Casa3'),
    ('Fernanda', 'Gustavo', 'Casa1'),
    ('Fernanda', 'Gustavo', 'Casa2'),
    ('Fernanda', 'Gustavo', 'Casa3'),
    ('Julieta', 'Juan', 'Casa1'),
    ('Julieta', 'Juan', 'Casa2'),
    ('Julieta', 'Juan', 'Casa3'),
    ('Julieta', 'Alan', 'Casa1'),
    ('Julieta', 'Alan', 'Casa2'),
    ('Julieta', 'Alan', 'Casa3'),
    ('Julieta', 'Gustavo', 'Casa1'),
    ('Julieta', 'Gustavo', 'Casa2'),
    ('Julieta', 'Gustavo', 'Casa3'),
    ('Ana', 'Juan', 'Casa1'),
    ('Ana', 'Juan', 'Casa2'),
    ('Ana', 'Juan', 'Casa3'),
    ('Ana', 'Alan', 'Casa1'),
    ('Ana', 'Alan', 'Casa2'),
    ('Ana', 'Alan', 'Casa3'),
    ('Ana', 'Gustavo', 'Casa1'),
    ('Ana', 'Gustavo', 'Casa2'),
    ('Ana', 'Gustavo', 'Casa3'),
    
]

n = 3  

resultado = DM3(B, G, H, T, n,10)
if(resultado != None):
    print("Resultado: ", resultado)
