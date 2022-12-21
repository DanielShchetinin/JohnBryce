class Person:
    def __init__(self, id:int, first_name:str, last_name:str, addres:str, phone_number:list, birth_year:int):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.addres = addres
        self.phone_number = phone_number
        self.birth_year = birth_year
        
        def getName(self):
            return {first_name}
            
        "self.age = age"

def main():
    count_profiles = 0
    first_person = False
    profiles = []
    profiles_dict = {}
    
    
    mainMenu(first_person, count_profiles, profiles, profiles_dict)
    
    
def mainMenu(first_person, count_profiles, profiles, profiles_dict):
    
    actions_profile = (
    "See information about this profile",
    "Edit information in this profile",
    "Exit"
    )
    
    person_miss = (
    "Create new profile",
    "Exit"
    )
    
    options = (
    "Profiles",
    "Exit"
    )
    
    option = None
    person_miss_option = None
    choose_profile = None
    choose_profile = None
    option_list = "\n".join([f"{idx + 1}. {act}" for idx, act in enumerate(options)])
    not_created = "\n".join([f"{idx + 1}. {act}" for idx, act in enumerate(person_miss)])
    actions_profile = "\n".join([f"{inx + 1}. {act}" for inx, act in enumerate(actions_profile)])

    print('\n')
    print("\n| ---------- Avaliable actions ---------- |:\n")
    print(option_list)
    print('\n')
    
    #tester
    # first_person = True
    # profiles.append(213731102)
    # profiles[0]  = Person(213731102, "Daniel", "Nuger", "Ashdod", 972537200511, 2002)
    # count_profiles += 1


    option = int(input("--> Insert your choose action: "))
    
    if option == 1:
        if first_person == True:
            for idx, profile in enumerate(profiles_dict):
                print(f"\n{idx+1}. {profiles_dict[213731102].first_name} {profiles_dict[213731102].last_name}.")
                new_profile_idx = (idx+1)
            print(f"\n{new_profile_idx+1}. Create new profile.")
            choose_profile = int(input("\n--> Insert your choose action: "))
            if choose_profile == new_profile_idx+1:
                createPerson(first_person, count_profiles, profiles, profiles_dict)
            if choose_profile == idx+1:
                print('\n')
                print(f"\n| ---------- Actions for {profiles[idx].first_name} {profiles[idx].last_name} ---------- |\n")
                print(actions_profile)
                print('\n')
                
                action = int(input("--> Insert your choose action: "))
                
        
                if action == 1:
                    print("\n")
                    print(f"ID: {profiles[idx].id}")
                    print(f"First name: {profiles[idx].first_name}")
                    print(f"Last name : {profiles[idx].last_name}")
                    print(f"Addres: {profiles[idx].addres}")
                    print(f"Birth year: {profiles[idx].birth_year}")
                    print(f"Age: {profiles[idx].age}")
                    print("\n")
                    print(f"Phone number: {profiles[idx].phone_number}")
                    print("\n")
                    print(f"1. Exit")
                    action = int(input("--> Insert your choose action: "))
                    if action == 1:
                        
                        
                        mainMenu(first_person, count_profiles, profiles, person_choosen, profile_numbers)
                
                if action == 2:  
                    person_choosen = idx    
                    changeUserInfo(first_person, count_profiles, profiles, person_choosen, profile_numbers)
                        
                if action == 3:
                    mainMenu(first_person, count_profiles, profiles, profiles_dict)
                if action == 3:
                    mainMenu(first_person, count_profiles, profiles, profiles_dict)

            
        if first_person == False:
            print("\n| ---------- Profile not found ---------- |")
            print('\n')
            print(not_created)
            print('\n')
            person_miss_option = int(input("--> Insert your choose action: "))
            if person_miss_option == 1:
                first_person = True
                createPerson(first_person, count_profiles, profiles, person_choosen, profile_numbers)
            if person_miss_option == 2:
                mainMenu(first_person, count_profiles, profiles, person_choosen, profile_numbers)
                createPerson(first_person, count_profiles, profiles, profiles_dict)
            if person_miss_option == 2:
                mainMenu(first_person, count_profiles, profiles, profiles_dict)

        
    if option == 2:
            stop()

def createPerson(first_person, count_profiles, profiles, person_choosen, profile_numbers):
    print("\n| ---------- Create Person ---------- |:\n")
    while True:
        id = input("Enter your ID: ")
        first_name = input("Enter your first name: ")
        last_name = input("Enter your last name: ")
        addres = input("Enter your addres: ")
        phone_number = input("Enter your phone number: ")
        birth_year = input("Enter your birth year: ")
        print('\n')
        print("\n| ---------- Agree the information ---------- |:\n")
        print(f"ID: {id}")
        print(f"First name: {first_name}")
        print(f"Last name : {last_name}")
        print(f"Addres: {addres}")
        print(f"Phone number: {phone_number}")
        print(f"Birth year: {birth_year}")
        while True:
            agree = input("\n--> To Agree or Decline this informaton Enter [Agree or Decline]: ").title()
            if agree == "Agree":
                profiles.append(id)                
                profiles[int(count_profiles)] = Person(id, first_name, last_name, addres, phone_number, birth_year)
                print(f"\nProfile", profiles[int(count_profiles)].first_name, profiles[int(count_profiles)].last_name, "is been saved!")
                count_profiles += 1
                break
            if agree == "Decline":
                createPerson(first_person, count_profiles, profiles, person_choosen, profile_numbers)
            if agree != "Agree" or agree != "Decline":
                continue
            break
        break
    mainMenu(first_person, count_profiles, profiles, person_choosen, profile_numbers)
        
def changeUserInfo(first_person, count_profiles, profiles, person_choosen, profile_numbers):
    changeOptions_list = (
    "Change Age",
    "Add Number",
    "Delete Number"
    )
    changeOptions = "\n".join([f"{inx + 1}. {act}" for inx, act in enumerate(changeOptions_list)])
    
    
    print('\n')
    print(changeOptions)
    print('\n')
    changeChoose = int(input("--> Insert your choose action: "))
    
    if changeChoose == 1:
        new_age = int(input(f"\n--> Insert a new Age for {profiles[person_choosen].first_name} {profiles[person_choosen].last_name}: "))
        profiles[person_choosen].age = new_age
        mainMenu(first_person, count_profiles, profiles, person_choosen, profile_numbers)

    # if changeChoose == 2:
    #     print(profile_numbers)
        
    #     new_age = int(input(f"\n--> Insert a new Age for {profiles[person_choosen].first_name} {profiles[person_choosen].last_name}: "))
    #     profiles[person_choosen].age = new_age
    #     mainMenu(first_person, count_profiles, profiles, person_choosen, profile_numbers)
        
def stop():
    print("\n"*25, "Programm is been stopped!\n\n")
    exit()



if __name__ == '__main__':
    main()
    