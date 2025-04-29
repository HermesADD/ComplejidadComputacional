def merge_list(L1, L2):
    merged = sorted(set(L1 + L2))
    return merged

def trim(L, delta):
    trimmed = [L[0]]
    last = L[0]
    
    for y in L[1:]:
        if y > last * (1 + delta):
            trimmed.append(y)
            last = y
    
    return trimmed

def approx_subset_sum(S, t , epsilon):
    n = len(S)
    L = [0]
    for i in range(n):
        L = merge_list(L,[x + S[i] for x in L])
        L = trim(L, epsilon / (2*n))
        L = [x for x in L if x <= t]
        
    return max(L)

if __name__ == "__main__":
    S = [104, 102, 201, 101]
    t = 300
    epsilon = 0
    resultado = approx_subset_sum(S,t,epsilon)
    print("Resultado aproximado: ", resultado)