def position_initiale_blanc(N):
    
    M = (N - 1) % 12 + 1
    return M

# Exemple d'utilisation
N = int(input())
M = position_initiale_blanc(N)
print(M)