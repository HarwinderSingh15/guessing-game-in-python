from random import randint

rand_num = randint(1, 20)

while True: 
    guess = input("Enter your guess between 1 to 20: \n")
    guess = int(guess)
    if guess > rand_num:
        print("TOO HEIGH!")
    elif guess < rand_num:
        print("TOO LOW!")
    else:
        print("You won. Your guess is correct.")
        start_over = input("Do you want to play again? (y/n)\n")
        if start_over == 'y':
            rand_num = randint(1, 20)
            guess = None
        else:
            break

            