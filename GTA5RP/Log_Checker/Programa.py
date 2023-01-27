space_visual = "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
frac_choosed = None
def main(frac_choosed):
    if frac_choosed == None:
        frac_choosed = "Не выбрано"
        
    welcome_menu_options = ["Начать проверку.", f"Выбор фракции | {frac_choosed}.", "Информация по использованию."]
    welcome_menu = "\n".join([f"| {inx+1}. {opt}" for inx, opt in enumerate(welcome_menu_options)])
    print('\n')
    print("\n| ━━━━━━━━━━━━ Logs Checker ━━━━━━━━━━━━ |\n")
    print(welcome_menu)
    print('\n')
    main_choose = input("| Enter a number from the list: ")
    if main_choose == "/exit":
        exit()
    nums = ["1","2","3"]
    if main_choose == None or main_choose not in nums:
        print(space_visual)
        print("Ошибка, Попробуйте еще раз!")
        main(frac_choosed)
    main_choose = int(main_choose)
    
    if main_choose == 1:
        fraction_list_check = ["LSPD", "LSSD", "FIB", "GOV", "ARMY", "SASPA", "EMS"]
        if frac_choosed in fraction_list_check:
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n| ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ |")
            print("| ━━━━━━ Обработка логов, Ожидайте ━━━━━ |")
            print("| ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ |\n\n\n\n\n\n")
            log_checker_system()
        if frac_choosed == "Ошибка, Введите верную фракцию" or frac_choosed == "Не выбрано":
            print(space_visual, "Для начала проверки логов - Выберите фракцию!")
            main(frac_choosed)

    if main_choose == 2:
        frac_choosed = fraction_choose()
        print(space_visual)
        main(frac_choosed)

    if main_choose == 3:
        print('\n')
        print("\n| ━━━━━━━━━━━━ Use Info ━━━━━━━━━━━━ |\n")
        print('''File "Staff.txt":\n
            Файл должен содержать в себе список логов "Фракции" в данном формате:
            Franklin_Morene	15
            Aron Hoffman	14
            Daniel_Gyro     13
            Aiden Morrius   12
            
            Так же можно добавить в файл тех кто уже не во фракции и получили ранее WARN либо были уволен.
            Форматы логов:
            
            WARNS:
            10	Daniel_Gyro	LSPD	Выгоняется за грубое нарушение (( warn ))	17.01.2023, 00:35:23
            9	Aron_Hoffman	LSPD	Выгоняется за грубое нарушение (( warn ))	17.03.2023, 01:31:52
            
            Уволенение:
            53	Aron_Hoffman	LSPD	Увольняет Daniel_Gyro[111111]	17.01.2023, 14:15:05
            51	Aiden_Morrius	LSPD	Увольняет Alexander_Tinkoff[222222]	16.01.2023, 23:30:14
            
            Уволение по VIP:
            52	Daniel_Gyro	LSPD	Увольняется по собственному желанию	17.01.2023, 14:06:54
            41	Aiden_Morrius	LSPD	Увольняется по собственному желанию	17.01.2023, 14:06:54
        ''')
        while True:
            escape = input("For exit to main menu enter - [1]: ")
            if escape == "1":
                print(space_visual)
                main(frac_choosed, frac_names, car_log, apartament_log, home_log, armour_log, familiy_log)
            if main_choose == None or main_choose != "1":
                print(space_visual)
                print("Ошибка")
                continue
    
def fraction_choose():
    fraction_list = ["LSPD", "LSSD", "FIB", "GOV", "ARMY", "SASPA", "EMS"]
    fraction_print = "\n".join([f"| {inx+1}. {opt}" for inx, opt in enumerate(fraction_list)])
    print(space_visual)
    print("\n| ━━━━━━━━━━━━ Fraction choose ━━━━━━━━━━━━ |\n")
    print(fraction_print)
    print('\n')
    fraction_input = input("| Enter a number from the list: ")
    nums = ["1","2","3","4","5","6","7"]
    if fraction_input == None or fraction_input not in nums:
        frac_choosed = "Ошибка, Введите верную фракцию"
        return frac_choosed
    else:
        fraction_input = fraction_list[int(fraction_input)-1]
        frac_choosed = fraction_input
        return frac_choosed

