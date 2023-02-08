class Address:
    
    def __init__(self, country: str, city: str, street: str, zip_code: int, building_number: int, entrance:int=None, floor:int=None):
        
        self._country = country
        self._city = city
        self._street = street
        self._zip_code = zip_code
        self._building_number = building_number
        self._entrance = entrance
        self._floor = floor
        
    def get_city(self):
        return self._city
    
    def get_full_address(self):
        return f"\nCountry: {self._country}.\nCity: {self._city}.\nStreet: {self._street}.\
                \n\nZip Code: {self._zip_code}.\nbuilding_number: {self._building_number}.\nEntrance: {self._entrance}.\nFloor: {self._floor}.\n"
