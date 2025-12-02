# Review for python chapter 3-5
# get your input for avarage and calculate the grade 
"""
average = float(input("Enter the avarage:"))
if average >= 90:
    letter_grade = 'A'
elif average >= 80:
    letter_grade = 'B'
elif average >= 70:
    letter_grade = 'C'
elif average >= 60:
    letter_grade = 'D'
else:
    letter_grade = 'F'
print(f'your final grade is {letter_grade}')
# match case 
login_status = 1
match login_status:
    case 1: print('invalid user name')
    case 2: print('invalid password')
    case 3: print('invalid login')
    case _: print('invalid input')
# another way 
match login_status:
    case 1 | 2 : print('invalid user name/password')
    case login_status if login_status !=3: print('invalid input')
    case 3: print('sucessfully login')
# random number/charactor
import random 
num1 = random.randint(1,10)
num2 = random.randrange(1,10)
print(f'randomly generated numbers: {num1} {num2}')
ch = chr(random.randint(ord('A'),ord('Z')))
print(f'the random charactor is {ch}')
# check vowel
ch = input('enter a charactor: ')
if ch.upper() in 'AEIOU':
    print(f'{ch} is a vowel')
# count vowel
word = input('enter a word:')
count = 0
for ch in word: 
    if ch.upper() in 'AEIOU' :
        count+= 1
print(f'there are {count} vowels in {word}')
# loops
# sentinel value controlled loop
SENTINEL = -99
total = 0
count = 0
num = float(input('enter a grade (or -99 to end):'))
while num != SENTINEL:
    if num >= 0 and num <=100:
        total += num 
        count += 1
    else:
        print('invalid grade, enter again')
    num = float(input('enter a grade (or -99 to end):'))

if count >0:
    average = total / count
    print(f'the average is {average:.2f}')

# flag controlled loop
matched = False 
magic_number = random.randint(1,10)
while not matched:
    guess_number = int(input('enter a number between 1-10:'))
    if guess_number == magic_number:
        print('congrates, you get it right')
    elif guess_number < magic_number:
        print('YOUR NUMBER IS TOO LOWW')
    else: 
        print('your number is too high')
if not matched:
    print('you did not get it')
"""
    #countner-controlled loop
# Counter-controlled loop
word = 'greetings'
for i in range(len(word)):
    print(word[i], end=' ')
print()  # Print newline

# Use continue and break
# Print only odd numbers from 0 to 10
for i in range(11):
    if i % 2 == 0:
        continue
    print(i, end=' ')
print()

# Break loop on first odd number (i.e., stop immediately if i is odd)
for i in range(11):
    if i % 2 != 0:
        break
    print(i, end=' ')
print()

# Menu-controlled loop
import random

while True:
    print('\nMath Calculator:')
    print('1. Addition')
    print('2. Multiplication')
    print('3. Exit the program')

    try:
        menu_selection = int(input('Enter your selection (1, 2, 3): '))
    except ValueError:
        print('Invalid input. Please enter a number.')
        continue

    if menu_selection == 3:
        print('Exiting the program...')
        break
    elif menu_selection == 1 or menu_selection == 2:
        num1 = random.randint(10, 50)
        num2 = random.randint(10, 50)

        if menu_selection == 1:
            result = num1 + num2
            print(f'{num1} + {num2} = {result}')
        else:  # menu_selection == 2
            result = num1 * num2
            print(f'{num1} * {num2} = {result}')
    else:
        print('Invalid selection. Please choose 1, 2, or 3.')







