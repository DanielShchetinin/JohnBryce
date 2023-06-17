from address import Address

class Customer:
    def __init__(self, customer_id: str, passport_id: str, name: str, surname: str, phone_number: str, address: Address, salary: int):
        self._customer_id = customer_id
        self._passport_id = passport_id
        self._name = name
        self._surname = surname
        self._phone_number = phone_number
        self._address = address
        self._salary = salary
        
    def get_customer_id(self):
        return self._customer_id
    
    def get_customer_passport(self):
        return self._passport_id
    
    def get_customer_fullname(self):
        return f"{self._name} {self._surname}"
    
    def get_customer_phone_number(self):
        return self._phone_number
    
    def get_customer_address(self):
        return self._address
    
    def get_customer_salary(self):
        return self._salary
    
    def set_customer_salary(self, new_salary):
        self._salary = new_salary    
    
    def __str__(self):
        return f"<Customer {self.get_customer_fullname()}, ID: {self.get_customer_id()}>"
