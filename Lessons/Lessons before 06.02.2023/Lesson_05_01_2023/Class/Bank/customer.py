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