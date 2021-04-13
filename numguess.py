import random

number = random.randint(1, 20)
count = 0

def divhint(number):
    if number % 2 == 0:
        print('The number you are searching is even')
    else:
        print('The number you are searching is odd')

def rangehint(number):
    if number in range(1, 11):
        print('The number you are searching is between 1 and 10')
    else:
        print('The number you are searching is between 11 and 20')

def difhint(number, num):
    dif = abs(number - num)
    print('The absolute number betweeen your number and the number that you are searching is', dif)

num = int(input('Guess the number: '))
while num != number:
    if count == 0:
        divhint(number)
        count += 1
    elif count == 1:
        rangehint(number)
        count += 1
    elif count == 2:
        difhint(number, num)
        count += 1
    elif count == 3:
        print('The number that you were searching is', number)
        break
    num = int(input('Guess the number: '))
else:
    print('Congrats!!')




