types_contretypes = {
    "feu": "eau",
    "plante": "electrik",
    "glace": "insecte",
    "psy": "roche",
    "tenebres": "spectre",
    "sol": "acier"
}


class Pokemon:
    def __init__(self, nom, typeP, pv, attaques):
        self.nom = nom
        self.typeP = typeP

        if pv > 600:
            self.pv = 600
        elif pv < 1:
            self.pv = 1
        else:
            self.pv = pv

        for attaque in range(len(attaques)):
            if attaques[attaque][1] < 0:
                attaques[attaque] = (attaques[attaque][0], 0)
            elif attaques[attaque][1] > 600:
                attaques[attaque] = (attaques[attaque][0], 600)

        self.attaques = attaques

    def __str__(self):
        return self.nom + "\n" + self.typeP + "\n" + str(self.pv) + "\n" + str(self.attaques)


class Deck:
    def __init__(self):
        self.pokemons = list()

    def ajouter_pokemon(self, pokemon):
        if len(self.pokemons) >= 60:
            return

        self.pokemons.append(pokemon)

    def __str__(self):
        result = "Pokemons:\n"
        for pokemon in self.pokemons:
            result += str(pokemon) + "\n"
        return result


def combat(deck1, deck2):
    poke1_n_attaque = 0
    poke2_n_attaque = 0

    while len(deck1.pokemons) > 0 and len(deck2.pokemons) > 0:

        if poke1_n_attaque >= 3:
            poke1_n_attaque = 0
        if poke2_n_attaque >= 3:
            poke2_n_attaque = 0

        poke1 = deck1.pokemons.pop(0)
        poke2 = deck2.pokemons.pop(0)

        degats = poke1.attaques[poke1_n_attaque][1]
        if poke2.typeP in types_contretypes:
            if poke1.attaques[poke1_n_attaque][0] == types_contretypes[poke2.typeP]:
                degats = degats * 2
                print("critique")
            elif poke2.attaques[poke1_n_attaque][0] == poke2.typeP:
                degats = degats // 2
                print("pas très efficace")

        print("########################################################")
        print(poke1.nom + " attaque " + poke2.nom + " avec " + poke1.attaques[poke1_n_attaque][0] + " et inflige " + str(degats) + " degats")
        poke2.pv -= degats
        print("pv de " + poke2.nom + " : " + str(poke2.pv))
        print("attaque n°" + str(poke1_n_attaque) + " pour " + poke1.nom)
        print("Set d'attaque de " + poke1.nom + " : " + str(poke1.attaques))

        poke1_n_attaque += 1
        if poke2.pv <= 0:
            poke2_n_attaque = 0
            deck1.pokemons.insert(0, poke1)
            print(poke2.nom + " est mort")
            continue

        degats = poke2.attaques[poke2_n_attaque][1]
        if poke1.typeP in types_contretypes:
            if poke2.attaques[poke2_n_attaque][0] == types_contretypes[poke1.typeP]:
                print("critique")
                degats = degats * 2
            elif poke1.attaques[poke2_n_attaque][0] == poke1.typeP:
                print("pas très efficace")
                degats = degats // 2

        print(poke2.nom + " attaque " + poke1.nom + " avec " + poke2.attaques[poke2_n_attaque][0] + " et inflige " + str(degats) + " degats")
        poke1.pv -= degats
        print("pv de " + poke1.nom + " : " + str(poke1.pv))
        print("attaque n°" + str(poke2_n_attaque) + " pour " + poke2.nom)
        print("Set d'attaque de " + poke2.nom + " : " + str(poke2.attaques))

        poke2_n_attaque += 1
        if poke1.pv <= 0:
            poke1_n_attaque = 0
            deck2.pokemons.insert(0, poke2)
            print(poke1.nom + " est mort")
            continue

        deck1.pokemons.insert(0, poke1)
        deck2.pokemons.insert(0, poke2)

    if len(deck1.pokemons) > 0:
        return "A " + deck1.pokemons[0].nom + " " + str(deck1.pokemons[0].pv)
    else:
        return "B " + deck2.pokemons[0].nom + " " + str(deck2.pokemons[0].pv)


def initDeck():
    d = Deck()
    nb_poke = int(input())
    if nb_poke > 60:
        nb_poke = 60
    elif nb_poke <= 0:
        nb_poke = 1
    for i in range(nb_poke):
        donnes_poke = input().split(" ")
        if len(donnes_poke) > 3:
            while (donnes_poke is None) or (donnes_poke[-1] == ""):
                donnes_poke.pop()
        if len(donnes_poke) > 3:
            pv = donnes_poke[len(donnes_poke) - 1]
            typeP = donnes_poke[len(donnes_poke) - 2]
            nom = " ".join(donnes_poke[:len(donnes_poke) - 2])
        else:
            nom, typeP, pv = donnes_poke
        pv = int(pv)
        if pv < 1 :
            pv = 1
        elif pv > 600 :
            pv = 600
        attaques = list()
        for j in range(3):
            typeA, degats = input().split(" ")
            degats = int(degats)
            if degats < 0 :
                degats = 0
            elif degats > 600 :
                degats = 600
            attaques.append((typeA, int(degats)))
        d.ajouter_pokemon(Pokemon(nom, typeP, pv, attaques))
    return d


print(combat(initDeck(), initDeck()))
