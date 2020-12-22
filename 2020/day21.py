class Food:
    allergens = []
    ingredients = []

    def __init__(self, line):
        self.allergens = set(line[line.index(' (contains') + 11:].strip(')').split(', '))
        self.ingredients = set(line[:line.index(' (contains')].split(' '))


def part_one(foods):
    allergen_ingredients = [list(value)[0] for key, value in find_allergen_ingredients(foods).items()]
    return sum(ingredient not in allergen_ingredients for food in foods for ingredient in food.ingredients)


def part_two(foods):
    return ','.join([list(v)[0] for k, v in sorted(find_allergen_ingredients(foods).items(), key=lambda item: item[0])])


def find_allergen_ingredients(foods):
    return remove_known_allergens(find_candidates(foods))


def find_candidates(foods):
    candidates = {}
    for allergen in set().union(*[food.allergens for food in foods]):
        foods_ = [food for food in foods if allergen in food.allergens]
        candidates[allergen] = set()
        for food in foods_:
            for ingredient in food.ingredients:
                if all(ingredient in food.ingredients for food in foods_):
                    candidates[allergen].add(ingredient)
    return candidates


def remove_known_allergens(candidates):
    while any(len(ingredients) > 1 for ingredients in candidates.values()):
        for allergen in candidates:
            if len(candidates[allergen]) == 1:
                for allergen_ in candidates:
                    if len(candidates[allergen_]) > 1:
                        remove_known_allergen(candidates, allergen, allergen_)
    return candidates


def remove_known_allergen(candidates, allergen, allergen_):
    for ingredient in candidates[allergen]:
        if ingredient in candidates[allergen_]:
            candidates[allergen_].remove(ingredient)


def get_foods():
    return [Food(line) for line in open('2020/input/day21').read().strip().split("\n")]


print(part_one(get_foods()))
print(part_two(get_foods()))
