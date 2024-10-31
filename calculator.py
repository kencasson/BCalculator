# Functions
def add(x, y):
    result = x + y
    return result

def subtract(x, y):
    result = x - y
    return result

def multiply(x, y):
    result = x * y
    return result

def divide(x, y):
    if y == 0:
        return "Error: Division by zero is undefined"
    else:
        result = x / y
        return result

# Loop for Menu
while True:
    # Display Menu
    print("\nWelcome to the Calculator")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Quit") # Option to Quit.

    # Get User Choice
    choice = int(input("Enter choice (1/2/3/4/5 to quit): "))

    # Check if choice is valid
    if choice == 5:
        print("Sayonara!")
        break # Exit loop if user chooses to quit.
            
    elif choice in [1, 2, 3, 4]:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        # Perform the chosen operation
        if choice == 1:
            print("Result:", add(num1, num2))
        elif choice == 2:
            print("Result:", subtract(num1, num2))
        elif choice == 3:
            print("Result:", multiply(num1, num2))
        elif choice == 4:
            print("Result:", divide(num1, num2))
    else:
        print("Invalid input. Please select a valid operation")