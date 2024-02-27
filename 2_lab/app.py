from random import randint, choice, shuffle

# задані характеристики будуть статичними/незмінними
def sword_info(sw:dict):
    """Виводить інформацію про Меч
    :param sw: Словник з характеристиками меча
    """
    print(f"""<<< Характеристика предмету {sw["name"]} >>>
Рідкісність: {sw["rarity"]}
Нанесення Шкоди: {sw["damage"]}
Витривалість: {sw["vitality"]}
Унікальний ефект: {sw["bonus"]}""")


stats_map = {"White": 1, 
             "Blue": 2, 
             "Green": 3, 
             "Red": 5, 
             "Epic": 8, 
             "Legendary": 12}

bonus_map = {"White": None, 
             "Blue": "Вдача +2", 
             "Green": "Вампіризм", 
             "Red": "Покритий отрута", 
             "Epic": ["Вампіризм", "Парирування"], 
             "Legendary": ["Критичний удар +2", "Зцілення +1", "Розкидає бомби"]}

rariry_all = list(stats_map.keys())
shuffle(rariry_all)

print("Ми задонатили та отримали бонус для всього акаунта на 1% до дамагу!")
donate = 1.01

# Закоментуємо ввід даних щоб могти виконати комірку
name = input("Введіть імя гравця: ")
my_value = input(f"Введіть число від 1 до {len(rariry_all)}: ")

rariry = rariry_all[int(my_value)]

sword = {"name": "Двохручний меч", 
         "rarity": rariry, 
         "damage": round(7 * stats_map[rariry] * donate), 
         "vitality": int(8) * stats_map[rariry], 
         "bonus": bonus_map[rariry]}

value = randint(1, 2)
if value > 1:
    print(f"Вітаємо, гравець {name} отримав Меч, його характеристики:")
    sword_info(sword)
else:
    print(f"На жаль, {name} нічого не випало.")
