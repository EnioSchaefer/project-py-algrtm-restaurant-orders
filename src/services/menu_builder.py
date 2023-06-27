from typing import Dict, List
from services.inventory_control import InventoryMapping
from services.menu_data import MenuData

DATA_PATH = "data/menu_base_data.csv"
INVENTORY_PATH = "data/inventory_base_data.csv"


def build_full_dish(dish):
    return {
        "dish_name": dish.name,
        "ingredients": dish.get_ingredients(),
        "price": dish.price,
        "restrictions": dish.get_restrictions(),
    }


def check_restrictions(dish_restrictions, restriction):
    is_restricted = list()
    for curr_restriction in dish_restrictions:
        is_restricted.append(curr_restriction.__eq__(restriction))
    return any(is_restricted)


class MenuBuilder:
    def __init__(self, data_path=DATA_PATH, inventory_path=INVENTORY_PATH):
        self.menu_data = MenuData(data_path)
        self.inventory = InventoryMapping(inventory_path)

    def make_order(self, dish_name: str) -> None:
        try:
            curr_dish = [
                dish
                for dish in self.menu_data.dishes
                if dish.name == dish_name
            ][0]
        except IndexError:
            raise ValueError("Dish does not exist")

        self.inventory.consume_recipe(curr_dish.recipe)

    # Req 4
    def get_main_menu(self, restriction=None) -> List[Dict]:
        menu = self.menu_data.dishes

        full_dishes = list()
        for dish in menu:
            is_available = self.inventory.check_recipe_availability(
                dish.recipe
            )
            if restriction is None and is_available:
                full_dishes.append(build_full_dish(dish))
            else:
                dish_restrictions = dish.get_restrictions()
                is_restricted = check_restrictions(
                    dish_restrictions, restriction
                )
                if not is_restricted and is_available:
                    full_dishes.append(build_full_dish(dish))

        return full_dishes


MenuBuilder().get_main_menu()
