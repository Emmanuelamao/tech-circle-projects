# Simple Calculator

# Getting user input
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Getting the operation choice from the user
print("Select operation: \n1. Add \n2. Subtract \n3. Multiply \n4. Divide")
choice = input("Enter choice(1/2/3/4): ")

# Performing the operation
if choice == '1':
    result = num1 + num2
    print(f"The result of {num1} + {num2} is {result}")
elif choice == '2':
    result = num1 - num2
    print(f"The result of {num1} - {num2} is {result}")
elif choice == '3':
    result = num1 * num2
    print(f"The result of {num1} * {num2} is {result}")
elif choice == '4':
    if num2 != 0:
        result = num1 / num2
        print(f"The result of {num1} / {num2} is {result}")
    else:
        print("Error! Division by zero.")
else:
    print("Invalid input")
