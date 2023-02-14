import time
import datetime
import os
import pickle
from visual_params import *
from exceptions import *
from address import Address
from book import Book
from customer import Customer
from loan import Loan

DB_URL = "Exams\\Library_Project\\library_database.pickle"

class Library:
    
    def __init__(self, library_name: str, library_address: Address):
        
        self._library_name = library_name
        self._library_address = library_address
        
        self._books: dict[int, Book] = {}
        self._customers: dict[int, Customer] = {}
        self._library: dict[str, Library] =  {}
    
    # Database Save System
    
    def save_library_to_dict(self, library):
        self._library["Library"] = library
        return True
    
    def save_to_picke(self, library):
        with open(DB_URL, "wb") as file:
            pickle.dump(library, file)
            file.close
            
    @staticmethod
    def load_from_pickle():
        with open(DB_URL, "rb") as file:
                library:Library = pickle.load(file)
                file.close
        return library            
    

    # Create func`s

    def add_customer(self, customer_id: int, customer_first_name: str, customer_last_name: str, address: Address, email: str, birth_date):
        if customer_id in self._customers:
            return False
        customer = Customer(customer_id, customer_first_name, customer_last_name, address, email, birth_date)
        self._customers[customer_id] = customer
        return True
    
    def add_book(self, book_id: int, book_name: str, book_autor: str, published_year: int, book_type: int = 3):
        if book_id in self._books:
            return False
        self._books[book_id] = Book(book_id, book_name, book_autor, published_year, book_type)
        return True
    
    def create_loan(self, customer_id: int, book_id: int, loan_date: datetime, return_date: datetime)
    # Read func`s
    
    def get_library(self): 
        return self._library["Library"]
    
    def get_library_name(self):
        return self._library_name
    
    def get_library_address(self):
        return self._library_address
    
    def get_library_full_information(self):
        print("Library Name:", self._library_name)
        print("Library Address:", self._library_address)
        return True
    
    def get_customer_by_id(self, customer_id):
        return self._customers.get(customer_id)
    
    def get_customers_dict(self):
        return self._customers
    
    def get_book_dict(self):
        return self._books
    
    def get_customer_full_info(self, customer_id):
        print("Customer ID:", customer_id)
        print("Full Name:", self._customers[customer_id].get_customer_full_name())
        print("Email:", self._customers[customer_id].get_customer_email())
        print("Full Address:", self._customers[customer_id].get_customer_address())
        print("Age:", self._customers[customer_id].get_customer_age())
        
    def get_book_full_info(self, book_id):
        print("Book ID:", book_id)
        print("Book Name:", self._books[book_id].get_book_name())
        print("Book Author:", self._books[book_id].get_book_author())
        print("Book Publish Year:", self._books[book_id].get_book_publish_year())
        print("Book Type:", self._books[book_id].get_book_type())
        
    def get_customer_by_name(self, name) -> list[Customer]:
        result = []
        for customer_id, customer in self._customers.items():
            if customer._customer_first_name == name:
                result.append(customer)
        return result
    
    def get_book_by_id(self, book_id):
        return self._books.get(book_id)
    
    def get_book_by_name(self, author_name) -> list[Book]:
        result = []
        for book_id, book in self._books.items():
            if book.get_book_author == author_name:
                result.append(book)
        return result
    
    # Update func`s
    
    def update_library_name(self, new_name):
        self._library_name = new_name
        return True
    
    def update_library_address(self, address:Address):
        self._library_address = address
        return True
    
    # Delete func`s
    
    def delete_customer(self, customer_id):
        if customer_id in self._customers:
            self._customers.pop(customer_id)
            return True
        else:
            return False
    
    def delete_book(self, book_id):
        if book_id in self._books:
            self._books.pop(book_id)
            return True
        else:
            return False
    
    # __str__ and __repr__
    
    def __str__(self):
        return f"Library name: {self.get_library_name()}, Address: {self.get_library_address()}"
    
    def __repr__(self):
        return self.__str__()
     
