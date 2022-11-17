# we get some inputs
Science_books = int(input("Enter how much Science fiction books you want buy: "))
Comics = int(input("Enter how much Comics you want buy: "))
History_books = int(input("Enter how much History books you want buy: "))

#Set a total discount 0 and calc the discounts
total_discount = 0
Comics_cost = Comics * 32

Science_cost = Science_books * 58
if Science_books >= 3:
    Science_cost = Science_books * 52.2
    dicount_science = (58 * Science_books) - Science_books
    total_discount = dicount_science
        
History_cost = History_books * 24

if History_books >= 2:
    free_book = History_books // 2
    History_books = History_books + free_book
    Comics_discount = free_book * 24 
    total_discount = total_discount + Comics_discount

#Check the book costs and finnaly discount
book_cost = Comics_cost + Science_cost + History_cost
if book_cost >= 300:
    book_discount = 20
    total_discount = total_discount + book_discount

#Prints and output any information.
print(f"\nYour order: \n\
Sci-fi books: {Science_books} and pay {round(Science_cost)}$\n\
Comics: {Comics} and pay {round(Comics_cost)}$\n\
History books: {History_books} and pay {round(History_cost)}$\n")

print(f"Total amount of books: {round(Science_books + Comics + History_books)}\
\nTotal cost before discount: {round(book_cost)}$")
if total_discount >= 1:
    print(f"Total discount: {round(total_discount)}$\
          \nTotal cost after discount: {round(book_cost - total_discount)}$\n")