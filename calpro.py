# python-assignment-1
operation = input('''
Please type what type of opration u want to do=( +,-,*,/,%,**,//)>>>''')

number_1 = int(input('Enter your first number: '))
number_2 = int(input('Enter your second number: '))

if operation == '+':
    print('{} + {} = '.format(number_1, number_2))
    print(number_1 + number_2)

elif operation == '-':
    print('{} - {} = '.format(number_1, number_2))
    print(number_1 - number_2)

elif operation == '*':
    print('{} * {} = '.format(number_1, number_2))
    print(number_1 * number_2)

elif operation == '/':
    print('{} / {} = '.format(number_1, number_2))
    print(number_1 / number_2)
    
elif operation == '%':
    print('{} % {} = '.format(number_1, number_2))
    print(number_1 % number_2)
    
elif operation == '**':
    print('{} ** {} = '.format(number_1, number_2))
    print(number_1 ** number_2)
    
elif operation == '//':
    print('{} // {} = '.format(number_1, number_2))
    print(number_1 // number_2)

else:
    print('You have not typed a valid operator, please run the program again.')
