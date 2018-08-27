num1 = float(input("Enter first number: ")) #user input 
op = input("Enter first Operator: ") #user input
num2 = float(input("Enter second number: ")) #user input

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "*":
    print(num1 * num2)
elif op == "/":
    print(num1 / num2)
elif op == "%":
    print(num1 % num2)
else:
    print("Invalid Operation")