# Main and Database system

def main():
    print(visual_database_menu)
    print(database_menu)
    print('\n')
    database_menu_choose = input(enter_choose)
    
    try:
        if not database_menu_choose.isdigit():
            print(visual_space)
            print("You cant use digits, Only numbers!")
            main()
            
        if database_menu_choose not in ["1", "2", "3", "4"]:
            print(visual_space)
            print("You can use only displayed options")
            main()
            
    except Exception as error_message:
        print(error_message)
        main()
        
    if database_menu_choose == "1":
        
        try:
        
            if not os.path.isfile(DB_URL):
                print(visual_space)
                print("Library database is not found, Please create new one.")
                main()
            else:
            
            
                with open(DB_URL, "rb") as file:
                    library:Library = pickle.load(file)
                    file.close
                    print(visual_space)
                    print(f"| Welcome to {library.get_library_name()}")
                    goto_library_menu()
                
        except Exception as error_message:
                print(visual_space)
                print("| Database load failed.")
                print("Reason: Unexpected error occurred")
                print("System:", error_message) # Need to remove 
                main()
    
    if database_menu_choose == "2":
        
        try:
        
            if os.path.isfile(DB_URL):
                print(visual_space)
                print("You can't create new library when you have one!")
                main()
            
            
            print(visual_creating_database)
            library_name = input("| Please enter a Library Name: ")
            print(visual_creating_database)
            print("| Choosed Library name:", library_name, "\n")
            library_creation_address = Address.create_address_for_library()
            print(visual_creating_database)
            print(f"| Choosed Library name: {library_name}")
            print(f"| Choosed Library Address: {library_creation_address}")
            print("\nCreating database...")
            time.sleep(2)
            print(visual_space)
            library = Library(library_name, library_creation_address)
            created = library.save_library_to_dict(library)
            library.save_to_picke(library)
            if created == True:
                print("| The Library Database file is been created")
                print(f"\n| Library information: {library}")
                main()
                
        except Exception as error_message:
            print(visual_space)
            print("Library creation failed.")
            print("Reason: Unexpected error occurred")
            print("System:", error_message) # Need to remove 
            main()
            
    if database_menu_choose == "3":
        
        try:
        
            if os.path.isfile(DB_URL):
                os.unlink(DB_URL)
                print(visual_space)
                print("The Library Database file is been deleted")
                main()
            else:
                print(visual_space)
                print("File not found.")
                main()
            
        except Exception as error_message:
            print(visual_space)
            print("Library delete failed.")
            print("Reason: Unexpected error occurred")
            print("System:", error_message) # Need to remove 
            main()
    
    if database_menu_choose == "4":
        
        try:
            if os.path.isfile(DB_URL):
                print(visual_space)
                print("Saving library database...")
                library:Library.save_to_picke()
                time.sleep(2)
                print(visual_space)
                print("The data is been saved. Bye!\n")
            else: 
                print("Bye!")
            exit() # Note: Dont forget add a save system here!
            
        except Exception as error_message:
            print(error_message)
            main()
        
        
