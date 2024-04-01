import unittest
from unittest.mock import patch
from random import choice
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
        """Задаємо початкові дані, створюємо Меч для накладання бафів
        rarity: генеруємо випадкову рідкісність меча для тесту;
        obj: створюємо обєкт Меча для тестування;
        buff: обєкт підготовки Меча до накладання бафу;
        """
        self.rarity = choice(list(SwordsSecond.rarity_map.keys()))
        self.obj = SwordsSecond.create_with_rarity('Меч для тренуваня', self.rarity)
        self.buff = Buff(self.obj)
        return super().setUp()
    
    def tearDown(self) -> None:
        """Очищеємо всі дані після виконання тесту
        Видаливши атрибут обєкта self ми також видалимо всі дані які були присвоєні даному атрибуту"""
        delattr(self, "rarity")
        delattr(self, "obj")
        delattr(self, "buff")
        return super().tearDown()
    
    @classmethod
    def tearDownClass(cls):
        print(f">>>>>>>>>>>В процесі тестування Бафів {cls} було створено {SwordsSecond.total_swords} Мечів<<<<<<<<<<")
    
    def test_apply_sharpening(self):
        """Тестуємо правильність накладання бафу Заточення на меч"""
        # 1- Задання початкових ресурсів, деколи ця частина повторюється і тому її краще винести в окремий зарезервовану функцію
        # ми винесли логіку частини 1 до методу setUp
        #rarity = 'White'
        #obj = SwordsSecond.create_with_rarity('Меч для тренуваня', rarity)
        ##print(f"ДЕБАГ: {obj.damage}")
        #buff = Buff(obj)
        
        # 2 - виклик тестованих компонентів
        result = self.buff.sharpening()
        #print(f"ДЕБАГ: {obj.damage}")
        # 3 - тестування, перевірка результатів тверджень
        self.assertIsInstance(result, str, "Повернене значення після накледення бафу не є стрічкою.")
        self.assertTrue(len(result) >= 10, "Повернене значення після накладення бафу є дуже коротким.")
        for attr in ['name', 'damage', 'vitality']:
            # тут робиться перевірки чи існують атрибути і чи ми можемо їх в подальшому викликати
            self.assertTrue(hasattr(self.buff, attr), "Атрибут не існує у об'єкті класу.")
            # якщо будо застосовано баф то відповідні атрибути повинні бути відмінними від None
            self.assertIsNotNone(getattr(self.buff, attr), f"Не задано атрибут {attr} при накладенні Бафу.")

        self.assertIsInstance(getattr(self.buff, 'damage'), (int, float), "Значення Шкоди та Витривалості повинне бути чисельного типу.")
        # Тестуємо формулу обрахунку нанесення шкоди відносно рідкісності Меча
        i = list(self.obj.rarity_map.keys()).index(self.rarity)
        self.assertEqual(3 + i + getattr(self.buff, 'damage'), self.obj.damage, "Невірне розраховане значення Шкоди при складенні всіх компонентів.")
        
        # ми вже перевірили що атрибут name існує тому ми можемо його тут викликати
        self.assertIsInstance(self.buff.name, str, "Імя накладеного бафу повинно бути стрічкою.")
        self.assertEqual(self.buff.name, "Заточення", f"При застосування бафу Заточення було задано невірне імя {self.buff.name}.")

    
    def test_apply_poisoning(self):
        """Тестуємо правильність змазування Меча отрутою"""
        # 1 - задання початкових даних - в методі СетАп

        # 2 - виклик коду який тестується
        result = self.buff.poisoning()

        # 3 - перевірка тведржень
        for attr in ['name', 'damage', 'vitality']:
            self.assertTrue(hasattr(self.buff, attr), "Атрибут не існує у об'єкті класу.")
            self.assertIsNotNone(getattr(self.buff, attr), f"Не задано атрибут {attr} при накладенні Бафу.")
        # Як бачимо твердження для подібних функцій будуть оданковими, і в найпростішому випадку ми можемо просто скопіювати код
        # Базово нам потрібно протестувати: обєкт та ініціалізація/зміна його атрибутів, результи що повертається з тестованоо коду
        # а також можливе виникнення помилок (exceptions) або виловлювати чи будуть виликані певні функції
    

    def test_apply_enchantment(self):
        """Тестуємо правильність накладання зачарування"""
        # 1 - задання початкових даних - в методі СетАп

        # Підмініємо ініціалізацію шкоди та витривалості, бо ми знаємо що вони будуть задаватись за допомогою int
        with patch('builtins.int', return_value=1):
            result = self.buff.enchantment()
            self.assertEqual(self.buff.damage, 1, f"Поточне значення {self.buff.damage} і не збігається з прогнозованим")
            self.assertEqual(self.buff.vitality, 1, f"Поточне значення {self.buff.vitality} і не збігається з прогнозованим")


class TestSwords(unittest.TestCase):
    pass


if __name__ == "__main__":
    unittest.main(verbosity=2)