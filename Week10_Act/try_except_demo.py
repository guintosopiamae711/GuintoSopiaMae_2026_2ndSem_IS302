try:
    number_smg = int(input("Enter a number: "))
    result_smg = 100 / number_smg
    print("Result:", result_smg)
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Invalid input")
