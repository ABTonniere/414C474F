dic_ingredients = {
    "emmental": 80,
    "oeuf": 50,
    "jambon": 46,
    "tomate": 14,
    "champignon": 21,
    "lard": 108,
    "chèvre": 99,
    "oignon": 18,
    "creme": 60,
    "andouille": 70,
    "cidre": 92,
    "patate": 45,
    "salade": 5,
    "bleu": 106,
    "saucisse": 120,
    "saumon": 87,
    "camembert": 95,
    "pomme": 12,
    "miel": 33,
    "saint-jacques": 45
}


def calc_calories_type_crepe(nbCrepes, ingredients):
    calories = 0
    for ingredient in ingredients:
        if ingredient in dic_ingredients:
            calories += dic_ingredients[ingredient]
    return calories * nbCrepes + 150 * nbCrepes


def get_crepes_commande():
    order = input()
    order_parts = order.split(' ')
    index = 1
    calories = 0

    nbType = int(order_parts[0])

    for i in range(nbType):
        nbCrepes = int(order_parts[index])
        index += 1
        ingredients = order_parts[index].split(',')
        index += 1
        calories += calc_calories_type_crepe(nbCrepes, ingredients)

    return calories


print(get_crepes_commande())
