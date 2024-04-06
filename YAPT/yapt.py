def est_palindrome(chaine):
    return chaine == chaine[::-1]


def trouver_palindromes(chaine):
    palindromes = []
    i = 0
    taille = len(chaine)
    last = -1
    for i in range(taille) :
        pal = -1
        i2 = i
        if (i2 < last) :
            i2 = last
        for j in range((i2 + 1), taille) :
            if est_palindrome(chaine[i:j]) :
                pal = j
        if (pal > (i + 2)) :
            last = pal
            palindromes.append((i, chaine[i:pal]))
    return palindromes


def trouver_plus_long_palindromes_touchants(chaine):
    palindromes = trouver_palindromes(chaine)
    if (palindromes is None) or (len(palindromes) == 0) :
        return "NADA"
    palindromes_plus_long = list()
    for i in range(len(palindromes) - 2) :
        deb = palindromes[i][0]
        pal1 = palindromes[i][1]
        tMax = len(pal1)
        j = i + 1
        while (j < len(palindromes)) and ((deb + tMax) >= palindromes[j][0]) :
            if (deb + tMax) == palindromes[j][0] :
                pal2 = palindromes[j][1]
                pal =  pal1 + ' ' + pal2
                tMin = len(pal2)
                if tMax < tMin :
                    tMin = tMax
                    tMax = len(pal2)
                palindromes_plus_long.append((pal,tMax,tMin,deb))
            j += 1
    if (palindromes_plus_long is None) or (len(palindromes_plus_long) == 0) :
        return "NADA"
    palindromes_plus_long = sorted(palindromes_plus_long, key=lambda x: (-len(x[0]), -x[1], -x[2], x[3]))
    return palindromes_plus_long[0][0]


N = int(input())
for _ in range(N):
    s = input()
    print(trouver_plus_long_palindromes_touchants(s))
