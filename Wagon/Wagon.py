'''
R = int(input())  
liste = list()
for k in range(R):
    liste.append(0)
    

for i in range(R):
    temps = input()
    temps =temps.split()
    noeuds = temps[1]
    liaison = temps[0]
    vagon=input()
    vagon = vagon.split()
    occ=[0]*int(liaison)
    print(occ)
    for elm in vagon:
        occ[int(elm)]+=1
    for j in occ:
        if(occ[j]>=((int(liaison)/2)+1)):
            liste[i]=1

for y in range(len(liste)):
    print(liste[y])
'''

R = int(input())  
liste = []

for k in range(R):
    liste.append(0)

for i in range(R):
    temps = input().split()
    liaison = int(temps[0])
    noeuds = int(temps[1])
    vagon = input().split()
    occ = [0] * (liaison + 1)  # On ajoute 1 pour gérer les indices de 1 à liaison
    for elm in vagon:
        occ[int(elm)] += 1
    print(occ)
    for j in range(1, len(occ)):  # On commence de 1 car les indices des noeuds commencent à 1
        if occ[j] >= (liaison / 2) + 1:
            liste[i] = 1
            break  # On peut arrêter la boucle dès qu'on a trouvé un élément majoritaire

for y in liste:
    print(y)

