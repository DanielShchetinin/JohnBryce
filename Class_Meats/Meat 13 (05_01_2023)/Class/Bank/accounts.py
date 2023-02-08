from customer import Customer

class BankAccount:
    
    def __init__(self, account_id, branch_id, customers: list[Customer]):
        self._account_id = account_id
        self._branch_id = branch_id
        self._owners = {}
        
        
    def get_account_id(self):
        return self._account_id
    
    def get_branch_id(self):
        return self.get_branch_id
    
    def set_branch_id(self, new_branch_id):
        self._branch_id = new_branch_id