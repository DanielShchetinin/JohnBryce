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
        
        self._account2customers: dict[int, set[Customer]] = {}
        self._customer2accounts: dict[int, set[BankAccount]] = {}
        
        
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
    
    def delete_branch(self, branch_id):
        if branch_id in self._branches:
            self._branches.pop(branch_id)
            return True
        else:
            return False
        
    
    def add_customer(self, customer_id: str, passport_id: str, name: str, surname: str, phone_number: str, address: Address, salary: int):
        if customer_id in self._customers:
            return False
        customer = Customer(customer_id, passport_id, name, surname, phone_number, address, salary)
        self._customers[customer_id] = customer
        return True    
    
    def create_account(self, account_id, branch_id, customer_ids: set[int]) -> bool:
        if account_id in self._accounts:
            return False

        account_holders = set()
        for customer_id in customer_ids:
            if customer_id not in self._customers:
                return False
            else:
                account_holders.add(self._customers[customer_id])

        account = BankAccount(account_id, branch_id)
        self._accounts[account_id] = account

        self._account2customers[account_id] = account_holders
        for customer_id in customer_ids:
            if customer_id not in self._customer2accounts:
                self._customer2accounts[customer_id] = set()
            self._customer2accounts[customer_id].add(account)

        return True
    
    
    
    
    
if __name__ == "__main__":
    bank = Bank("Leumi", Address("Israel", "Tel-Aviv", "Dizengoff", 51232, 5))
    
    bank.add_branch(1, "Ashkelon", Address("Israel", "Ashkelon", "Ort", 123456, 1))
    bank.add_branch(2, "Ashdod Yam", Address("Israel", "Ashdod", "Kineret", 123436, 2))
    bank.add_branch(3, "Ashdod City", Address("Israel", "Ashdod", "Dizengoff", 125456, 4))
    
    bank.add_customer(1, "213731102", "Daniel", "Shchetinin", "0537200511", Address("Israel", "Ashdod", "Kineret", 123456, 116), 7500)
    bank.add_customer(2, "213731103", "Vadim", "Shchetinin", "0537200512", Address("Israel", "Ashdod", "Kineret", 123456, 116), 7505)
    
    bank.create_account(1, 1, (1,2))
    
    
    
    # print(new_customer, new_customer.get_customer_salary())
    # new_customer.set_customer_salary(10000)
    # print(new_customer, new_customer.get_customer_salary())