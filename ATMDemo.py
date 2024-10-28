'''
Author: Aswathi Biju
Date: 28/10/2024
Description: program that simulates a simple bank ATM system.
The user has an initial balance of $1000.
The ATM should display a menu with options to:
    1.Check Balance
    2.Deposit Money
    3.Withdraw Money
    4.Exit
'''
balance_amount=1000
while True:
    print("\n1. \tCheck Balance")
    print("2. \tDeposit Money")
    print("3. \tWithdraw Money")
    print("4. \tExit")
    choice=int(input("Enter your choice: "))
    if choice ==1:
        print(f"The current balance ${balance_amount}")
    elif choice == 2:
        deposit_amount= float(input("Enter amount: "))
        print(f"The deposit amount ${deposit_amount} and"
             f"The current balance ${balance_amount}")
    elif choice == 3:
        withdraw_amount= float(input("Enter the amount to withdraw: "))
        print(f"The amount to withdraw ${withdraw_amount}"
              f"The current balance ${balance_amount}")
        if withdraw_amount>balance_amount:
            print("Insufficient Amount")
        else :
            print("Sufficient Amount")
    elif choice ==4:
        break
    else :
        print("Invalid Entry")
