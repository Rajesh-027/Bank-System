from Account import BankAccount 
from Bank import Bank

def main():
    bank = Bank()
    
    while True:
        print("----------Welcome to your Bank---------")
        print("\n1. Create Account", "2. Login", "3. Exit  \n", sep = "\n")

        try:
            choice = int(input("What you want to do:"))
        except ValueError:
            print("Please enter a valid number!\n")
            continue

        match choice:
            case 1: 
                bank.create_account()
                
            case 2: 
                try:
                    acc = bank.login()
                    if acc:
                        account_menu(acc, bank)
                except ValueError as e:
                    print(e)
                    
            case 3: 
                print("Thank you for using our bank!")
                break
                
            case _:
                print("Invalid Choice\n")


def account_menu(acc, bank):
    print(f"----------Welcome Back, {acc.name}---------")
    while True:
        print("1. Deposit", "2. Withdraw", "3. Balance", "4. Transaction History", "5. Account Details", "6. Logout","7. Delete \n", sep = "\n")

        try:
            choice = int(input("What you want to do:"))
        except ValueError:
            print("Please enter a valid number! \n")
            continue

        match (choice):
            case 1: 
                try:
                    amount = int(input("Enter amount: "))
                    acc.deposit(amount)
                    bank.save_data()
                except ValueError as e:
                    print(e)
            case 2: 
                try: 
                    amount = int(input("Enter amount: "))
                    acc.withdraw(amount)
                    bank.save_data()
                except ValueError as e:
                    print(e)
                    
            case 3: 
                print(f"Your current Balance: {acc.get_balance()}\n")
                
            case 4: 
                history  = acc.get_history()
                for t in history:
                    print(f"{t['date']} | {t['type']} | ₹{t['amount']} | {t['status']}")
                    
            case 5: 
                print(acc)
                
            case 6: 
                print("Logged out successfully!\n")
                break

            case 7: 
                bank.delete_account(acc.acc_no)
                break
                
            case _:
                print("Invalid Choice\n")


if __name__ == "__main__":
    main()
