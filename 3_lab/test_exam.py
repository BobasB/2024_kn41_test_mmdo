from game.swords import SwordsSecond

def test_property_rarity_type():
    # тест повинен складатись з 3 частин
    # частина 1 - ініціалізація даних
    test_obj = SwordsSecond.create_with_random_rarity("Меч Екзаменатора")
    # частина 2 - виклик тестовваної функції або коду
    result = test_obj.rarity_type
    # частина 3 - виконання тестування, перевірка тверджень
    assert isinstance(result, str)
