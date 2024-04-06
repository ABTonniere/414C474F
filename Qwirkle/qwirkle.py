def verifGrille(grille, xMax, yMax):
    for x in range(xMax):
        for y in range(yMax):
            if not verifCellule(grille, x, y, xMax, yMax):
                return False

    return True


def verifCellule(grille, x, y, xMax, yMax):
    symboles = ['R', 'X', 'L', 'C', 'S', 'T']
    couleurs = ['1', '2', '3', '4', '5', '6']

    if grille[x][y] == "--":
        return True

    if len(grille[x][y]) != 2:
        return False

    if grille[x][y][0] not in symboles or grille[x][y][1] not in couleurs:
        return False

    symbole, couleur = grille[x][y]

    symboles_voisins = []
    couleurs_voisines = []
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x + dx, y + dy
        if nx >= 0 and nx < len(grille) and ny >= 0 and ny < len(grille[0]):
            cellule_voisine = grille[nx][ny]
            if cellule_voisine != "--":
                symbole_voisin, couleur_voisin = cellule_voisine[0], cellule_voisine[1]
                symboles_voisins.append(symbole_voisin)
                couleurs_voisines.append(couleur_voisin)

    # vérification si ligne valide
    if symbole in symboles_voisins and couleur in couleurs_voisines:
        return False

    return True
