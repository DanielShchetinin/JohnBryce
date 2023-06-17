from address import Address

class Branch:
    
    def __init__(self, branch_id: int, name: str, address: Address):
        self._branch_id = branch_id
        self._name = name
        self._address:Address = address
        
    def get_branch_id(self):
        return self._branch_id

    def get_branch_name(self):
        return self._name
    
    def get_branch_address(self) -> Address:
        return self._address
    
    def set_branch_address(self, new_address):
        self._address = new_address
        
    def __str__(self):
        return f"<Branch id: {self.get_branch_id()}, branch name: {self.get_branch_name()}>"
    
    def __repr__(self):
        return self.__str__()
        