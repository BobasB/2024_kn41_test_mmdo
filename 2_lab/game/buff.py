class Buff:
    def __init__(self, obj) -> None:
        self.name = None
        self.damage = None
        self.vitality = None
        self.obj = obj

    def sharpening(self):
        """Заточення"""
        # Базові значення накладених бафів
        if self.obj.buff:
            return "Неможливо накласти 2 Бафи"
        
        self.name = "Заточення"
        self.damage = 4
        self.vitality = -1
        print(f"Заточення: Шкода {self.damage} ||| Витривалість {self.vitality}")
        self.obj.damage += self.damage
        self.obj.vitality += self.vitality
        return "Меч заточено"
    
    def poisoning(self):
        """Змазуємо Меч отрутою"""
        if self.obj.buff:
            return "Неможливо накласти 2 Бафи"
        self.name = "Отрута"
        self.damage = 2
        self.vitality = 0
        print("Отрута")
        self.obj.damage += self.damage
        return "Змазано отрутою"
    
    def enchantment(self):
        """Зачаровуємо Меч на витривалість"""
        if self.obj.buff:
            return "Неможливо накласти 2 Бафи"
        self.name = "Зачарування"
        self.damage = 0
        self.vitality = 5
        print("Зачарування")
        self.obj.vitality += 5
        return "Накладено чари"
    
    def crystals(self):
        """Застосовуємо криста Мани"""
        if self.obj.buff:
            return "Неможливо накласти 2 Бафи"
        self.name = "Кристал Мани"
        self.damage = -1
        self.vitality = 3
        print("Застосовуємо кристал мани")
        self.obj.vitality += 3
        self.obj.damage -= 1
        return "Застосовано кристал мани"

    def berserk(self):
        """Впадаємо в стан Берсерка"""
        if self.obj.buff:
            return "Неможливо накласти 2 Бафи"
          
        self.name = "Берсерк"
        self.damage = self.obj.damage * 2 # вдвічі збільшуємо значення шкоди 
        self.vitality = self.obj.vitality / 2
        print("Ввійшли в стан Берсерка")
        self.obj.vitality = self.vitality
        self.obj.damage = self.damage
        return "Ввійшли в стан Берсерка"