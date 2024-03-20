import unittest
import app

# Клас повинен починатись з слова Test
class TestGame(unittest.TestCase):
        # Кожен тест є функцією, та повинен починатись з слова test
    def test_swords_names(self):
        """Тестуємо правильність імен Мечів"""
        self.assertIsInstance(app.swords_names, list, "Імена мечів мають мітитись у списку!")


class TestBuffs(unittest.TestCase):
    pass

class TestSwords(unittest.TestCase):
    pass


if __name__ == "__main__":
    unittest.main(verbosity=2)