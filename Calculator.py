def addition(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiplication(x, y):
    return x * y

def division(x, y):
    return x / y

print("Welcome to Jaya's Calculator 📱🧑‍🏫🧑‍💻")
print("Let's do some calculation!")
print("Choose an option according to your task: ")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

while True:
    choice = input("Enter your choice (1/2/3/4): ")
    
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        
        if choice == '1':
            print(f"{num1} + {num2} = {addition(num1, num2)}")
        elif choice == '2':
            print(f"{num1} - {num2} = {subtract(num1, num2)}")
        elif choice == '3':
            print(f"{num1} * {num2} = {multiplication(num1, num2)}")
        elif choice == '4':
            print(f"{num1} / {num2} = {division(num1, num2)}")
    else:
        print("Invalid input! Please enter a valid option.")
    
    next_calc = input("Do you want to do another calculation? (yes/no): ")
    if next_calc.lower() == 'no':
        break

print("Thank you for using Jaya's Calculator! Have a great day! 😊")
