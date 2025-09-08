""" Welcome to my ATM 

This is a simplified version of the ATM program that avoids complicated
non-interactive handling and focuses on the basics.

Functions involved in my atm:
- Create account
- Login
- Balance inquiry
- Deposit
- Withdraw
- Exit

 NOTE : Data is stored in-memory (not saved to a file).
"""

accounts = {}


def create_account():
    print("\n--- Create Account ---")
    name = input("Enter your name: ").strip()
    pin = input("Set a 4-digit PIN: ").strip()
    if not (pin.isdigit() and len(pin) == 4):
        print("PIN must be 4 digits.")
        return
    acc_no = str(1000 + len(accounts) + 1)
    accounts[acc_no] = {"name": name, "pin": pin, "balance": 0.0}
    print(f"Account created successfully! Your account number: {acc_no}")


def login():
    print("\n--- Login ---")
    acc_no = input("Enter account number: ").strip()
    pin = input("Enter PIN: ").strip()
    if acc_no in accounts and accounts[acc_no]["pin"] == pin:
        print(f"Welcome {accounts[acc_no]['name']}!")
        account_menu(acc_no)
    else:
        print("Invalid account number or PIN.")


def account_menu(acc_no):
    while True:
        print("\n--- Account Menu ---")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Logout")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            print(f"Balance: ₹{accounts[acc_no]['balance']:.2f}")
        elif choice == "2":
            amt = float(input("Enter deposit amount: "))
            accounts[acc_no]["balance"] += amt
            print(f"Deposited ₹{amt:.2f}. New balance: ₹{accounts[acc_no]['balance']:.2f}")
        elif choice == "3":
            amt = float(input("Enter withdrawal amount: "))
            if amt <= accounts[acc_no]["balance"]:
                accounts[acc_no]["balance"] -= amt
                print(f"Withdrawn ₹{amt:.2f}. New balance: ₹{accounts[acc_no]['balance']:.2f}")
            else:
                print("Insufficient, please add more to your account.")
        elif choice == "4":
            print("Logging out...")
            break
        else:
            print("Invalid choice.")


def main():
    while True:
        print("\n=== Welcome to Keshav's ATM ===")
        print("1. Create Account")
        print("2. Login")
        print("3. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            create_account()
        elif choice == "2":
            login()
        elif choice == "3":
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
