try:
    num1_smg = float(input("Enter first number: "))
    num2_smg = float(input("Enter second number: "))
    result_smg = num1_smg / num2_smg
    print("Result:", result_smg)
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Invalid numeric input")
