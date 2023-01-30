space_visual = "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
print(space_visual)

while True:
    nick = input("Введите полный ник/статик игрока: ")

    nakazanie_list = ["4.13 правила проекта", "1.6 правила гос. структур", "1.7 правила гос. структур", "1.6.1 правила гос. структур", "Меню ввода имени нарушителя"]
    nakazanie_print = "\n".join([f"| {inx+1}. {opt}" for inx, opt in enumerate(nakazanie_list)])
    print(space_visual)
    print("\n| ━━━━━━━━━━━━ Выберите наказание ━━━━━━━━━━━━ |\n")
    print(nakazanie_print)
    print('\n')
    nakazanie_choose = int(input("Введите свой выбор: "))

    if nakazanie_choose == 1:
        print(space_visual)
        print(nick, "Добавлен в список наказание!\n")
        with open('Punishment.txt', 'a', encoding='utf-8') as f:
            f.write(f"\noffprison {nick} 240 4.13 правила проекта // By Gyro\n")
            f.write(f"offwarn {nick} 4.13 правила проекта // By Gyro")
        
    if nakazanie_choose == 2:
        print(space_visual)
        print(nick, "Добавлен в список наказание!\n")
        with open('Punishment.txt', 'a', encoding='utf-8') as f:
            f.write(f"\noffprison {nick} 240 1.6 правила гос. структур // By Gyro\n")
            f.write(f"offwarn {nick} 1.6 правила гос. структур // By Gyro")
        
    if nakazanie_choose == 3:
        print(space_visual)
        print(nick, "Добавлен в список наказание!\n")
        with open('Punishment.txt', 'a', encoding='utf-8') as f:
            f.write(f"\noffprison {nick} 240 1.7 правила гос. структур // By Gyro\n")
            f.write(f"offwarn {nick} 1.7 правила гос. структур // By Gyro")
        
    if nakazanie_choose == 4:
        print(space_visual)
        print(nick, "Добавлен в список наказание!\n")
        with open('Punishment.txt', 'a', encoding='utf-8') as f:
            f.write(f"\noffprison {nick} 240 1.6.1 правила гос. структур // By Gyro\n")
            f.write(f"offwarn {nick} 1.6.1 правила гос. структур // By Gyro")
            
    if nakazanie_choose == 5:
        print(space_visual)
        continue