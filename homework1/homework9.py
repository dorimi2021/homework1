from random import randint

x = randint(1, 100)
count = 0
print(f'Guess the number between 1 and 100 \nIs {x} the guessed number?')
while count<=100:
    answer = str(input())
    if answer == 'yes':
        count += 1
        print(f'Great! I tried {count} times')
        break
    elif answer == 'no':
        y = randint(1, 100)
        count += 1
        print(f'Is {y} the guessed number?')
    else:
        print('Answer yes or no')