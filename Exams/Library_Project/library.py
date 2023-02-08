import datetime
from address import Address
from book import Book
from customer import Customer
from loan import Loan

enter_choose = "| Enter a number from the list: "
visual_space = "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
library_created = False

class Library:
    
    def __init__(self, library_name: str, library_address):
        
        self._library_name = library_name
        self._library_address = library_address
        
        self._books: dict[int, Book] = {}
        self._customers: dict[int, Customer] = {}
    
    def create_library(self, library_name: str, library_address):
        print(library_name)
        print(library_address)
        Library(library_name, library_address)
        return True
        
    def get_library_name(self):
        return self._library_name
    
    def get_library_address(self):
        return self._library_address

    def add_customer(self, customer_id: int, customer_first_name: str, customer_last_name: str, address: Address, email: str, birth_date: datetime.date):
        if customer_id in self._customers:
            return False
        self._customers[customer_id] = Customer(customer_id, customer_first_name, customer_last_name, address, email, birth_date)
        return True
    
    def add_book(self, book_id: int, book_name: str, book_autor: str, published_year: int, book_type: int = 3):
        if book_id in self._customers:
            return False
        self._books[book_id] = Book(book_id, book_name, book_autor, published_year, book_type)
        return True
     

def main():
    library_menu_options = ["Load Library", "Create library", "Exit"]
    library_menu = "\n".join([f"| {inx+1}. {opt}" for inx, opt in enumerate(library_menu_options)])
    print('\n')
    print("\n| ━━━━━━━━━━━━ Library Menu ━━━━━━━━━━━━ |\n")
    print(library_menu)
    print('\n')
    library_menu_choose = input(enter_choose)
    if library_menu_choose == "1":
        pass
    
    visual_menu = f'''{visual_space}\n| ━━━━━━━━━━━━ Creating library ━━━━━━━━━━━━ |\n\n'''
    
    if library_menu_choose == "2":
        if library_created == True:
            print(visual_space)
            print("Message: You can't create new library.\nReason: You already have a library.")
            main()
        print(visual_menu)
        try:
            library_name = input("Please enter a Library name: ")
            print(visual_menu)
            print('Library name:', library_name)
            library_address = Address.create_address()
            print(type(library_address))
            create_library = Library.create_library(library_name, library_address)
            if create_library == True:
                print("Good Job! You create a first library!")
                main()
                
        except Exception as e:
            print("Error, Try again")
            print(e)
            main()
    
    if library_menu_choose == "3":
        exit() # Note: Dont forget add a save system here!
     
     
        
if __name__ == "__main__":
    main()