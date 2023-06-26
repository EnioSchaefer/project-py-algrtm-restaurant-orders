from src.models.ingredient import Ingredient  # noqa: F401, E261, E501
from src.models.ingredient import Restriction


# Req 1
def test_ingredient():
    ingredient1_name = 'queijo provolone'
    ingredient2_name = 'queijo gorgonzola'
    ingredient1_name_repr = f"Ingredient('{ingredient1_name}')"
    ingredient2_name_repr = f"Ingredient('{ingredient2_name}')"
    ingredient_restrictions = {Restriction.LACTOSE, Restriction.ANIMAL_DERIVED}
    ingredient1 = Ingredient(ingredient1_name)
    ingredient2 = Ingredient(ingredient1_name)

    assert ingredient1.__hash__() == ingredient2.__hash__()

    ingredient2 = Ingredient(ingredient2_name)
    assert ingredient1.__hash__() != ingredient2.__hash__()

    assert ingredient1.__eq__(ingredient2) is False

    ingredient2 = Ingredient(ingredient1_name)
    assert ingredient1.__eq__(ingredient2) is True

    ingredient2 = Ingredient(ingredient2_name)
    assert ingredient1.__repr__() == ingredient1_name_repr
    assert ingredient2.__repr__() == ingredient2_name_repr

    assert ingredient1.name == ingredient1_name
    assert ingredient2.name == ingredient2_name

    for restriction in ingredient_restrictions:
        assert restriction in ingredient1.restrictions
        assert restriction in ingredient2.restrictions
