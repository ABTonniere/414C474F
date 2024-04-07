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
            elif attaques[attaque][1] > 100:
                attaques[attaque] = (attaques[attaque][0], 100)

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
        if poke1.attaques[poke1_n_attaque][0] in types_contretypes:
            if poke1.attaques[poke1_n_attaque][0] == types_contretypes[poke2.typeP]:
                degats = degats * 2
            elif poke2.attaques[poke1_n_attaque][0] == poke2.typeP:
                degats = degats // 2

        poke2.pv -= degats
        poke1_n_attaque += 1
        if poke2.pv <= 0:
            poke2_n_attaque = 0
            deck1.pokemons.insert(0, poke1)
            continue

        degats = poke2.attaques[poke2_n_attaque][1]
        if poke2.attaques[poke2_n_attaque][0] in types_contretypes:
            if poke2.attaques[poke2_n_attaque][0] == types_contretypes[poke1.typeP]:
                degats = degats * 2
            elif poke1.attaques[poke2_n_attaque][0] == poke1.typeP:
                degats = degats // 2

        poke1.pv -= degats
        poke2_n_attaque += 1
        if poke1.pv <= 0:
            poke1_n_attaque = 0
            deck2.pokemons.insert(0, poke2)
            continue

        deck1.pokemons.insert(0, poke1)
        deck2.pokemons.insert(0, poke2)

    if len(deck1.pokemons) > 0:
        return "A " + deck1.pokemons[0].nom + " " + str(deck1.pokemons[0].pv)
    else:
        return "B " + deck2.pokemons[0].nom + " " + str(deck2.pokemons[0].pv)


deck1 = Deck()
deck2 = Deck()

nb_poke_1 = int(input())
if nb_poke_1 > 60:
    nb_poke_1 = 60
elif nb_poke_1 <= 0:
    nb_poke_1 = 1

for i in range(nb_poke_1):

    nom, typeP, pv = input().split(" ")
    pv = int(pv)
    attaques = list()
    for j in range(3):
        typeA, degats = input().split(" ")
        attaques.append((typeA, int(degats)))

    deck1.ajouter_pokemon(Pokemon(nom, typeP, pv, attaques))

nb_poke_2 = int(input())
if nb_poke_2 > 60:
    nb_poke_2 = 60
elif nb_poke_2 <= 0:
    nb_poke_2 = 1

for i in range(nb_poke_2):

    nom, typeP, pv = input().split(" ")
    pv = int(pv)
    attaques = list()
    for j in range(3):
        typeA, degats = input().split(" ")
        attaques.append((typeA, int(degats)))

    deck2.ajouter_pokemon(Pokemon(nom, typeP, pv, attaques))

print(combat(deck1, deck2))
