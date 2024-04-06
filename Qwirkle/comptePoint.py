def calc_score_cell_direction(tuiles, dep, direction) :
    i,j = dep
    i += direction[0]
    j += direction[1]
    nbTuile = 0
    while (i,j) in tuiles :
        nbTuile += 1
        i += direction[0]
        j += direction[1]
    print(nbTuile,end=' ')
    return nbTuile

def calc_score_cell(tuiles, ajout, ignore=None) :
    l = ajout[0]
    c = ajout[1]
    score = 0
    inL = False
    inC = False

    nbTuile = calc_score_cell_direction(tuiles, (l,c), (-1,0))
    if nbTuile == 6 :
        score+= 6
    if (ignore is None) or ((ignore[0] < l) and (ignore[1] == c)) :
        score+= nbTuile
    elif not (ignore  is  None) :
        inL = True
    if nbTuile != 0 :
        inL = True

    nbTuile = calc_score_cell_direction(tuiles, (l,c), (1,0))
    if nbTuile == 6 :
        score+= 6
    if (ignore is None) or ((ignore[0] > l) and (ignore[1] == c)) :
        score+= nbTuile
    elif not (ignore  is  None) :
        inL = True
    if nbTuile != 0 :
        inL = True

    nbTuile = calc_score_cell_direction(tuiles, (l,c), (0,-1))
    if nbTuile == 6 :
        score+= 6
    if (ignore is None) or ((ignore[0] == l) and (ignore[1] < c)) :
        score+= nbTuile
    elif not (ignore  is  None) :
        inC = True
    if nbTuile != 0 :
        inC = True

    nbTuile = calc_score_cell_direction(tuiles, (l,c), (0,+1))
    if nbTuile == 6 :
        score+= 6
    if (ignore is None) or ((ignore[0] == l) and (ignore[1] > c)) :
        score+= nbTuile
    elif not (ignore  is  None) :
        inC = True
    if nbTuile != 0 :
        inC = True

    print(score)
    return ((score + 1), inL,inC)

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
    oldS,INL,INC = calc_score_cell(tuiles,ajout[0]);
    score = oldS
    if len(ajout) == 1 :
        if INL and INC :
            score+= 1
    else :
        for i in range(1, len(ajout)) :
            s,inL,inC = calc_score_cell(tuiles,ajout[i],(ajout[i-1][0],ajout[i-1][1]));
            print(inC,INL,oldS,inL,INC,s)
            if inC and INL and (oldS != 1) :
                oldS = s
                s+= 1
            elif inL and INC and (oldS != 1) :
                oldS = s
                s+= 1
            else :
                oldS = s
            print(score)
            score+= s
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
