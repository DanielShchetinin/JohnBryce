list_code = []

class Person:
    def __init__(self, id:int, first_name:str, last_name:str, addres:str, phone_number:int, birth_year:int):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.addres = addres
        self.phone_number = phone_number
        self.birth_year = birth_year

# info_options = (
#     "Change Age",
#     "Add Number",
#     "Remove Number",
# )

# def main ():
#     getInfoFromUser()

# def chooseNewInfo():
#     option = None
#     option_list = "\n".join([f"{idx + 1}. {act}" for idx, act in enumerate(info_options)])

#     print('\n')
#     print("| ---------- Avaliable actions ---------- |:\n")
#     print(option_list)
#     print('\n')

#     option = input("--> Insert your choose action: ")

#     return (option - 1)

# def getInfoFromUser():
#     print("| ---------- Create Person ---------- |:\n")
#     while True:
#         id = input("Enter your ID: ")
#         first_name = input("Enter your first name: ")
#         last_name = input("Enter your last name: ")
#         addres = input("Enter your addres: ")
#         phone_number = input("Enter your phone number: ")
#         birth_year = input("Enter your birth year: ")
#         code_name = input("\nEnter a profile name: ")
#         print('\n')
#         print("| ---------- Agree the information ---------- |:\n")
#         print(f"""
#     ID: {id}
#     First name: {first_name}
#     Last name : {last_name}
#     Addres: {addres}
#     Phone number: {phone_number}
#     Birth year: {birth_year}
#     Profile name: {code_name}"""
#     )   
#         while True:
#             agree = input("\n--> To Agree or Decline this informaton Enter [Agree or Decline]: ").title()
#             if agree == "Agree":
#                 list_code.append(code_name)
#                 list_code[0] = Person(id, first_name, last_name, addres, phone_number, birth_year)
#                 person = list_code[0]
#                 print(f"\nPerosn {person.first_name} {person.last_name} is been saved as profile {person()}")
#                 return None
#             if agree == "Decline":
#                 getInfoFromUser()
#             if agree != "Agree" or agree != "Decline":
#                 continue
#             break
            



# if __name__ == '__main__':
#     main()
    

list_code = []

code = input("Insert: ")
list_code.append(code)

list_code[0] = Person(213731102, "Daniel", "Nuger", "Ashdod", 537200511, 2002)