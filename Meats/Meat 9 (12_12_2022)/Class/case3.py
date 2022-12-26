pythonbank = """\n\
░██╗░░░░░░░██╗███████╗██╗░░░░░░█████╗░░█████╗░███╗░░░███╗███████╗  ████████╗░█████╗░
░██║░░██╗░░██║██╔════╝██║░░░░░██╔══██╗██╔══██╗████╗░████║██╔════╝  ╚══██╔══╝██╔══██╗
░╚██╗████╗██╔╝█████╗░░██║░░░░░██║░░╚═╝██║░░██║██╔████╔██║█████╗░░  ░░░██║░░░██║░░██║
░░████╔═████║░██╔══╝░░██║░░░░░██║░░██╗██║░░██║██║╚██╔╝██║██╔══╝░░  ░░░██║░░░██║░░██║
░░╚██╔╝░╚██╔╝░███████╗███████╗╚█████╔╝╚█████╔╝██║░╚═╝░██║███████╗  ░░░██║░░░╚█████╔╝
░░░╚═╝░░░╚═╝░░╚══════╝╚══════╝░╚════╝░░╚════╝░╚═╝░░░░░╚═╝╚══════╝  ░░░╚═╝░░░░╚════╝░

██████╗░██╗░░░██╗████████╗██╗░░██╗░█████╗░███╗░░██╗  ██████╗░░█████╗░███╗░░██╗██╗░░██╗
██╔══██╗╚██╗░██╔╝╚══██╔══╝██║░░██║██╔══██╗████╗░██║  ██╔══██╗██╔══██╗████╗░██║██║░██╔╝
██████╔╝░╚████╔╝░░░░██║░░░███████║██║░░██║██╔██╗██║  ██████╦╝███████║██╔██╗██║█████═╝░
██╔═══╝░░░╚██╔╝░░░░░██║░░░██╔══██║██║░░██║██║╚████║  ██╔══██╗██╔══██║██║╚████║██╔═██╗░
██║░░░░░░░░██║░░░░░░██║░░░██║░░██║╚█████╔╝██║░╚███║  ██████╦╝██║░░██║██║░╚███║██║░╚██╗
╚═╝░░░░░░░░╚═╝░░░░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░╚═╝░░╚══╝  ╚═════╝░╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░╚═╝"""

byetext = """\n\
████████╗██╗░░██╗███████╗  ██████╗░██████╗░░█████╗░░██████╗░██████╗░░█████╗░███╗░░░███╗  ██╗░██████╗
╚══██╔══╝██║░░██║██╔════╝  ██╔══██╗██╔══██╗██╔══██╗██╔════╝░██╔══██╗██╔══██╗████╗░████║  ██║██╔════╝
░░░██║░░░███████║█████╗░░  ██████╔╝██████╔╝██║░░██║██║░░██╗░██████╔╝███████║██╔████╔██║  ██║╚█████╗░
░░░██║░░░██╔══██║██╔══╝░░  ██╔═══╝░██╔══██╗██║░░██║██║░░╚██╗██╔══██╗██╔══██║██║╚██╔╝██║  ██║░╚═══██╗
░░░██║░░░██║░░██║███████╗  ██║░░░░░██║░░██║╚█████╔╝╚██████╔╝██║░░██║██║░░██║██║░╚═╝░██║  ██║██████╔╝
░░░╚═╝░░░╚═╝░░╚═╝╚══════╝  ╚═╝░░░░░╚═╝░░╚═╝░╚════╝░░╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░░░░╚═╝  ╚═╝╚═════╝░

██████╗░███████╗███████╗███╗░░██╗  ░██████╗████████╗░█████╗░██████╗░██████╗░███████╗██████╗░██╗
██╔══██╗██╔════╝██╔════╝████╗░██║  ██╔════╝╚══██╔══╝██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗██║
██████╦╝█████╗░░█████╗░░██╔██╗██║  ╚█████╗░░░░██║░░░██║░░██║██████╔╝██████╔╝█████╗░░██║░░██║██║
██╔══██╗██╔══╝░░██╔══╝░░██║╚████║  ░╚═══██╗░░░██║░░░██║░░██║██╔═══╝░██╔═══╝░██╔══╝░░██║░░██║╚═╝
██████╦╝███████╗███████╗██║░╚███║  ██████╔╝░░░██║░░░╚█████╔╝██║░░░░░██║░░░░░███████╗██████╔╝██╗"""

