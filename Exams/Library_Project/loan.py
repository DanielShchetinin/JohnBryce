import datetime


class Loan:
    
    def __init__(self, customer_id: int, book_id: int, return_date: datetime.date, loan_date: datetime.date = datetime.date.today()):
        
        self.customer_id = customer_id
        self.book_id = book_id
        self.return_date = return_date
        self.loan_date = loan_date