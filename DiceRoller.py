

import random


# Start Loop & Ask user
while True:
    Reply = input('Roll the dice? (Yes/No): ').lower().strip()
    # If user enters "yes"
    if Reply == 'yes':
        # Generate two random numbers
        dice_outcome1 = random.randint(1, 6)
        dice_outcome2 = random.randint(1, 6)
        print(
            f'({dice_outcome1}, {dice_outcome2}). You rolled a {dice_outcome1 + dice_outcome2}!')
    # if user enters "no"
    elif Reply == 'no':
        # print a thank you messege
        print('thanks for playing!')
        # terminate
        break
    # Else, Print "Invalid Choice"
    else:
        print('Invalid Choice!')
