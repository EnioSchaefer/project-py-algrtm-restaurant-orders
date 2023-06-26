from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient
from src.models.ingredient import Restriction
import pytest


# Req 2
def test_dish():
    dish1_name = "dish1"
    dish1_price = 49.90
    dish2_name = "dish2"
    dish2_price = 29.90
    dish1_repr = f"Dish('{dish1_name}', R${dish1_price:.2f})"
    dish2_repr = f"Dish('{dish2_name}', R${dish2_price:.2f})"
    dish1_restrictions = {Restriction.ANIMAL_DERIVED, Restriction.GLUTEN}
    dish1_ingredients = {Ingredient("ovo"), Ingredient("farinha")}
    dish1 = Dish(dish1_name, dish1_price)
    dish2 = Dish(dish2_name, dish2_price)

    assert dish1.name == dish1_name

    assert dish1.__hash__() != dish2.__hash__()

    assert dish1.__eq__(dish2) is False

    assert dish1.__repr__() == dish1_repr
    assert dish2.__repr__() == dish2_repr

    with pytest.raises(TypeError):
        Dish(123, "abc")

    with pytest.raises(ValueError):
        Dish("abc", -123)

    dish1.add_ingredient_dependency(Ingredient("ovo"), 3)
    dish1.add_ingredient_dependency(Ingredient("farinha"), 1)

    assert dish1.recipe.get(Ingredient("ovo")) == 3
    assert dish1.recipe.get(Ingredient("farinha")) == 1

    assert dish1.get_restrictions() == dish1_restrictions

    assert dish1.get_ingredients() == dish1_ingredients

    dish2 = Dish(dish1_name, dish1_price)

    assert dish1.__hash__() == dish2.__hash__()

    assert dish1.__eq__(dish2) is True
