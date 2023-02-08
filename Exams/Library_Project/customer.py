import datetime
from address import Address


class Customer:
    
    def __init__(self, customer_id: int, customer_first_name: str, customer_last_name: str, address: Address, email: str, birth_date: datetime.date):
        
        self._customer_id = customer_id
        self._customer_first_name = customer_first_name
        self._customer_last_name = customer_last_name
        self._address: Address = address
        self._email = email
        self._birth_date: datetime = birth_date
        
    def get_customer_id(self):
        return self._customer_id
    
    def get_customer_full_name(self):
        return f"{self._customer_first_name} {self._customer_last_name}"

    def __str__(self):
        return f"Customer Name: {self._customer_first_name} {self._customer_last_name} with ID: {self._customer_id}."
    

if __name__ == "__main__":
    c1 = Customer(1, "Daniel", "Shchetinin", Address("Israel", "Ashdod", "Kineret", 123456, 116), "DanielShchetinin@gmail.com", datetime.date(year=2002, month=11, day=5))
    
    print(c1)