BigSpace = "\n"*11

class Bank:
    def __init__(self, account:int, ID:int, first_name:str, last_name:str, birth_year:int, city:str, phone_number:str):
        self.account = account
        self.ID = ID   
        self.first_name = first_name
        self.last_name = last_name
        self.birth_year = birth_year
        self.city = city
        self.phone_number = phone_number
        
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"
        
print(pythonbank)
      
def main():
    bank_safe = {11111:Bank(11111, 111111111, "Bank", "Director", 1111, "Bank", "1111111111")}
    accounts_count = 11111
    
    mainMenu(bank_safe, accounts_count)
    
def mainMenu(bank_safe: dict, accounts_count: int):
    MainMenuChoose = str(None)
    BankMenuOptions = ["Register a Bank Account", "List of Bank Accounts", "Exit from the Bank"]
    TextBMO = "\n".join([f"| {inx+1}. {opt}" for inx, opt in enumerate(BankMenuOptions)])
    print('\n')
    print("\n| ━━━━━━━━━━━━ Bank Menu ━━━━━━━━━━━━ |:\n")
    print(TextBMO)
    print('\n')
    MainMenuChoose = input("| ---> Insert your choose: ")
    numChecker(MainMenuChoose, BankMenuOptions)
    MainMenuChoose = int(MainMenuChoose)

    if MainMenuChoose == 1:
        createAccount(bank_safe, accounts_count)
    if MainMenuChoose == 2:
        idx = 0
        print("\n| ━━━━━━━━━━━━ List of Bank Accounts ━━━━━━━━━━━━ |:\n")
        for key in (bank_safe):
            print(f"\n{idx+1}. {bank_safe[key].get_full_name()}. [Account Number: {bank_safe[key].account}].")
            idx +=1
        print('\n')
        print(f"{idx+1}. Exit to the Bank Menu.")
        accountChoose = input(f"| ---> Insert your bank acoount number or enter [{idx+1}]: ")
        if accountChoose == idx+1:
            mainMenu(bank_safe, accounts_count)
        #accountOptions(accountChoose)
    if MainMenuChoose == 3:
        stopProgram()

def createAccount(bank_safe: dict, accounts_count: int):
    accounts_count += 1
    account = accounts_count
    print("\n| ━━━━━━━━━━━━ Account Register ━━━━━━━━━━━━ |:\n")
    ID = input("Enter your ID: ")
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    birth_year = input("Enter your birth year: ")
    city = input("Enter your city: ")
    phone_number = str(input("Enter your phone number: "))
    
    bank_safe[account] = Bank(account, ID, first_name, last_name, birth_year, city, phone_number)
    print(f"\nBank account for", bank_safe[account].get_full_name(), "is been saved!")
    mainMenu(bank_safe, accounts_count)




def stopProgram():
    print(f"\n"*25, "The program is been stopped!", "\n"*21, byetext, "\n")
    exit()

def numChecker(MainMenuChoose: str, BankMenuOptions: list):
    if not MainMenuChoose.isnumeric():
        print(f"{BigSpace}Invalid, Please enter only numbers.{BigSpace}")
        return mainMenu()
    bank_count = len(BankMenuOptions)
    MainMenuChoose = int(MainMenuChoose)
    if MainMenuChoose < 0 or MainMenuChoose > bank_count:
        print(f"{BigSpace}Invalid, Please choose only one number from the list.{BigSpace}")
        return mainMenu()


if __name__ == '__main__':
    main()
