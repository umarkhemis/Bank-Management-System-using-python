import pwinput
import subprocess
import emoji

class BankAccount:
    def __init__(self, account_number):
        self.account_number = account_number
        self.balance = 500
        self.logged_in = False  # Flag to track login status

    def get_account_number(self):
        return self.account_number

    def get_balance(self):
        return self.balance

    def deposit(self, amount):
        while(True):
            if amount >= 500:
                self.balance += amount
                print(f"Thank you for depositing {amount}shs!!")
                break
            else:
                print("Sorry!! Can't deposit amount less than 500shs!!!!",emoji.emojize(":pensive_face:", language="alias"))
                break

    def withdraw(self, amount):
        while(True):
            if amount < self.balance and amount >= 500:
                self.balance -= amount
                print(f"You successfully withrawn {amount}shs!!")
                break
            else:
                print("Sorry, You Have Insufficient balance!!!", emoji.emojize(":pensive_face:"":pensive_face:", language="alias"))
                break
def main():
    account1 = None  # Initialize account outside the loop
    while True:
        if account1 is None or not account1.logged_in:
            print("1. Log In")
            print("*. Exit")
        else:
            print("1. Logged In Successfully", emoji.emojize(":thumbsup:", language='alias'))  # Show different message if logged in
            print("2. Deposit Cash")
            print("3. Withdraw Cash")
            print("4. Log Out")  # New option for logout
        choice = input("Enter your option: ")
        print("")

        if choice == '1':
            if account1 is None or not account1.logged_in:
                username = input("Enter Username: ").capitalize()
                password = pwinput.pwinput(prompt="Enter Password: ", mask="*")
                account_number = pwinput.pwinput(prompt="Enter Your Account_Number: ", mask="*")

                account1 = BankAccount(account_number)
                account1.logged_in = True  # Set login flag
                print("")
                print("........................")
                print("Congratulations!!! Here are your Account Details.....")
                print(f"Account Name: {username.capitalize()}")
                print(f"Account Number: {account1.get_account_number()}")
                print(f"Initial Balance: {account1.get_balance()}")
                print("\nMake Transactions Now!!!!!!\n")
            else:
                print("You are already logged in.\n")
        elif choice == "*":
            print("Exiting................")
            subprocess.run(["cowsay", "-t", emoji.emojize("Good Bye::wave::wave:", language='alias')])  # Use cowsay to say goodbye
            break

        elif choice == '2':
            if account1 is None or not account1.logged_in:
                print("Please log in first......\n")
            else:
                deposit_amount = int(input("Deposit Here: "))
                account1.deposit(deposit_amount)
                print(f"Current Balance: {account1.get_balance()}\n")

        elif choice == '3':
            if account1 is None or not account1.logged_in:
                print("Please log in first......\n")
            else:
                withdraw_amount = int(input("Withdraw Here: "))
                account1.withdraw(withdraw_amount)
                print(f"Current Balance: {account1.get_balance()}\n")


        elif choice == '4':  # Handle logout
            if account1 is not None and account1.logged_in:
                account1.logged_in = False
                print("Logged out successfully.\n")
            else:
                print("You are not logged in.\n")

        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()