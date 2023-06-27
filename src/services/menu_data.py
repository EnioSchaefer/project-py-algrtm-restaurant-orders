import csv
from models.dish import Dish
from models.ingredient import Ingredient


# Req 3
def find_dish(name, price, dishes):
    for dish in dishes:
        if dish.name == name and dish.price == price:
            return dish
    return None


def generate_dishes(source_path):
    with open(source_path, encoding="utf-8") as file:
        data_reader = csv.reader(file, delimiter=",", quotechar='"')

        dishes = set()
        dish_enumerate = enumerate(data_reader)
        for i, dish in dish_enumerate:
            if i > 0:
                name = dish[0]
                price = float(dish[1])
                ingredient = dish[2]
                quantity = int(dish[3])
                dish_found = find_dish(name, price, dishes)
                if dish_found is not None:
                    dish_found.add_ingredient_dependency(
                        Ingredient(ingredient), quantity)
                else:
                    new_dish = Dish(name, price)
                    new_dish.add_ingredient_dependency(
                        Ingredient(ingredient), quantity)
                    dishes.add(new_dish)
        return dishes


class MenuData:
    def __init__(self, source_path: str) -> None:
        self.source_path = source_path
        self.dishes = generate_dishes(self.source_path)


menu_data = MenuData('tests/mocks/menu_base_data.csv')
