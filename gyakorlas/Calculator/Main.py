num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))


operator = input("Enter an operator(+ - * /): ")
if operator == "+":
    result = round(num1 + num2,2)
    print(f"{num1} + {num2} = {result}")
elif operator == "-":
    result = round(num1 - num2,2)
    print(f"{num1} - {num2} = {result}")
elif operator == "*":
    result = round(num1 * num2,2)
    print(f"{num1} * {num2} = {result}")
elif operator == "/":
    if num2 == 0:
        print(f"You can't divide with {num2}")
        exit(1)
    result = round(num1 / num2,2)
    print(f"{num1} / {num2} = {result}")