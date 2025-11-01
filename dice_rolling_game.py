import random

while True:
    choice = input('Roll the dice (y/n): ')
    if choice == 'y':
        die1 = random.randint(1,6)
        die2 = random.randint(1,6)
        print(f'you rolled ({die1}, {die2})')
    elif choice == 'n':
        print('good bye!')
        break
    else:
        print('please choose y or n')