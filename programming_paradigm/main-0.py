# main-0.py

import sys
from bank_account import BankAccount

def main():
    # Initialize a BankAccount object with an initial balance (e.g., 100)
    account = BankAccount(100)  # Example starting balance
    
    # Check if there are enough command line arguments
    if len(sys.argv) < 2:
        print("Usage: python main-0.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    # Extract command and amount from command line arguments
    command, *params = sys.argv[1].split(':')
    amount = float(params[0]) if params else None

    # Execute commands based on the command line input
    if command == "deposit" and amount is not None:
        account.deposit(amount)
        print(f"Deposited: ${amount:.2f}")
    elif command == "withdraw" and amount is not None:
        if account.withdraw(amount):
            print(f"Withdrew: ${amount:.2f}")
        else:
            print("Insufficient funds.")
    elif command == "display":
        account.display_balance()
    else:
        print("Invalid command.")

if __name__ == "__main__":
    main()

