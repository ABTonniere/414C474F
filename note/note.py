P = int(input())
groupe = []
tempNMG = input()
tempNMG = tempNMG.split()
N = int(tempNMG[0])
M = int(tempNMG[1])
G = int(tempNMG[2])
eleve = input()
eleve = eleve.split()

for i in range(M):
    tempR = input()
    print(tempR)
    tempR = tempR.split()
    eleveModif = int(tempR[1])
    eleveVal = int(tempR[2])
    eleve[eleveModif] = int(eleveVal)

for j in range(G):
    tempG = input()
    tempG = tempG.split()
    groupeDeb = int(tempG[1])
    groupeFin = int(tempG[2])
    moy = 0
    for k in range (groupeDeb,groupeFin):
        moy+= int(eleve[k])
    moy = moy/((groupeFin-groupeDeb)+1)
    groupe[j]=moy

max = moy[0]
plusfort =0
for l in moy:
    if(moy[l]>min):
        max = moy[l]
        plusfort=0

print(plusfort)
