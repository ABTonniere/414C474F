def est_palindrome(chaine):
    return chaine == chaine[::-1]


def trouver_palindromes(chaine):
    palindromes = []
    for i in range(len(chaine)):
        for j in range(i + 2, len(chaine) + 1):
            if est_palindrome(chaine[i:j]):
                palindromes.append((i, j, chaine[i:j]))
    return sorted(palindromes, key=lambda x: (-len(x[2]), x[0]))


def trouver_plus_long_palindromes_touchants(chaine):
    palindromes = trouver_palindromes(chaine)
    paires_valides = []
    i = 0
    while i < len(palindromes) - 1:
        if palindromes[i][1] > palindromes[i + 1][0] or palindromes[i][1] == palindromes[i + 1][0]:
            combined = palindromes[i][2] + palindromes[i + 1][2]
            if not est_palindrome(combined):
                return palindromes[i][2], palindromes[i + 1][2]
            else:
                i += 2
        else:
            i += 1

    if not paires_valides:
        return "NADA"

    paires_valides.sort(key=lambda x: (-len(x[0]) - len(x[1]), -len(x[0]), x[0]))
    return paires_valides[0]


N = int(input())
for _ in range(N):
    s = input()
    result = trouver_plus_long_palindromes_touchants(s)
    if result == "NADA":
        print(result)
    else:
        print(result[0], result[1])
