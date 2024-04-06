n = int(input())
if(n<1 or n>100000):
    exit()
mon_tableau = []
for i in range(n):
    while(True):
        try:
            a,b = map(int, input().split())
            if(abs(a)>1000000000 or abs(b)>1000000000):
                continue
        except ValueError:
            continue
        mon_tableau.append(a+b)
        break

for i in range(n): 
    print(mon_tableau[i])