# Library Menu
def goto_library_menu():
    print(visual_library_menu)
    print(library_menu)
    print('\n')
    library_menu_choose = input(enter_choose)
    try:
        if not library_menu_choose.isdigit():
            print(visual_space)
            print("You cant use digits, Only numbers!")
            goto_library_menu()
            
        if library_menu_choose not in ["1", "2", "3", "4", "5"]:
            print(visual_space)
            print("You can use only displayed options")
            goto_library_menu()
            
    except Exception as error_message:
        print(error_message)
        goto_library_menu()
        
    if library_menu_choose == "1":
        print(visual_space)
        goto_customer_menu()
        
    if library_menu_choose == "2":
        print(visual_space)
        goto_book_menu()
        
    if library_menu_choose == "3":
        print(visual_space)
        goto_loan_menu()
        
    if library_menu_choose == "4":
        try:
            with open(DB_URL, "rb") as file:
                library:Library = pickle.load(file)
                file.close
                
                print(visual_space)
                print(visual_library_settings)
                print(library_settings)
                print('\n')
                settings_menu_choose = input(enter_choose)
                if not settings_menu_choose.isdigit():
                    print(visual_space)
                    print("You cant use digits, Only numbers!")
                    goto_library_menu()
                
                if settings_menu_choose not in ["1", "2", "3", "4"] :
                    print(visual_space)
                    print("You can use only displayed options")
                    goto_library_menu()
                
                if settings_menu_choose == "1":
                    print(visual_space)
                    print(visual_library_settings)
                    library.get_library_full_information()
                    return_menu = input("\n| Enter [1] to return to the customer menu: ")
                    if not return_menu.isdigit():
                        print(visual_space)
                        print("Error")
                        goto_library_menu()
                    if return_menu == "1":
                        print(visual_space)
                        goto_library_menu()       
                        
        except Exception as error_message:
            print(error_message)
            goto_library_menu()    
            
        if settings_menu_choose == "2":
            try:
                with open(DB_URL, "rb") as file:
                    library:Library = pickle.load(file)
                    file.close

                print(visual_space)
                print(visual_library_settings)
                new_name = input("| Enter a new name for Library or Press [ENTER] for return: ")
                if new_name == "" or new_name == " ":
                    print(visual_space)
                    goto_library_menu()
                change = library.get_library().update_library_name(new_name)

                if change == True:
                    library.save_to_picke(library)
                    print(visual_space)
                    print(f"Library name changed Successful to: {new_name}")
                    goto_library_menu()
                else:
                    print(visual_space)
                    print("Error")
                    goto_library_menu()
                    
            except Exception as error_message:
                print(error_message)
                goto_library_menu()
                
        if settings_menu_choose == "3":
            try:
                with open(DB_URL, "rb") as file:
                    library:Library = pickle.load(file)
                    file.close

                print(visual_space)
                print(visual_library_settings)
                new_address = Address.create_address_for_library()
                if new_address == "" or new_address == " ":
                    print(visual_space)
                    goto_library_menu()
                change = library.get_library().update_library_address(new_address)

                if change == True:
                    library.save_to_picke(library)
                    print(visual_space)
                    print(f"Library address changed Successful to: \n{new_address}")
                    goto_library_menu()
                else:
                    print(visual_space)
                    print("Error")
                    goto_library_menu()
                    
            except Exception as error_message:
                print(error_message)
                goto_library_menu()


        if settings_menu_choose == "4":
            print(visual_space) 
            goto_library_menu()
        
        
        
    if library_menu_choose == "5":
        try:
            if os.path.isfile(DB_URL):
                print(visual_space)
                print("Saving library database...")
                library:Library.save_to_picke()
                time.sleep(2)
                print(visual_space)
                print("The data is been saved. Bye!\n")
            else: 
                print("Bye!")
            exit() # Note: Dont forget add a save system here!
            
        except Exception as error_message:
            print(error_message)
            main()
    
    
    # Customer Menu
