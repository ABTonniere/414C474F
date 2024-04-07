def recupInt(expr,deb=0) :
    ent = ""
    fin = deb
    while (fin < len(expr)) and expr[fin].isdigit() :
        ent+= expr[fin]
        fin+= 1
    if ent == "" :
        ent = 0
    return (deb,int(ent),fin)

def evaluate(expr) :
    e = list()
    positiv = True
    deb = 0
    while True :
        deb,nb,fin = recupInt(expr,deb)
        if (fin >= len(expr)) or (expr[fin] == ')') :
            return (e,fin+1)
        elif expr[fin] == ' ' :
            if expr[fin+1] == '-' :
                positiv = False
            fin+= 3
        if deb == fin :
            if positiv :
                e.append(1)
            else :
                e.append(-1)
        else :
            if positiv :
                e.append(nb)
            else :
                e.append(-nb)
        positiv = True
        deb = fin

expr = input()
pos = expr.find('^')
rep = None
while pos > 0 :
    car = expr[pos - 1]
    deb = pos - 1
    # Obtenir la sous-chaîne à répéter
    if car == ')' :
        deb = pos - 2
        nbPar = 1
        while (nbPar != 0) and (deb >= 0) :
            if expr[deb] == '(' :
                nbPar-= 1
                if nbPar == 0 :
                    break
            elif expr[deb] == ')' :
                nbPar+= 1
            deb-= 1
        if deb < 0 :
            print("Pas de paranthèse ouvrante")
            print(expr)
            exit(-1)
        rep = expr[deb:pos]
    else :
        rep = "" + car
    # Obtenir le nombre de répétition
    _,nbRep,fin = recupInt(expr,(pos+1))
    # Répéter la sous chaine
    deb = expr[:deb] + (rep * nbRep)
    pos = len(deb)
    expr = deb + expr[fin:]
    # Rechercher le prochain opérateur de répétition
    if pos == len(expr) :
        pos = -1
    else :
        pos = expr[pos:].find('^') + pos

pos = expr.find('(')
while pos > 0 :
    e = expr[pos:]
    pos2 = expr.find(')')
    _,tab,_ = evaluate(e[:pos2])
    pos = expr.find('(')

