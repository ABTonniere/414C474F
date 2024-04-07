def aChemin(g,cible) :
    file = list()
    file.append((cible,cible))
    visited = set()
    while len(file) != 0 :
        parent,n = file.pop(0);
        visited.add(n)
        for u in g[n] :
            if u not in visited :
                file.append((n,u))
            if (u == cible) and (u != parent) :
                return True
    return False

def estCycle(N,M) :
    # Création du graphe
    g = dict()
    liens = input().split()
    for i in range(0, M*2, 2) :
        # Obtention d'un couple symbolisant un lien
        u = int(liens[i])
        v = int(liens[i+1])
        if u == v :
            return True
        # Vérifier les paramètres
        if (u < 0) or (v < 0) :
            return True
        elif (u >= N) or (u >= N) :
            return True
        # Si l'un des noeuds ne faisait pas partit du graphe, il est ajouter
        if u not in g :
            g[u] = set()
        if v not in g :
            g[v] = set()
        # Vérifier si le lien n'existe pas déjà
        if (v in g[u]) or (u in g[v]) :
            return True
        # On lie les deux noeuds
        g[u].add(v)
        g[v].add(u)
    # Pour chaques noeuds du graphe, on vérifie si il existe un cycle (chemin passant par 2 autres noeuds et revenant au départ)
    for u in g.keys() :
        if aChemin(g,u) :
            return True
    # Si aucun cycle n'à était trouvé, c'est que le graphe n'en à pas.
    return False

R = int(input())
if R < 1 :
    R = 1
elif R > 1000 :
    R = 1000
for r in range(R) :
    N,M = map(int, input().split())
    if N < 1 :
        N = 1
    elif N > 1000 :
        N = 1000
    if M < 1 :
        M = 1
    elif M > 1000 :
        M = 1000
    if estCycle(N,M) :
        print(1)
    else :
        print(0)