def goto_customer_menu():
    print(visual_customer_menu)
    print(customer_menu)
    print('\n')
    customer_menu_choose = input(enter_choose)
    try:
        if not customer_menu_choose.isdigit():
            print(visual_space)
            print("You cant use digits, Only numbers!")
            goto_customer_menu()
            
        if customer_menu_choose not in ["1", "2", "3", "4", "5", "6"]:
            print(visual_space)
            print("You can use only displayed options")
            goto_customer_menu()
            
    except Exception as error_message:
        print(error_message)
        goto_customer_menu()
        
    if customer_menu_choose == "1":
        try:
            
            library = Library.load_from_pickle()

            print(visual_creating_customer)
            id_of_customer = input("| Please enter ID of Customer: ")
            if not id_of_customer.isdigit():
                print(visual_space)
                print("Error")
                goto_customer_menu()
            id_of_customer = int(id_of_customer)
            customers_list = library.get_customers_dict()
            if id_of_customer in customers_list:
                print(visual_space)
                print("Error, This ID is used.")
                goto_customer_menu()
            first_name_of_customer = input("| Please enter First Name of Customer: ")
            last_name_of_customer = input("| Please enter Last Name of Customer: ")
            email_of_customer = input("| Please enter Email for Customer: ")
            print(visual_creating_customer)
            print(f"| Customer ID: {id_of_customer}")
            print(f"| Customer Full Name: {first_name_of_customer} {last_name_of_customer}")
            print(f"| Customer E-mail: {email_of_customer}\n")
            
            birthdate_of_customer = input("\n| In next format: dd.mm.yyyy.\n| Please enter Birthdate of Customer: ")
            birthdate_of_customer_datetime = datetime.datetime.strptime(birthdate_of_customer, "%d.%m.%Y")
            visualdate = datetime.date.strftime(birthdate_of_customer_datetime, "%d.%m.%Y")
            print(visual_creating_customer)
            print(f"| Customer ID: {id_of_customer}")
            print(f"| Customer Full Name: {first_name_of_customer} {last_name_of_customer}")
            print(f"| Customer E-mail: {email_of_customer}")
            print(f"| Customer Birthdate: {visualdate}\n")
            
            print("\n| Make a Address of Customer: ")
            address_of_customer = Address.create_address_for_customer()
            
            print(visual_creating_customer)
            print(f"| Customer ID: {id_of_customer}")
            print(f"| Customer Full Name: {first_name_of_customer} {last_name_of_customer}")
            print(f"| Customer E-mail: {email_of_customer}")
            print(f"| Customer Birthdate: {visualdate}")
            print(f"| Customer Address: {address_of_customer}\n\n")
            print("Creating Customer Account...")
            time.sleep(2)            
            library.add_customer(id_of_customer, first_name_of_customer, last_name_of_customer, address_of_customer, email_of_customer, birthdate_of_customer)
            print(visual_space)
            print("Successful, New Customer account is been created!")
            library.save_to_picke(library)
            goto_customer_menu()
            
            
        except Exception as error_message:
            print(error_message)
            goto_customer_menu()


    if customer_menu_choose == "2":
        try:
             
            with open(DB_URL, "rb") as file:
                library:Library = pickle.load(file)
                file.close
            customers_list = library.get_customers_dict()
            if len(customers_list) == 0:
                print(visual_space)
                print("No Customers to delete!")
                goto_customer_menu()
            print(visual_space)
            print(visual_customers_delete)
            customer:Customer = library.get_customers_dict()
            for key in customer:
                print(customer[key])
            customer_id = input("\n| Enter ID to delete account: ")
            if not customer_id.isdigit():
                print(visual_space)
                print("Error")
                goto_customer_menu()
            customer_id = int(customer_id)
            customer_deleted = library.delete_customer(customer_id)
            if customer_deleted == True:
                print(visual_space)
                print("Account Deleted!")
                library.save_to_picke(library)
                goto_customer_menu()
            else:
                print(visual_space)
                print("Customer not exist!")
                goto_customer_menu()
        
        except Exception as error_message:
            print(error_message)
            goto_customer_menu()
            
    if customer_menu_choose == "3":
        try:
        
            library = Library.load_from_pickle()
            customers_list = library.get_customers_dict()
            if len(customers_list) == 0:
                print(visual_space)
                print("No Customers for display!")
                goto_customer_menu()
            print(visual_space)
            print(visual_customers_full)
            customer_id = input("| Enter ID to get information about Customer: ")
            if not customer_id.isdigit():
                print(visual_space)
                print("Error")
                goto_customer_menu()
            customer_id = int(customer_id)
            if customer_id not in customers_list:
                print(visual_space)
                print("Error, ID not exist.")
                goto_customer_menu()
            print(visual_space)
            print(visual_customers_full)
            library.get_customer_full_info(customer_id)
            return_menu = input("\n| Enter [1] to return to the customer menu: ")
            if not return_menu.isdigit():
                print(visual_space)
                print("Error")
                goto_customer_menu()
            if return_menu == "1":
                print(visual_space)
                goto_customer_menu()
                
        except Exception as error_message:
            print(error_message)
            goto_customer_menu()
            
    if customer_menu_choose == "4":
        try:
            
            with open(DB_URL, "rb") as file:
                library:Library = pickle.load(file)
                file.close
            customers_list = library.get_customers_dict()
            if len(customers_list) == 0:
                print(visual_space)
                print("No Customers for display!")
                goto_customer_menu()
            print(visual_space)
            print(visual_customers_name)
            customer_name = input("| Enter name to search customers with choosed name: ").title()
            result = library.get_customer_by_name(customer_name)
            print(visual_space)
            print(visual_customers_name)
            for i in result:
                print(i)
            return_menu = input("\n| Enter [1] to return to the customer menu: ")
            if not return_menu.isdigit():
                print(visual_space)
                print("Error")
                goto_customer_menu()
            if return_menu == "1":
                print(visual_space)
                goto_customer_menu()
            
        except Exception as error_message:
            print(error_message)
            goto_customer_menu()   
            
            
    if customer_menu_choose == "5":
        try:
        
            with open(DB_URL, "rb") as file:
                library:Library = pickle.load(file)
                file.close
            customers_list = library.get_customers_dict()
            if len(customers_list) == 0:
                print(visual_space)
                print("No Customers for display!")
                goto_customer_menu()
            print(visual_space)
            print(visual_customers_list)
            customer:Customer = library.get_customers_dict()
            for key in customer:
                print(customer[key])
            print("\n")
            print(customer_list, "\n")
            customer_list_choose = input(enter_choose)
            if not customer_list_choose.isdigit():
                print(visual_space)
                print("You cant use digits, Only numbers!")
                goto_customer_menu()
            
            if customer_list_choose not in ["1", "2"]:
                print(visual_space)
                print("You can use only displayed options")
                goto_customer_menu()
                
            if customer_list_choose == "1":
                print(visual_space)
                print(visual_customers_full)
                customer_id = input("| Enter ID to get information about Customer: ")
                if not customer_id.isdigit():
                    print(visual_space)
                    print("Error")
                    goto_customer_menu()
                customer_id = int(customer_id)
                if customer_id not in customers_list:
                    print(visual_space)
                    print("Error, ID not exist.")
                    goto_customer_menu()
                print(visual_space)
                print(visual_customers_full)
                library.get_customer_full_info(customer_id)
                return_menu = input("\n| Enter [1] to return to the customer menu: ")
                if not return_menu.isdigit():
                    print(visual_space)
                    print("Error")
                    goto_customer_menu()
                if return_menu == "1":
                    print(visual_space)
                    goto_customer_menu()
                
            if customer_list_choose == "2":
                print(visual_space)
                goto_customer_menu()
                
        except Exception as error_message:
            print(error_message)
            goto_customer_menu()

    if customer_menu_choose == "6":
        print(visual_space)
        goto_library_menu()
   
