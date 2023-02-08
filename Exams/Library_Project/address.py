class Address:

    
    def __init__(self, country: str, city: str, street: str, building_number: int):
        
        self._country = country
        self._city = city
        self._street = street
        self._building_number = building_number

        
    def get_city(self):
        return self._city
    
    def get_full_address(self):
        return f"\nCountry: {self._country}.\nCity: {self._city}.\nStreet: {self._street}.\
                \n\nbuilding_number: {self._building_number}.\n.\n"

    @staticmethod
    def create_address():
        country = input("Please Enter a country: ")
        city = input("Please Enter a city: ")
        street = input("Please Enter a street: ")
        building_number = int(input("Please Enter a buliding number: "))

        address_for_use = Address(country, city, street, building_number)
        return address_for_use
    
if __name__ == "__main__":
    library_address = Address.create_address()
    print(library_address.get_full_address())
    print(library_address)