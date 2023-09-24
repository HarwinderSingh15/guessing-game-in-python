from random import randint

guess = input("Enter your guess between 1 to 20: \n")

rand_num = randint(1, 20)

is_game_over = False

while True: 
    if is_game_over:
        break
    if int(guess) > rand_num:
        guess = input("Your guess is too high. Try again!\n")
    elif int(guess) < rand_num:
        guess = input("Your guess is too low. Try again!\n")
    else:
        print("You won. Your guess is correct.")
        start_over = input("Do you want to play again? (y/n)\n")
        if start_over == 'y':
            rand_num = randint(1, 20)
            guess = input("Enter your guess between 1 to 20: \n")
        else:
            is_game_over = True

            