def read_names_file(filename):
    frac_names = []
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            if "Пополняет" in line:
                continue
            if "warn" in line:
                name = line.strip().split("\t")
                name = name[1]
                frac_names.append((name))
                continue
            if "Увольняет " in line:
                name = line.strip().split("\t")
                name = name[3].split(" ")
                name = name[1].split("[")
                name = name[0]
                frac_names.append((name))
                continue
            if "Увольняется" in line:
                name = line.strip().split("\t")
                name = name[1]
                frac_names.append((name))
                continue            
            
            else:
                
                name = line.strip().split("\t")
                name = name[0]
                name_for_process = name.split(" ")
                name = name_for_process[0]
                if name in frac_names:
                    continue
            frac_names.append((name))
    return frac_names

def check_warn_names(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        warned_names = []
        for line in file:
            if "warn" in line:
                name = line.strip().split("\t")
                name = name[1]
                warned_names.append((name))
                continue
    return warned_names

def check_leave_names(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        leave_names = []
        for line in file:
            if "Увольняет " in line:
                name = line.strip().split("\t")
                name = name[3].split(" ")
                name = name[1].split("[")
                name = name[0]
                leave_names.append((name))
                continue
    return leave_names

def check_vip_leave_names(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        vip_leave_names = []
        for line in file:
            if "Увольняется" in line:
                name = line.strip().split("\t")
                name = name[1]
                vip_leave_names.append((name))
                continue
    return vip_leave_names


def read_car_file(filename):
    car_log = []
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            if line == " " or line == "\t":
                continue
            log = line.strip().split("\t")
            car_log.append((log))
    return car_log

def read_apartament_file(filename):
    apartament_log = []
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            if line == " " or line == "\t":
                continue
            log = line.strip().split("\t")
            apartament_log.append((log))
    return apartament_log

def read_home_file(filename):
    home_log = []
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            if line == " " or line == "\t":
                continue
            log = line.strip().split("\t")
            home_log.append((log))
    return home_log

def read_armour_file(filename):
    armour_log = []
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            if line == " " or line == "\t":
                continue
            log = line.strip().split("\t")
            armour_log.append((log))
    return armour_log

def read_familiy_file(filename):
    familiy_log = []
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            if line == " " or line == "\t":
                continue
            log = line.strip().split("\t")
            familiy_log.append((log))
    return familiy_log

frac_names = read_names_file('names.txt')
warned_names = check_warn_names('names.txt')
leave_names = check_leave_names('names.txt')
vip_leave_names = check_vip_leave_names('names.txt')
car_log = read_car_file('cars.txt')
apartament_log = read_apartament_file('apartament.txt')
home_log = read_home_file('home.txt')
armour_log = read_armour_file('armour.txt')
familiy_log = read_familiy_file('familiy.txt')

def log_checker_system():
    apartament_per_name = {}
    cars_per_name = {}
    armour_per_name = {}
    home_per_name = {}
    familiy_per_name = {}
    
    matched_names = []
    not_matched_names = []
    for name in frac_names:
        if name not in matched_names: 
            cars_per_name[name] = []
            apartament_per_name[name] = []
            armour_per_name[name] = []
            home_per_name[name] = []
            familiy_per_name[name] = []
            
        for log in car_log:
            if len(log[1].split(" ")) != 2:
                continue
            if len(log[1].split(" ")) == 2:
                log[1] = log[1].split(" ")
                static = log[1][1]
                log[1] = log[1][0]
                name_for_match = log[1]
                log[1] = log[1] + " " + static
                if name == name_for_match:
                    cars_per_name[name].append(log)
                    if name not in matched_names:
                        matched_names.append(name)
                        
        for log in apartament_log:
            if len(log[1].split(" ")) != 2:
                continue
            if len(log[1].split(" ")) == 2:
                log[1] = log[1].split(" ")
                static = log[1][1]
                log[1] = log[1][0]
                name_for_match = log[1]
                log[1] = log[1] + " " + static
                if name == name_for_match:
                    apartament_per_name[name].append(log)
                    if name not in matched_names:
                        matched_names.append(name)
                    
        for log in armour_log:
            if len(log[1].split(" ")) != 2:
                continue
            if len(log[1].split(" ")) == 2:
                log[1] = log[1].split(" ")
                static = log[1][1]
                log[1] = log[1][0]
                name_for_match = log[1]
                log[1] = log[1] + " " + static
                if name == name_for_match:
                    armour_per_name[name].append(log)
                    if name not in matched_names:
                        matched_names.append(name)
            if len(log[2].split(" ")) == 2:
                log[2] = log[2].split(" ")
                static = log[2][1]
                log[2] = log[2][0]
                name_for_match = log[2]
                log[2] = log[2] + " " + static
                if name == name_for_match:
                    armour_per_name[name].append(log)
                    if name not in matched_names:
                        matched_names.append(name)
                        
        for log in familiy_log:
            if len(log[1].split(" ")) != 2:
                continue
            if len(log[1].split(" ")) == 2:
                log[1] = log[1].split(" ")
                static = log[1][1]
                log[1] = log[1][0]
                name_for_match = log[1]
                log[1] = log[1] + " " + static
                if name == name_for_match:
                    familiy_per_name[name].append(log)
                    if name not in matched_names:
                        matched_names.append(name)
                        
        for log in home_log:
            if len(log[1].split(" ")) == 2:
                log[1] = log[1].split(" ")
                static = log[1][1]
                log[1] = log[1][0]
                name_for_match = log[1]
                log[1] = log[1] + " " + static
                if name == name_for_match:
                    home_per_name[name].append(log)
                    if name not in matched_names:
                        matched_names.append(name)
                        
        if name in matched_names:
            continue
        if name in not_matched_names:
            continue
        if name not in matched_names and name not in not_matched_names:
            not_matched_names.append(name)
        
        
    with open('result.txt', 'a', encoding='utf-8') as f:
        for name in matched_names:
            f.write("\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n")
            
            if name in warned_names and name in vip_leave_names and name in leave_names:
                f.write(f'\nИгрок {name} совпадает в логах || Статус(ы): Warn, Уволен, VIP Уволнение\nЛоги: \n')
            
            if name in warned_names and name in vip_leave_names and name not in leave_names:
                f.write(f'\nИгрок {name} совпадает в логах || Статус(ы): Warn, VIP Уволнение\nЛоги: \n')
                
            if name in warned_names and name not in vip_leave_names and name in leave_names:
                f.write(f'\nИгрок {name} совпадает в логах || Статус(ы): Warn, Уволен\nЛоги: ')
                
            if name not in warned_names and name in vip_leave_names and name in leave_names:
                f.write(f'\nИгрок {name} совпадает в логах || Статус(ы): VIP Уволнение, Уволен\nЛоги: \n')
                
            if name in warned_names and name not in vip_leave_names and name not in leave_names:
                f.write(f'\nИгрок {name} совпадает в логах || Статус: Warn\nЛоги: \n')
                
            if name in leave_names and name not in warned_names and name not in vip_leave_names:
                f.write(f'\nИгрок {name} совпадает в логах || Статус: Уволен\nЛоги: \n')
                
            if name in vip_leave_names and name not in leave_names and name not in warned_names:
                f.write(f'\nИгрок {name} совпадает в логах || Статус: VIP Уволнение\nЛоги: \n')
                
            if name not in vip_leave_names and name not in leave_names and name not in warned_names:
                f.write(f'\nИгрок {name} совпадает в логах || Статус: Сейчас во фракции\nЛоги: \n')
            
            if len(cars_per_name[name]) != 0:
                f.write("\nАвтомобиль:\n")
                for log in cars_per_name[name]:
                    f.write(' '.join(log))
                    f.write("\n")
            if len(apartament_per_name[name]) != 0:
                f.write("\nАпартаменты:\n")
                for log in apartament_per_name[name]:
                    f.write(' '.join(log))
                    f.write("\n")
            if len(home_per_name[name]) != 0:
                f.write("\nДом:\n")
                for log in home_per_name[name]:
                    f.write(' '.join(log))
                    f.write("\n")
            if len(familiy_per_name[name]) != 0:
                f.write("\nСемья:\n")
                for log in familiy_per_name[name]:
                    f.write(' '.join(log))
                    f.write("\n")
            if len(armour_per_name[name]) != 0:
                f.write("\nБроня:\n")
                for log in armour_per_name[name]:
                    f.write(' '.join(log))
                    f.write("\n")
        f.write("\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

    for name in matched_names:
        print("\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        
        if name in warned_names and name in vip_leave_names and name in leave_names:
            print(f'\nИгрок {name} совпадает в логах || Статус(ы): Warn, Уволен, VIP Уволнение\nЛоги: ')
        
        if name in warned_names and name in vip_leave_names and name not in leave_names:
            print(f'\nИгрок {name} совпадает в логах || Статус(ы): Warn, VIP Уволнение\nЛоги: ')
            
        if name in warned_names and name not in vip_leave_names and name in leave_names:
            print(f'\nИгрок {name} совпадает в логах || Статус(ы): Warn, Уволен\nЛоги: ')
            
        if name not in warned_names and name in vip_leave_names and name in leave_names:
            print(f'\nИгрок {name} совпадает в логах || Статус(ы): VIP Уволнение, Уволен\nЛоги: ')
            
        if name in warned_names and name not in vip_leave_names and name not in leave_names:
            print(f'\nИгрок {name} совпадает в логах || Статус: Warn\nЛоги: ')
            
        if name in leave_names and name not in warned_names and name not in vip_leave_names:
            print(f'\nИгрок {name} совпадает в логах || Статус: Уволен\nЛоги: ')
            
        if name in vip_leave_names and name not in leave_names and name not in warned_names:
            print(f'\nИгрок {name} совпадает в логах || Статус: VIP Уволнение\nЛоги: ')
            
        if name not in vip_leave_names and name not in leave_names and name not in warned_names:
            print(f'\nИгрок {name} совпадает в логах || Статус: Сейчас во фракции\nЛоги: ')
            
            
        if len(cars_per_name[name]) != 0:
            print("\nАвтомобиль:\n")
            for log in cars_per_name[name]:
                print(' '.join(log))
        if len(apartament_per_name[name]) != 0:
            print("\nАпартаменты:\n")
            for log in apartament_per_name[name]:
                print(' '.join(log))
        if len(home_per_name[name]) != 0:
            print("\nДом:\n")
            for log in home_per_name[name]:
                print(' '.join(log))
        if len(familiy_per_name[name]) != 0:
            print("\nСемья:\n")
            for log in familiy_per_name[name]:
                print(' '.join(log))
        if len(armour_per_name[name]) != 0:
            print("\nБроня:\n")
            for log in armour_per_name[name]:
                print(' '.join(log))
        
        
        
        
    show_not_match = input("\nПоказать имена из 'names.txt' которые не совпадают в логах? [1. Да/2. Нет]: ")
    show_not_match = int(show_not_match)
    if show_not_match == 1:
        procces = '\n'.join(f"{inx+1}. {name_not}" for inx, name_not in enumerate(not_matched_names))
        print()
        print("\nИмена которые не совпадают:")
        print()
        print(procces)
        print()
    if show_not_match == 2:
        print("\nДосвидание Админчик")    
        
if __name__ == '__main__':
    main(frac_choosed)