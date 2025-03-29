try:
    a=int(input("Enter the first number: "))
    b=int(input("Enter the second number: "))
    division=a/b
    print(f"The result of the division is: {division}")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
