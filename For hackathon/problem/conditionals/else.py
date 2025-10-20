age = int(input('enter your age: '))

if age <= 0:
    print('invalid age')
elif age >= 18:
    print('you can vote')
else:
    print('you are <18')
