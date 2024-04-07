for x in range(1,10) :
    for y in range(1,10) :
        for w in range(1,10) :
            for z in range(1,10) :
                puissance = (x**y)*(w**z)
                entier = ((x*(10**3))+(y*(10**2))+(w*10)+z)
                if puissance == entier :
                    print("OK")