def goto_book_menu():
    print(visual_book_menu)
    print(books_menu)
    print('\n')
    books_menu_choose = input(enter_choose)     
   
    try:
        if not books_menu_choose.isdigit():
            print(visual_space)
            print("You cant use digits, Only numbers!")
            goto_book_menu()
            
        if books_menu_choose not in ["1", "2", "3", "4", "5", "6"]:
            print(visual_space)
            print("You can use only displayed options")
            goto_book_menu()
            
    except Exception as error_message:
        print(error_message)
        goto_book_menu()    
            
    if books_menu_choose == "1":
        try:
            
            with open(DB_URL, "rb") as file:
                library:Library = pickle.load(file)
                file.close
        
            print(visual_creating_book)
            id_of_book = input("| Please enter ID of Book: ")
            if not id_of_book.isdigit():
                print(visual_space)
                print("Error")
                goto_book_menu()
            id_of_book = int(id_of_book)
            book_list = library.get_book_dict()
            if id_of_book in book_list:
                print(visual_space)
                print("Error, This ID is used.")
                goto_book_menu()
            name_of_book = input("| Please enter Name of Book: ")
            author_name_of_book = input("| Please enter Author name of Book: ")
            publish_year_of_book = input("| Please enter the publish year of the book: ")
            print(visual_creating_book)
            print(f"| Book ID: {id_of_book}")
            print(f"| Book Name: {name_of_book}")
            print(f"| Book Autor: {author_name_of_book}")
            print(f"| Book Publish Year: {publish_year_of_book}\n")
            
            book_type_of_book = input("\n| Book Types:\n| The book type defines the maximum loan time for the book:\
                              \n| Type 1 – up to 10 days.\n| Type 2 – up to 5 days.\n| Type 3 – up to 2 day.\n\n| Enter book type for the book: ")
            print(visual_creating_book)
            print(f"| Book ID: {id_of_book}")
            print(f"| Book Name: {name_of_book}")
            print(f"| Book Autor: {author_name_of_book}")
            print(f"| Book Publish Year: {publish_year_of_book}")
            print(f"| Book Type: {book_type_of_book}\n")

            print("Creating new book...")
            time.sleep(3)            
            library.add_book(id_of_book, name_of_book, author_name_of_book, publish_year_of_book, book_type_of_book)
            print(visual_space)
            print("Successful, New book is been created!")
            library.save_to_picke(library)
            goto_book_menu()    
            
        except Exception as error_message:
            print(error_message)
            goto_book_menu()
    
    if books_menu_choose == "2":
        try:
             
            with open(DB_URL, "rb") as file:
                library:Library = pickle.load(file)
                file.close
            book_list = library.get_book_dict()
            if len(book_list) == 0:
                print(visual_space)
                print("No books to delete!")
                goto_book_menu()
            print(visual_space)
            print(visual_books_delete)
            book:Book = library.get_book_dict()
            for key in book:
                print(book[key])
            book_id = input("\n| Enter book ID to delete: ")
            if not book_id.isdigit():
                print(visual_space)
                print("Error")
                goto_book_menu()
            book_id = int(book_id)
            customer_deleted = library.delete_customer(book_id)
            if customer_deleted == True:
                print(visual_space)
                print("Book Deleted!")
                library.save_to_picke(library)
                goto_book_menu()
            else:
                print(visual_space)
                print("Book not exist!")
                goto_book_menu()
        
        except Exception as error_message:
            print(error_message)
            goto_book_menu()    
        
    if books_menu_choose == "3":
        try:
        
            library = Library.load_from_pickle()
            books_list = library.get_book_dict()
            if len(books_list) == 0:
                print(visual_space)
                print("No Books for display!")
                goto_customer_menu()
            print(visual_space)
            print(visual_books_full)
            book_id = input("| Enter ID to get information about the book: ")
            if not book_id.isdigit():
                print(visual_space)
                print("Error")
                goto_customer_menu()
            book_id = int(book_id)
            if book_id not in books_list:
                print(visual_space)
                print("Error, ID not exist.")
                goto_customer_menu()
            print(visual_space)
            print(visual_books_full)
            library.get_book_full_info(book_id)
            return_menu = input("\n| Enter [1] to return to the customer menu: ")
            if not return_menu.isdigit():
                print(visual_space)
                print("Error")
                goto_customer_menu()
            if return_menu == "1":
                print(visual_space)
                goto_customer_menu()
                
        except Exception as error_message:
            print(error_message)
            goto_customer_menu()
    
    if books_menu_choose == "4":
        pass 
        
    if books_menu_choose == "5":
        try:
        
            with open(DB_URL, "rb") as file:
                library:Library = pickle.load(file)
                file.close
            book_list = library.get_book_dict()
            if len(book_list) == 0:
                print(visual_space)
                print("No Books for display!")
                goto_book_menu()
            print(visual_space)
            print(visual_books_list)
            book:Book = library.get_book_dict()
            for key in book:
                print(book[key])
            print("\n")
            print(books_list_menu, "\n")
            books_list_choose = input(enter_choose)
            if not books_list_choose.isdigit():
                print(visual_space)
                print("You cant use digits, Only numbers!")
                goto_book_menu()
            
            if books_list_choose not in ["1", "2"]:
                print(visual_space)
                print("You can use only displayed options")
                goto_book_menu()
                
            if books_list_choose == "1":
                print(visual_space)
                print(visual_books_full)
                book_id = input("| Enter ID to get information about the Book: ")
                if not book_id.isdigit():
                    print(visual_space)
                    print("Error")
                    goto_book_menu()
                book_id = int(book_id)
                if book_id not in book_list:
                    print(visual_space)
                    print("Error, ID not exist.")
                    goto_book_menu()
                print(visual_space)
                print(visual_books_full)
                library.get_book_full_info(book_id)
                return_menu = input("\n| Enter [1] to return to the books menu: ")
                if not return_menu.isdigit():
                    print(visual_space)
                    print("Error")
                    goto_book_menu()
                if return_menu == "1":
                    print(visual_space)
                    goto_book_menu()
                    
            if books_list_choose == "2":
                print(visual_space)
                goto_book_menu()           
        
        except Exception as error_message:
            print(error_message)
            goto_book_menu()
            
    if books_menu_choose == "6":
        print(visual_space)
        goto_library_menu()
        
