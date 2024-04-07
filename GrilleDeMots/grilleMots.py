def chercher_mot(grille, mot):
    for i in range(len(grille)):
        for j in range(len(grille[i])):
            if dfs(grille, i, j, mot):
                return True
    return False


def dfs(grille, i, j, mot):
    if len(mot) == 0:
        return True
    if i < 0 or i >= len(grille) or j < 0 or j >= len(grille[0]) or grille[i][j] != mot[0]:
        return False
    tmp = grille[i][j]
    grille[i][j] = "#"
    res = dfs(grille, i + 1, j, mot[1:]) or dfs(grille, i - 1, j, mot[1:]) or dfs(grille, i, j + 1, mot[1:]) or dfs(
        grille, i, j - 1, mot[1:]) or dfs(grille, i + 1, j + 1, mot[1:]) or dfs(grille, i - 1, j - 1, mot[1:]) or dfs(
        grille, i - 1, j + 1, mot[1:]) or dfs(grille, i + 1, j - 1, mot[1:])
    grille[i][j] = tmp
    return res


grille = []

liste_mots_chercher = list()

dims = str(input()).split(' ')
dimX, dimY = int(dims[0]), int(dims[1])

for i in range(dimY):
    grille.append(list(input()))

grille = [[ch for ch in ligne if ch != " "] for ligne in grille]

nb_mots = int(input())
nb_mots_trouve = 0

for i in range(nb_mots):
    liste_mots_chercher.append(input())

for mot in liste_mots_chercher:
    if chercher_mot(grille, mot):
        nb_mots_trouve += 1

print(nb_mots_trouve)
