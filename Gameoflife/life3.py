def est_valide(x, y, N, M):
    return (0 <= x < N) and (0 <= y < M)

def nb_voisin(mat, x, y, N, M):
    voisin = 0
    case_vois = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]
    for dx, dy in case_vois:
        if est_valide(x + dx, y + dy, N, M) and mat[x + dx][y + dy] == 1:
            voisin += 1
    return voisin

def mat_tempo(mat, N, M):
    mat_temp = [[0 for _ in range(M)] for _ in range(N)]
    for i in range(N):
        for j in range(M):
            nb_voisins = nb_voisin(mat, i, j, N, M)
            if mat[i][j] == 1:
                nb_voisins -= 1  # Ne pas compter la cellule elle-même comme un voisin
            mat_temp[i][j] = nb_voisins
    return mat_temp

def edit_mat(mat, mat_temp, N, M):
    for i in range(N):
        for j in range(M):
            if mat[i][j] == 1:
                if mat_temp[i][j] < 2 or mat_temp[i][j] > 3:
                    mat[i][j] = 0
            else:
                if mat_temp[i][j] == 3:
                    mat[i][j] = 1

def affiche(mat, N, M):
    for i in range(N):
        ligne = "|"
        for j in range(M):
            if mat[i][j]:
                ligne += "•"
            else:
                ligne += " "
        ligne += "|"
        print(ligne)

def init_mat_from_input():
    mat = []
    for _ in range(N):
        ligne = input().strip()
        mat.append([int(x) for x in ligne])
    return mat

def alive(mat):
    return sum(sum(row) for row in mat)

N, M = map(int, input().split())
mat = init_mat_from_input()
iterations = int(input())
print("premier etat")
print(alive(mat))
affiche(mat, N, M)

for _ in range(iterations):
    mat_temp = mat_tempo(mat, N, M)
    edit_mat(mat, mat_temp, N, M)

print("\n\ndernier etat")
affiche(mat, N, M)
print(alive(mat))

