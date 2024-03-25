import unittest
from unittest.mock import patch
import app
from game.swords import SwordsSecond

# Клас повинен починатись з слова Test
class TestGame(unittest.TestCase):
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
    pass

class TestSwords(unittest.TestCase):
    pass


if __name__ == "__main__":
    unittest.main(verbosity=2)