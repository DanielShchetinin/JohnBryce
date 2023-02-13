import datetime


class Loan:
    
    def __init__(self, customer_id: int, book_id: int, return_date: datetime.date, loan_date: datetime = datetime.datetime.today()):
        
        self.customer_id = customer_id
        self.book_id = book_id
        self.return_date = return_date
        self.loan_date = loan_date
        
        self.loan_list: dict [int, list] = {}
        
    def loan_book(self, customer_id, book_id):
        if book_id in self.loan_list.items():
            return False
        if customer_id in self.loan_list.keys():
            self.loan_list[customer_id].append(book_id)
        