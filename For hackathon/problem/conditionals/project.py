num1 = float(input('enter first number: '))
num2 = float(input('enter second number: '))
choice = input('Enter your choice + - *')

if choice == '+':
    print(f'Addition: {num1 + num2}')
elif choice == '-':
    print(f'Substraction: {num1 - num2}')
else:    
    print(f'Multiplication: {num1*num2}')
    