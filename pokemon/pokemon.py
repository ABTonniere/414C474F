class Pokemon:

    def __init__(self,name,pv,type,attaque1,typeattaque1,attaque2,typeattaque2,attaque3,typeattaque3):

        self.nom = name
        self.pv = int(pv)
        self.type = type

        self.attaque1 = int(attaque1)
        self.type1 = typeattaque1

        self.attaque2 = int(attaque2)
        self.type2 = typeattaque2

        self.attaque3 = int(attaque3)
        self.type3 = typeattaque3

    def __str__(self):
        return  self.nom



def type(Type1,Type2):
    if(Type1 == Type2):
        return 1
    if(Type1 == "feu" and Type2 == "eau" or Type1 == "eau" and Type2 == "feu"):
        return 2
    if(Type1 == "electrik" and Type2 == "plante" or Type1 == "plante" and Type2 == "electrik"):
        return 2
    if(Type1 == "glace" and Type2 == "insecte" or Type1 == "insecte" and Type2 == "glace"):
        return 2
    if(Type1 == "psy" and Type2 == "roche" or Type1 == "roche" and Type2 == "psy"):
        return 2
    if(Type1 == "tenenbre" and Type2 == "spectre" or Type1 == "spectre" and Type2 == "tenenbre"):
        return 2
    if(Type1 == "normal" or Type2 == "normal"):
        return 0
    return 0
   

def attaque(pokemondef,attaque,typeattaque):
    #plus grande valeur d'attaque
    attaque1 = 0

    if(type(typeattaque,pokemondef.type)==2):
        attaque1 = attaque*2

    elif(type(typeattaque,pokemondef.type)==1):
        attaque1 = attaque/2

    elif(type(typeattaque,pokemondef.type)==0):
        attaque1 = attaque
    else:
        print("type iconue ", typeattaque)
        exit()
    return pokemondef.pv - int(attaque1)

        

def Combat(pokemonA,pokemonB):
    attaqueA = 1
    attaqueB = 1
    while(pokemonA.pv>0 and pokemonB.pv>0):


        if(attaqueA == 1):
            pokemonB.pv = int(attaque(pokemonB,pokemonA.attaque1,pokemonA.type1))
            attaqueA +=1
        if(attaqueA == 2):
            pokemonB.pv = int(attaque(pokemonB,pokemonA.attaque2,pokemonA.type2))
            attaqueA +=1
        if(attaqueA == 3):
            pokemonB.pv = int(attaque(pokemonB,pokemonA.attaque3,pokemonA.type3))
            attaqueA = 1

        if(pokemonB.pv<=0):
            print("A",pokemonA.nom,pokemonA.pv)
            return 'B'
        

        if(attaqueB == 1):
            pokemonA.pv=int(attaque(pokemonA,pokemonB.attaque1,pokemonB.type1))
            attaqueB +=1
        if(attaqueB == 2):
            pokemonA.pv=int(attaque(pokemonA,pokemonB.attaque2,pokemonB.type2))
            attaqueB +=1
        if(attaqueB == 3):
            pokemonA.pv = int(attaque(pokemonA,pokemonB.attaque3,pokemonB.type3))
            attaqueB = 1



        if(pokemonA.pv<=0):
            print("B",pokemonB.nom,pokemonB.pv)
            return 'A'
        
       

NbA = int(input())
lstPokemonA= []
for i in range(NbA):
    pokemon = input()
    pokemon = pokemon.split()
    pokemonA = pokemon[0]
    TypeA = pokemon[1]
    pvA = pokemon[2]
    pvA = int(pvA)
    attaque1 = input()
    attaque1 = attaque1.split()
    typeA1 = attaque1[0]
    attaqueA1Val = attaque1[1]
    int(attaqueA1Val)
    attaque2 = input()
    attaque2 = attaque2.split()
    typeA2 = attaque2[0]
    attaqueA2Val = attaque2[1]
    int(attaqueA2Val)
    attaque3 = input()
    attaque3 = attaque3.split()
    typeA3 = attaque3[0]
    attaqueA3Val = attaque3[1]
    int(attaqueA3Val)
    lstPokemonA.append(Pokemon(pokemonA, pvA, TypeA, attaqueA1Val, typeA1, attaqueA2Val, typeA2, attaqueA3Val, typeA3))


NbB = int(input())
lstPokemonB= []
for i in range(NbB):
    pokemon = input()
    pokemon = pokemon.split()
    pokemonA = pokemon[0]
    TypeA = pokemon[1]
    pvA = pokemon[2]
    pvA = int(pvA)
    attaque1 = input()
    attaque1 = attaque1.split()
    typeA1 = attaque1[0]
    attaqueA1Val = attaque1[1]
    int(attaqueA1Val)
    attaque2 = input()
    attaque2 = attaque2.split()
    typeA2 = attaque2[0]
    attaqueA2Val = attaque2[1]
    int(attaqueA2Val)
    attaque3 = input()
    attaque3 = attaque3.split()
    typeA3 = attaque3[0]
    attaqueA3Val = attaque3[1]
    int(attaqueA3Val)
    lstPokemonB.append(Pokemon(pokemonA, pvA, TypeA, attaqueA1Val, typeA1, attaqueA2Val, typeA2, attaqueA3Val, typeA3))



while(len(lstPokemonA)!=0 and len(lstPokemonB)!=0):
    result = Combat(lstPokemonA[0],lstPokemonB[0])
    if(result == 'B'):
        lstPokemonB.pop(0)
    else:
        lstPokemonA.pop(0)