def goto_loan_menu():
    print(visual_loan_menu)
    print(loan_menu)
    print('\n')
    loan_menu_choose = input(enter_choose)
    
    try:
        if not loan_menu_choose.isdigit():
            print(visual_space)
            print("You cant use digits, Only numbers!")
            goto_loan_menu()
            
        if loan_menu_choose not in ["1", "2", "3", "4", "5", "6", "7"]:
            print(visual_space)
            print("You can use only displayed options")
            goto_loan_menu()
            
    except Exception as error_message:
        print(error_message)
        goto_loan_menu()    
            
    if loan_menu_choose == "1":
        try:
            
            library = Library.load_from_pickle()
            print(visual_space)
            print(visual_creating_loan)
            
            customer_id = input("| Please enter Customer ID: ")
            customer = library.get_customer_by_id(int(customer_id))
            print(visual_space)
            print(visual_creating_loan)
            print(f"| Choosed Customer:", customer.get_customer_half_info(),"\n")
            book_id = input("| Please enter Book ID: ")
            book = library.get_book_by_id(int(book_id))
            print(visual_space)
            print(visual_creating_loan)
            print(f"| Choosed Customer:", customer.get_customer_half_info())
            print(f"| Choosed Book:", book.get_book_info())
            loan_date = datetime.date.today()
            print(f"| Loan Date:", datetime.date.strftime(loan_date, "%d.%m.%Y"))
            return_date = None
            if book.get_book_type() == "1":
                return_date = loan_date + datetime.timedelta(days=10)
            if book.get_book_type() == "2":
                return_date = loan_date + datetime.timedelta(days=5)
            if book.get_book_type() == "3":
                return_date = loan_date + datetime.timedelta(days=2)
            print(f"| Return Date:", datetime.date.strftime(return_date, "%d.%m.%Y"))
            make_loan_choose = input(f"\n| Make new loan? [Y/N]: ")
            if make_loan_choose == "N" or make_loan_choose == "n":
                print(visual_space)
                print("Loan Making is been canceled")
                goto_loan_menu()
            else:
                loan = Loan(customer_id, book_id, return_date, loan_date)
                loan.loan_book(customer_id, book_id)
                loanlist = loan.get_loan_list()
                print(loanlist[0])
                
        except Exception as error_message:
            print(error_message)
            goto_loan_menu()    
            
            
if __name__ == "__main__":
    print(visual_space)
    main()