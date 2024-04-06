def calc_score_cell_direction(tuiles, dep, direction) :
    i,j = dep
    i += direction[0]
    j += direction[1]
    nbTuile = 0
    while (i,j) in tuiles :
        nbTuile += 1
        i -= 1
    return nbTuile

def calc_score_cell(tuiles, ajout, ignore=None) :
    l = ajout[0]
    c = ajout[1]
    score = 1
    nbTuile = calc_score_cell_direction(tuiles, (l,c), (-1,0))
    if nbTuile == 6 :
        score+= 6
    if ((l - 1), c) != ignore :
        score+= nbTuile
    nbTuile+= calc_score_cell_direction(tuiles, (l,c), (1,0))
    if nbTuile == 6 :
        score+= 6
    if ((l + 1), c) != ignore :
        score+= nbTuile
    nbTuile+= calc_score_cell_direction(tuiles, (l,c), (0,-1))
    if nbTuile == 6 :
        score+= 6
    if (l, (c - 1)) != ignore :
        score+= nbTuile
    nbTuile+= calc_score_cell_direction(tuiles, (l,c), (0,+1))
    if nbTuile == 6 :
        score+= 6
    if (l, (c + 1)) != ignore :
        score+= nbTuile
    return score

def joue(tuiles, nbL, nbC) :
    ajout = list()
    for i in range(nbL) :
        ligne = input().split()
        if len(ligne) < nbC :
            return 0
        for j in range(nbC) :
            if (i,j) not in tuiles :
                if ligne[j] != "--" :
                    ajout.append((i,j,ligne[j]))
    if len(ajout) == 0 :
        return 0
    score = calc_score_cell(tuiles,ajout[0]);
    if len(ajout) == 1 :
        return score
    for i in range(1, len(ajout)) :
        score+= calc_score_cell(tuiles,ajout[i],(ajout[i-1][0],ajout[i-1][1]));
    for i,j,v in ajout :
        tuiles[(i,j)] = v
    return score

tuiles = dict()
nbJoueur = int(input())
points = [0 for _ in range(nbJoueur)]
nbTours = int(input())
nbL, nbC = map(int, input().split())
for tour in range(nbTours) :
    for joueur in range(nbJoueur) :
        points[joueur] += joue(tuiles, nbL, nbC)
        print(points)
for point in points :
    print(point)
