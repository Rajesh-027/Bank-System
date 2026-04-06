import json

class Bank:

    def __init__(self):
        self.accounts = {}
        self.load_data()

        
    def create_account(self):
        name = input("Enter your full Name :")
        password = input("Enter a password :")
        
        while True:
            try:
                balance = int(input("Enter initial deposit (minimum 1000) : "))
                if balance < 1000:
                    raise ValueError(f"Initial deposit should be minimum ₹1000.\n")
                break
            except ValueError as e:
                print(e)
                print("Please try again!\n")
                
        acc = BankAccount(name, password, balance)

        self.accounts[acc.acc_no] = acc
        self.save_data()

        print("\nYour account is successfully created.\n")
        print(acc)

    
    def save_data(self):
        data = {}
        for acc_no, acc in self.accounts.items():
            data[acc_no] = {
                "name": acc.name,
                "password": acc.get_password(),
                "balance": acc.get_balance(),
                "transactions": acc.transactions
            }

        with open('data/accounts.json', 'w') as f:
            json.dump(data, f)

    
    def load_data(self):
        try: 
            with open('data/accounts.json', 'r') as f:
                content = f.read()
                if not content:             # check if empty
                    return  
                    
                data = json.loads(content)
                
                for acc_no, acc_data in data.items():
                    acc = BankAccount(
                        acc_data["name"],
                        acc_data["password"],
                        acc_data["balance"]
                    )
                    acc.acc_no = acc_no 
                    acc.transactions = acc_data["transactions"]
                    self.accounts[acc_no] = acc
                    
                if self.accounts:
                    last = max(self.accounts.keys())
                    BankAccount._account_counter = int(last)
        except FileNotFoundError:
            pass

    
    def login(self):
        acc_no = input("Enter Account Number:")
        
        if acc_no in self.accounts.keys():
            password = input("Enter Password")
            
            if self.accounts[acc_no].verify_password(password):
                print("Login successful! Welcome", self.accounts[acc_no].name)
                return self.accounts[acc_no]
            else:
                raise ValueError("Incorrect Password\n")
        else:
            raise ValueError("Account number is not found!\n")

    
    def delete_account(self, acc_no):
        password = input("Enter Password")
        
        if self.accounts[acc_no].verify_password(password):
            confirm = input("Are you sure? (yes/no):")
            
            if confirm.lower() == "yes":
                del self.accounts[acc_no]
                self.save_data()
                print("Your account is deleted successfully\n")
            else:
                print("Deletion cancelled!\n")
        else:
            raise ValueError("Incorrect Password\n")