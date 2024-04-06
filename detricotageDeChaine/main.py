N = int(input())
if N < 0 :
    N = 1
elif N > 1000 :
    N = 1000

for i in range(N) :
    entrer = input().split()
    if len(entrer) != 2 :
        continue
    boite,melange = entrer
    B = len(boite)
    if (B < 1) or (B > 50) :
        continue
    X = len(melange)
    if (X < 1) or (X > 10000) :
        continue
    while True :
        newMelange = melange.replace(boite, "")
        if newMelange == melange :
            break
        melange = newMelange
    if len(melange) == 0 :
        print("OK")
    else :
        print("OUPS")
