from address import Address
from branch import Branch
from customer import Customer
from accounts import BankAccount

class Bank:
    
    def __init__(self, name: str, address: Address):
        self._name = name
        self._address = address
        self._branches: dict[int, Branch] = {}
        self._customers: dict[int, Customer] = {}
        self._accounts: dict[int, BankAccount] = {name}
        
        self
        
        
    def get_bank_name(self):
        return self._name
    
    def get_bank_address(self):
        return self._address
    
    # CRUD
    
    def add_branch(self, branch_id: int, name: str, address: Address) -> bool:
        if branch_id in self._branches:
            return False
        branch = Branch(branch_id, name, address)
        self._branches[branch_id] = branch
        return True
        
    def get_branch_by_id(self, branch_id) -> Branch:
        return self._branches.get(branch_id)
    
    def get_branches_by_city(self, city) -> list[Branch]:
        result = []
        for branch_id, branch in self._branches.items():
            if branch.get_branch_address().get_city() == city:
                result.append(branch)
        return result
    
    def update_branch_address(self, branch_id: int, address: Address) -> bool:
        branch = self._branches.get(branch_id)
        if not branch:
            return False
        branch.set_branch_address(address)
        return True        
    
    def add_account(self):
        pass
    
    
    
    
    
if __name__ == "__main__":
    bank = Bank("Leumi", Address("Israel", "Tel-Aviv", "Dizengoff", 51232, 5))
    
    bank.add_branch(1, "Ashkelon", Address("Israel", "Ashkelon", "Ort", 123456, 1))
    bank.add_branch(2, "Ashdod Yam", Address("Israel", "Ashdod", "Kineret", 123436, 2))
    bank.add_branch(3, "Ashdod City", Address("Israel", "Ashdod", "Dizengoff", 125456, 4))