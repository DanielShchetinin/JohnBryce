import datetime


class Loan:
    
    def __init__(self, customer_id: int, book_id: int, return_date: datetime.date, loan_date: datetime = datetime.datetime.today()):
        
        self.customer_id = customer_id
        self.book_id = book_id
        self.return_date = return_date
        self.loan_date = loan_date
        
    def get_loan_list(self):
        return self.loan_list
    
    def loan_info(self):
        return f"Customer ID: {self.customer_id}, Book ID: {self.book_id}, Loaned: {self.loan_date}, Return: {self.return_date}"