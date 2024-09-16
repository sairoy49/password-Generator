def calculator():
        try:
            a = float(input("Enter the value  a: "))
            b = float(input("Enter the value  b: "))
            operator = input("Enter the operation to be performed (+, -, *, /, %): ")
        
            if operator == '+':
                result = a + b
            elif operator == '-':
                result = a - b
            elif operator == '*':
                result = a * b
            elif operator == '/':
                result = a / b
            elif operator == '%':
                result = a % b
            else:
                result = 'Invalid operation'
        
            print(f"{a} {operator} {b} is {result}")
    
        except ZeroDivisionError:
            print("You cannot divide by zero.")
    
        except ValueError:
            print("Please enter valid numbers.")

calculator()