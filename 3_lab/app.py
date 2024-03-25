from game.swords import SwordsSecond
from random import shuffle, choice

SWORDS_NAMES = [
"Меч Смертівника", 
"Драконобійчий Клинок", 
"Стрілецька Сага", 
"Кований Піднебінник",
"Тіньовий Катана",
"Ластівчиний Клинок",
"Зоряний Рапір",
"Проклятий Кинджал",
"Молот Богів",
"Легендарний Лезо"]

MAX_TURNS = 5

def get_player_name(player_number: int) -> str:
    """Функція для отримання імені гравця."""
    return str(input(f"№{player_number} >>> Введіть ім'я гравця: "))

def create_sword_for_player(player_name: str) -> SwordsSecond:
    """Функція для створення меча для гравця з випадковою рідкісністю."""
    sword_name = f"{choice(SWORDS_NAMES)} отритимав {player_name}"
    sword = SwordsSecond.create_with_random_rarity(sword_name)
    sword.player = player_name # тут ми задаємо динамічний атрибут, який буде вказувати якому гравцю належить даний меч
    return sword


if __name__ == "__main__":

    s1 = create_sword_for_player(get_player_name("1"))
    
    s2 = create_sword_for_player(get_player_name("2"))

    print(f"""
    Гравець №1: {s1.player} володіє Мечем:\n{s1.info}
    Гравець №2: {s2.player} володіє Мечем:\n{s2.info}
    """)

    players = [s1, s2] # згрупував Мечі гравціі у список
    shuffle(players) # помішав список щоб випадково визначити хто буду ходити першим
    
    turn = 1 # починаємо з ходу 1
    #for turn in range(MAX_TURNS):
    while s1.vitality > 0 and s2.vitality > 0 and turn < MAX_TURNS:
        print(f"{10*'<'} РОЗПОЧИНАЄМО ХІД №{turn} {10*'>'}")
        shuffle(players) # помішав список щоб випадково визначити хто буду ходити першим
        for p in players:
            print(f"Випав хід для гравця {p.player}")
            action = int(input("Введіть 1 щоб атакувати, 2 щоб накласти випадковий Баф: "))
            if action == 1:
                # спробуємо видали з списка себе
                pp = players.copy()
                pp.remove(p)
                pp.append("Камінь") # додаємо якийсь обєкт, який не є мечем але ми можемо по ньому вдарити
                print(p.attack(choice(pp)))
            elif action == 2:
                print(p.apply_random_buff())
            else:
                print("Введено неправильне значення, гравець пропускає хід.")
        print(f"""
        <+> Гравець №1: {s1.player} Стати після ходу №{turn}:\n{s1.info}
        <+> Гравець №2: {s2.player} Стати після ходу №{turn}:\n{s2.info}
        """)
        turn += 1
    
    
    print(f"ГРА ЗАВЕРШИЛАСЬ НА {turn} ХОДІ, В ОДНОГО З ГРАВЦІВ ЗЛОМАВСЯ МЕЧ або завершилась кількість ходів")
    print(f"Виграв гравець {s1.player}" if s1.vitality > s2.vitality else f"Виграв гравець {s2.player}")

