def aChemin(g,u,v) :
    file = list()
    file.append((u,u))
    visited = set()
    while len(file) != 0 :
        parent,actu = file.pop(0)
        visited.add(actu)
        # Si un voisin du noeud actuel est connecter au noeud d'origine, c'est que ce noeud y est connecter.
        # Si ce neoud est connecter à l'origine par un chemin déjà pris, cela ne compte pas.
        for i in g[actu] :
            if (i == parent) or (i == actu) :
                continue
            if (i == v) :
                return True
            if (i not in visited) :
                file.append((actu,i))
    return False

def estCycle(N,M) :
    # Création du graphe
    g = dict()
    liens = input().split()
    for i in range(0, M*2, 2) :
        # Obtention d'un couple symbolisant un lien
        u = int(liens[i])
        v = int(liens[i+1])
        # Si l'un des noeuds ne faisait pas partit du graphe, il est ajouter
        if u not in g :
            g[u] = set()
        if v not in g :
            g[v] = set()
        # On lie les deux noeuds
        g[u].add(v)
        g[v].add(u)
    # Pour chaques noeuds du graphe, on vérifie si il existe un cycle (chemin passant par 2 autres noeuds et revenant au départ)
    for u in g.keys() :
        if aChemin(g,u,u) :
            return True
    # Si aucun cycle n'à était trouvé, c'est que le graphe n'en à pas.
    return False

R = int(input())
for r in range(R) :
    N,M = map(int, input().split())
    if estCycle(N,M) :
        print(1)
    else :
        print(0)
