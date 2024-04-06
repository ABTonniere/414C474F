def est_palindrome(chaine):
    return chaine == chaine[::-1]


def trouver_palindromes(chaine):
    palindromes = []
    i = 0
    taille = len(chaine)
    while i < (taille - 1) :
        j = i + 2
        while j < taille :
            if est_palindrome(chaine[i:j]) :
                i2 = i
                j2 = j
                while (0 < i2) and (j2 < taille) and est_palindrome(chaine[i2:j2]) :
                    i2 -= 1
                    j2 += 1
                if i2 < i :
                    i2 += 1
                    j2 -= 1
                palindromes.append((i2, chaine[i2:j2]))
                i = j2
                break
            j+= 1
        i+= 1
    return palindromes


def trouver_plus_long_palindromes_touchants(chaine):
    palindromes = trouver_palindromes(chaine)
    if (palindromes is None) or (len(palindromes) == 0) :
        return "NADA"
    palindromes_plus_long = list()
    for i in range(len(palindromes)) :
        for j in range((i + 1), len(palindromes)) :
            pal1 = palindromes[i][1]
            pal2 = palindromes[j][1]
            pal =  pal1 + ' ' + pal2
            tMax = len(pal1)
            tMin = len(pal2)
            if tMax < tMin :
                tMin = tMax
                tMax = len(pal2)
            palindromes_plus_long.append((pal,tMax,tMin,palindromes[i][0]))
    if (palindromes_plus_long is None) or (len(palindromes_plus_long) == 0) :
        return "NADA"
    palindromes_plus_long = sorted(palindromes_plus_long, key=lambda x: (-len(x[0]), -x[1], -x[2], x[3]))
    return palindromes_plus_long[0][0]


N = int(input())
for _ in range(N):
    s = input()
    print(trouver_plus_long_palindromes_touchants(s))
