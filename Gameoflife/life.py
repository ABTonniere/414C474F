def est_valide(x, y,N,M):
    return (0 <= x and x < N) and (0 <= y and y < M)

def nb_voisin(mat, x, y,N,M):
    voisin = 0
    case_vois = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]
    for dx, dy in case_vois:
        if est_valide(x + dx, y + dy,N,M):
            if mat[x + dx][y + dy] == 1:
                voisin += 1
    return voisin

def mat_tempo(mat,N,M):
    mat_temp = [[0 for _ in range(M)] for _ in range(N)]
    for i in range(N):
        for j in range(M):
            mat_temp[i][j] = nb_voisin(mat, i, j,N,M)
    return mat_temp

def edit_mat(mat, mat_temp,N,M):
    for i in range(N):
        for j in range(M):
            if mat_temp[i][j] == 3 or mat_temp[i][j] == 2:
                mat[i][j] = 1
            else:
                mat[i][j] = 0


def affiche(mat,N,M):
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
    mat_t = []
    for _ in range(N):
        ligne=input()
        mat_t.append([int(x) for x in ligne])
    return mat_t

def alive(mat,N,M):
    tot=0
    for i in range(N):
        for j in range(M):
            if mat[i][j] == 1:
                tot += 1
    return tot


N, M = map(int, input().split())
mat = init_mat_from_input()

iterations = int(input())
print("premier etat")
print(alive(mat,N,M))
affiche(mat,N,M)
for _ in range(iterations):
    edit_mat(mat, mat_tempo(mat,N,M),N,M)

print("\n\ndernier etat")
affiche(mat,N,M)
print(mat_tempo(mat,N,M))
print(alive(mat,N,M))

