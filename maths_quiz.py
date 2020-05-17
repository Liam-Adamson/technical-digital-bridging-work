#Liam Adamson
#Maths questions
#17/05/2020

import random

def main():
    display_intro()
    display_menu()
    display_separator()
    get_user_input()
    display_separator()
    
def display_intro():
    title = "** Maths Quiz **"
    print('*'*len(title))
    print(title)
    print('*'*len(title))

def display_menu():
    menu_list = ['1. Easy', '2. Medium', '3. Hard', '4. Exit']
    print(menu_list[0])
    print(menu_list[1])
    print(menu_list[2])
    print(menu_list[3])

def display_separator():
    print('-'*16)

def get_user_input():
    quiz_length = 5
    score = 0
    user_input = int(input('Enter your choice (1-4): '))
    while user_input > 4 or user_input <= 0:
        print('Invalid menu option.')
        user_input = int(input('Please try again: '))
    if user_input == 4:
        print('Exiting maths quiz')
        display_separator()
        exit()

    for i in range(quiz_length):
        if user_input == 1:
            num1 = random.randint(1,10)
            num2 = random.randint(1,10)
            operator_list = ['+', '-', '/','*']
            operator = random.choice(operator_list)
            answer = 0
            if operator == '+':
                answer = num1 + num2
            elif operator == '-':
                answer = num1 - num2
            elif operator == '/':
                answer = num1 / num2
            elif operator == '*':
                answer = num1 * num2
        elif user_input == 2:
            num1 = random.randint(1,50)
            num2 = random.randint(1,50)
            operator_list = ['+', '-', '/','*']
            operator = random.choice(operator_list)
            answer = 0
            if operator == '+':
                answer = num1 + num2
            elif operator == '-':
                answer = num1 - num2
            elif operator == '/':
                answer = num1 / num2
            elif operator == '*':
                answer = num1 * num2
        elif user_input == 3:
            num1 = random.randint(1,100)
            num2 = random.randint(1,100)
            operator_list = ['+', '-', '/','*']
            operator = random.choice(operator_list)
            answer = 0
            if operator == '+':
                answer = num1 + num2
            elif operator == '-':
                answer = num1 - num2
            elif operator == '/':
                answer = num1 / num2
            elif operator == '*':
                answer = num1 * num2
        print(num1, operator, '__', '=', answer)

       

        user_guess = int(input('what is the missing number? '))
        if user_guess == num2:
            print('correct!')
            print(num1, operator, num2, '=', answer)
            score = score + 1
        else:
            print('incorrect! the correct answer was', num2)
    print('your score was, ', score, "out of ", quiz_length)
        
main()
