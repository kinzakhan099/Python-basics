bankBalance=int(input("Enter your bank balance: "))
withdrawAmount=int(input("Enter amount to withdraw: "))
try:
    if withdrawAmount>bankBalance:
        raise ValueError("Insufficient balance! Withdrawal denied.")
    elif withdrawAmount<0:
        raise ValueError("Withdrawal amount must be positive")
    else:
        print(f"Withdrawal of {withdrawAmount} successful!")
        bankBalance -= withdrawAmount
finally:
    print("Transaction completed")
    print(f"Your bank balance is: {bankBalance}")