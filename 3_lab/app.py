from game.swords import SwordsSecond
from random import shuffle, choice

swords_names = [
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

if __name__ == "__main__":
    player1 = str(input("Введіть імя гравця №1: "))
    s1 = SwordsSecond.create_with_random_rarity(f"{choice(swords_names)} яким володіє {player1}")
    s1.player = player1 # тут ми задаємо динамічний атрибут, який буде вказувати якому гравцю належить даний меч
    player2 = str(input("Введіть імя гравця №2: "))
    s2 = SwordsSecond.create_with_random_rarity(f"{choice(swords_names)} яким володіє {player2}")
    s2.player = player2

    print(f"""
    Гравець №1: {s1.player} володіє Мечем:\n{s1.info}
    Гравець №2: {s2.player} володіє Мечем:\n{s2.info}
    """)

    players = [s1, s2] # згрупував Мечі гравціі у список
    shuffle(players) # помішав список щоб випадково визначити хто буду ходити першим
    MAX_TURNS = 5
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

