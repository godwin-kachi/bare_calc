'''
Project Name: Console Calculator
Built: 24-03-23
'''

num1 = int(input('Random number 1: '))
num2 = int(input('Random number 2: '))

def more_evaluation(*num):
    pass


def add(num1, num2):
    ans = num1 + num2
    print(f'{num1} + {num2} = ', ans)
    restart()

def quit():
    print('Thank you for using our app')
    print('Bye Bye')

def minus(num1, num2):
    print(f'{num1} - {num2} = ', num1 - num2)
    restart()

def divide(num1, num2):
    if num2 == 0:
        print('Unfortunately I cant divide by zero')
        restart()
    else:
        print(f'{num1} / {num2} = ', num1/num2 )
        restart()

def multiply(num1, num2):
    print(f'{num1} x {num2} = ', num1*num2)
    restart()

def raises(num1, num2):
    print(f'{num1} ** {num2} = ', num1**num2)
    restart()




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
                add(num1, num2)
            case 2:
                minus(num1, num2)
            case 3:
                divide(num1, num2)
            case 4:
                multiply(num1, num2)
            case 5:
                raises(num1, num2)
            case 6:
                quit()
            case _:
                print('You have selected an option I do not recognize')
                quit()
    except ValueError:
        print('I am programmed to accept digits and not text')
        quit()

restart()