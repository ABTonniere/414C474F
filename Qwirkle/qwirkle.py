def verif(tuiles, cell) :
    if cell == "--" :
        tuiles.clear()
    else :
        if (len(tuiles) == 0) :
            tuiles.append(cell)
        elif (len(tuiles) == 1) :
            if (tuiles[0][0] != cell[0]) and (tuiles[0][1] != cell[1]) :
                return False
            elif (tuiles[0][0] == cell[0]) and (tuiles[0][1] == cell[1]) :
                return False
            tuiles.append(cell)
        else :
            if (tuiles[0][0] == tuiles[1][0]) :
                if (tuiles[0][0] != cell[0]) or (tuiles[0][1] == cell[1]) :
                    return False
            elif (tuiles[0][1] == tuiles[1][1]) :
                if (tuiles[0][0] == cell[0]) or (tuiles[0][1] != cell[1]) :
                    return False
            else :
                return False
            tuiles.append(cell)
            if len(tuiles) > 6 :
                return False
    return True

def verifGrille() :
    tuiles = list()
    colonnes = list()
    inventaire = dict()
    nbL, nbC = map(int, input().split())
    for i in range(nbL) :
        ligne = input().split()
        if len(ligne) != nbC :
            return False
        for j in range(len(ligne)) :
            if not verif(tuiles, ligne[j]) :
                return False
            if i == 0 :
                colonnes.append(list())
            colonnes[j].append(ligne[j])
            if ligne[j] != "--" :
                if ligne[j] in inventaire :
                    if inventaire[ligne[j]] >= 3 :
                        return False
                else :
                    inventaire[ligne[j]] = 0
                inventaire[ligne[j]] += 1
        tuiles.clear()
    tuiles = list()
    for col in colonnes :
        for c in col :
            if not verif(tuiles, c) :
                return False
        tuiles.clear()
    return True

if (verifGrille()) :
    print("VALIDE")
else :
    print("INVALIDE")
