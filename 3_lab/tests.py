import unittest
from unittest.mock import patch
import app
from game.swords import SwordsSecond
from game.buff import Buff

# Клас повинен починатись з слова Test
class TestGame(unittest.TestCase):
    """Тестуємо Базові компоненти гри, основний код запуски."""
        # Кожен тест є функцією, та повинен починатись з слова test
    def test_constants(self):
        """Тестуємо правильність задання константб в нас їх 2 (може бути і більше)"""
        self.assertIsInstance(app.SWORDS_NAMES, list, "Імена мечів мають мітитись у списку!")
        for name in app.SWORDS_NAMES:
            self.assertIsInstance(name, str, "Назва меча не є стрічкою!")
        self.assertIsInstance(app.MAX_TURNS, (int, float))
    
    def test_input_player_name(self):
        """Тестуємо правильність вводу імені гравця з клавіатури"""
        with patch('builtins.input', return_value="Player1"):
            player = app.get_player_name('1')
            self.assertEqual(player, 'Player1', "Введене значення зклавіатури є невірним!")
            self.assertIsInstance(player, str, "Повернене значення, введене з клавіатури не є стрічкою!")

    def test_create_sword_for_player(self):
        """Тестуємо правильність створення меча для введеного імені гравця
        - повине створитись бєкт певного класу;
        - в обєкті присутній певний атрибут;
        - новий атрибут в обєкті повинен відповідати імені гравця;
        - імя гравця повинно бути частиною імені меча;
        """
        sword = app.create_sword_for_player('Player1')
        self.assertIsInstance(sword, SwordsSecond)
        self.assertIn('player', sword.__dict__)
        self.assertEqual(sword.player, 'Player1')
        self.assertIn('Player1', sword.name)


class TestBuffs(unittest.TestCase):
    """Тестуємо бібліотеку яка реалізує бафи для Меча"""
    def setUp(self) -> None:
        return super().setUp()
    
    def test_apply_sharpening(self):
        """Тестуємо правильність накладання бафу Заточення на меч"""
        # 1- Задання початкових ресурсів, деколи ця частина повторюється і тому її краще винести в окремий зарезервовану функцію
        rarity = 'White'
        obj = SwordsSecond.create_with_rarity('Меч для тренуваня', rarity)
        #print(f"ДЕБАГ: {obj.damage}")
        buff = Buff(obj)
        
        # 2 - виклик тестованих компонентів
        result = buff.sharpening()
        #print(f"ДЕБАГ: {obj.damage}")
        # 3 - тестування, перевірка результатів тверджень
        self.assertIsInstance(result, str, "Повернене значення після накледення бафу не є стрічкою.")
        self.assertTrue(len(result) >= 10, "Повернене значення після накладення бафу є дуже коротким.")
        for attr in ['name', 'damage', 'vitality']:
            # тут робиться перевірки чи існують атрибути і чи ми можемо їх в подальшому викликати
            self.assertTrue(hasattr(buff, attr), "Атрибут не існує у об'єкті класу.")
            # якщо будо застосовано баф то відповідні атрибути повинні бути відмінними від None
            self.assertIsNotNone(getattr(buff, attr), f"Не задано атрибут {attr} при накладенні Бафу.")

        self.assertIsInstance(getattr(buff, 'damage'), (int, float), "Значення Шкоди та Витривалості повинне бути чисельного типу.")
        i = list(obj.rarity_map.keys()).index(rarity)
        self.assertEqual(3 + i + getattr(buff, 'damage'), obj.damage, "Невірне розраховане значення Шкоди при складенні всіх компонентів.")
        
        # ми вже перевірили що атрибут name існує тому ми можемо його тут викликати
        self.assertIsInstance(buff.name, str, "Імя накладеного бафу повинно бути стрічкою.")
        self.assertEqual(buff.name, "Заточення", f"При застосування бафу Заточення було задано невірне імя {buff.name}.")

    
    def test_apply_poisoning(self):
        """Тестуємо правильність змазування Меча отрутою"""
        # 1 - задання початкових даних
        rarity = 'Blue'
        obj = SwordsSecond.create_with_rarity('Меч для тренуваня', rarity)
        buff = Buff(obj)

        # 2 - виклик коду який тестується
        result = buff.poisoning()

        # 3 - перевірка тведржень
        for attr in ['name', 'damage', 'vitality']:
            self.assertTrue(hasattr(buff, attr), "Атрибут не існує у об'єкті класу.")
            self.assertIsNotNone(getattr(buff, attr), f"Не задано атрибут {attr} при накладенні Бафу.")
        # Як бачимо твердження для подібних функцій будуть оданковими, і в найпростішому випадку ми можемо просто скопіювати код
        # Базово нам потрібно протестувати: обєкт та ініціалізація/зміна його атрибутів, результи що повертається з тестованоо коду
        # а також можливе виникнення помилок (exceptions) або виловлювати чи будуть виликані певні функції
    

    def test_apply_enchantment(self, ):
        """Тестуємо правильність накладання зачарування"""
        # 1 - задання початкових даних
        rarity = 'Blue'
        obj = SwordsSecond.create_with_rarity('Меч для тренуваня', rarity)
        buff = Buff(obj)

        # Підмініємо ініціалізацію шкоди та витривалості, бо ми знаємо що вони будуть задаватись за допомогою int
        with patch('builtins.int', return_value=1):
            result = buff.enchantment()
            self.assertEqual(buff.damage, 1, f"Поточне значення {buff.damage} і не збігається з прогнозованим")
            self.assertEqual(buff.vitality, 1, f"Поточне значення {buff.vitality} і не збігається з прогнозованим")


class TestSwords(unittest.TestCase):
    pass


if __name__ == "__main__":
    unittest.main(verbosity=2)