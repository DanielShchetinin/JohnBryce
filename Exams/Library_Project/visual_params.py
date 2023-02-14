
# Global visual aspects

enter_choose = "| Enter a number from the list: "
visual_space = "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"


# Database menu visual aspects

database_menu_options = ["Load Library Database", "Create Library Database", "Delete Library Database", "Exit"]
database_menu = "\n".join([f"| {inx+1}. {opt}" for inx, opt in enumerate(database_menu_options)]) 

visual_database_menu = f'\n| ━━━━━━━━━━━━ Database Menu ━━━━━━━━━━━━ |\n\n'
visual_creating_database = f'{visual_space}\n| ━━━━━━━━━━━━ Creating Database ━━━━━━━━━━━━ |\n\n'
visual_database_menu_w_space = f'{visual_space}\n| ━━━━━━━━━━━━ Database Menu ━━━━━━━━━━━━ |\n\n'

# Library menu visual aspects

library_menu_options = ["Customer Menu", "Book Menu", "Loan Menu | NOT WORK", "Library Settings", "Save and Exit"]
library_menu = "\n".join([f"| {inx+1}. {opt}" for inx, opt in enumerate(library_menu_options)]) 

visual_library_menu = f'\n| ━━━━━━━━━━━━ Library Menu ━━━━━━━━━━━━ |\n\n'

library_settings_options = ["Display Library Information", "Change library Name", "Change library Address", "Save and Return"]
library_settings = "\n".join([f"| {inx+1}. {opt}" for inx, opt in enumerate(library_settings_options)]) 
visual_library_settings = f'\n| ━━━━━━━━━━━━ Library Settings ━━━━━━━━━━━━ |\n\n'

# Customers menu visual aspects

customer_menu_options = ["Add Customer", "Delete Customer", "Find Customer By ID", "Find Customer By Name", "Display all Customers", "Return to Library Menu"]
customer_menu = "\n".join([f"| {inx+1}. {opt}" for inx, opt in enumerate(customer_menu_options)]) 

visual_customer_menu = f'\n| ━━━━━━━━━━━━ Customer Menu ━━━━━━━━━━━━ |\n\n'
visual_creating_customer = f'{visual_space}\n| ━━━━━━━━━━━━ Creating Customer ━━━━━━━━━━━━ |\n\n'
visual_customers_list = f'{visual_space}\n| ━━━━━━━━━━━━ Customers list ━━━━━━━━━━━━ |\n\n'

customer_list_options = ["Open full information By ID", "Return to Customer Menu"]
customer_list = "\n".join([f"| {inx+1}. {opt}" for inx, opt in enumerate(customer_list_options)]) 

visual_customers_delete = f'{visual_space}\n| ━━━━━━━━━━━━ Delete Customers ━━━━━━━━━━━━ |\n\n'
visual_customers_full = f'{visual_space}\n| ━━━━━━━━━━━━ Full Information ━━━━━━━━━━━━ |\n\n'
visual_customers_name = f'{visual_space}\n| ━━━━━━━━━━━━ Search by Name ━━━━━━━━━━━━ |\n\n'

# Books menu visual aspects

books_menu_options = ["Add Book", "Delete Book", "Find Book By Name | NOT WORK", "Find Book By Author | NOT WORK", "Display all books ", "Return to Library Menu"]
books_menu = "\n".join([f"| {inx+1}. {opt}" for inx, opt in enumerate(books_menu_options)]) 

visual_book_menu = f'\n| ━━━━━━━━━━━━ Books Menu ━━━━━━━━━━━━ |\n\n'
visual_creating_book = f'{visual_space}\n| ━━━━━━━━━━━━ Creating Book ━━━━━━━━━━━━ |\n\n'
visual_books_list = f'{visual_space}\n| ━━━━━━━━━━━━ Books list ━━━━━━━━━━━━ |\n\n'
visual_books_delete = f'{visual_space}\n| ━━━━━━━━━━━━ Delete Books ━━━━━━━━━━━━ |\n\n'
visual_books_full = f'{visual_space}\n| ━━━━━━━━━━━━ Full Information ━━━━━━━━━━━━ |\n\n'

books_list_options = ["Open full information By ID", "Return to Book Menu"]
books_list_menu = "\n".join([f"| {inx+1}. {opt}" for inx, opt in enumerate(books_list_options)]) 


# Loan menu visual aspects
loan_menu_options = ["Make New Loan", "Return Loan", "Display loans history by customer ID", "Display loans history by book ID", "Display all active loans", "Display all loans history", "Return to Library Menu"]
loan_menu = "\n".join([f"| {inx+1}. {opt}" for inx, opt in enumerate(loan_menu_options)])

visual_loan_menu = f'\n| ━━━━━━━━━━━━ Loan Menu ━━━━━━━━━━━━ |\n\n'
visual_creating_loan = f'\n| ━━━━━━━━━━━━ Make Loan ━━━━━━━━━━━━ |\n\n'