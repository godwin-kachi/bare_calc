'''
Project Name: Console Calculator
Built: 24-03-23
'''

num1 = int(input('Random number 1: '))
num2 = int(input('Random number 2: '))
answer = []

def quit():
    print('Thank you for using our app')
    print('Bye Bye')

def restart():
    print('''What would you like to do:
    1. Addition 
    2. Subtract
    3. Divide
    4. Multiply
    5. Power of
    6. Quit
        ''')

    try:
        choice = int(input('choice: '))
        match choice:
            case 1:
                print(f'{num1} + {num2} = ', num1 + num2)
            case 2:
                print(f'{num1} - {num2} = ', num1 - num2)
            case 3:
                if num2 == 0:
                    print('Unfortunately I cant divide by zero')
                    restart()
                else:
                    print(f'{num1} / {num2} = ', num1/num2 )
                    restart()
            case 4:
                print(f'{num1} x {num2} = ', num1*num2)
            case 5:
                print(f'{num1} ** {num2} = ', num1**num2)
            case 6:
                quit()
            case _:
                print('You have selected an option I do not recognize')
    except ValueError:
        print('I am programmed to accept digits and not text')
        quit()

restart()