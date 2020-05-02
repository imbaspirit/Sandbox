import random

number = random.randint(1, 100)
# print(number)
user_number = None
count = 0
levels = {1: 9, 2: 7, 3: 5, 4: 3, 5: 1}
level = int(input('Choose the difficulty level for your GAME:\n"I’m too young to die" - press 1'
                  '\n"Hey, not too rough" - press 2'
                  '\n"Hurt me plenty" -press 3'
                  '\n"Ultra-Violence" - press 4'
                  '\n"Nightmare!" - press 5\n '))
max_count = levels[level]

user_count = int(input('Enter the number of Players: '))
users = []
for i in range(user_count):
    user_name = input(f'Enter the name of {i + 1} Player: ')
    users.append(user_name)

winner = False
winner_name = None

while not winner:
    count += 1
    if count > max_count:
        print('\nNobody wins...')
        break
    print(f'\nAttempt №{count}')
    for user in users:
        print(f'{user} turn.')
        user_number = int(input('Enter the number from 1 to 100: '))
        if user_number == number:
            winner = True
            winner_name = user
            break
        elif number < user_number:
            print("Your number is bigger than My.\nAccess denied..\n")
        else:
            print('Your number is smaller than My.\nAccess denied..\n')
else:
    print(f'\n\nAccess granted to {winner_name}\n\n')

