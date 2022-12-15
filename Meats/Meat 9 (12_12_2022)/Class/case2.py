class Person:
    def __init__(self, id:int, first_name:str, last_name:str, addres:str, phone_number:int, birth_year:int):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.addres = addres
        self.phone_number = phone_number
        self.birth_year = birth_year
        
        "self.age = age"

def main():
    count_profiles = 0
    
    first_person = False
    
    profiles = []
    
    
    mainMenu(first_person, count_profiles, profiles)
    
    
def mainMenu(first_person, count_profiles, profiles):
    
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

    option = int(input("--> Insert your choose action: "))
    
    if option == 1:
        if first_person == True:
            for idx, profile in enumerate(profiles):
                print(f"\n{idx+1}. {profiles[idx].first_name} {profiles[idx].last_name}.")
                new_profile_idx = (idx+1)
            print(f"\n{new_profile_idx+1}. Create new profile.")
            choose_profile = int(input("\n--> Insert your choose action: "))
            if choose_profile == new_profile_idx+1:
                createPerson(first_person, count_profiles, profiles)
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
                    print(f"Age: {None}")
                    print("\n")
                    print(f"Phone number: {profiles[idx].phone_number}")
                    print("\n")
                    print(f"1. Exit")
                    action = int(input("--> Insert your choose action: "))
                    if action == 1:
                        mainMenu(first_person, count_profiles, profiles)
                if action == 3:
                    mainMenu(first_person, count_profiles, profiles)
            
        if first_person == False:
            print("\n| ---------- Profile not found ---------- |")
            print('\n')
            print(not_created)
            print('\n')
            person_miss_option = int(input("--> Insert your choose action: "))
            if person_miss_option == 1:
                first_person = True
                createPerson(first_person, count_profiles, profiles)
            if person_miss_option == 2:
                mainMenu(first_person, count_profiles, profiles)
        
    if option == 2:
            stop()

def createPerson(first_person, count_profiles, profiles):
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
                createPerson(first_person, count_profiles, profiles)
            if agree != "Agree" or agree != "Decline":
                continue
            break
        break
    mainMenu(first_person, count_profiles, profiles)
        
def changeUserAge(first_person, count_profiles, profiles):
    pass

def stop():
    print("\n"*25, "Programm is been stopped!\n\n")
    exit()



if __name__ == '__main__':
    main()
    