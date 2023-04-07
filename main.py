import random  # importing random  Module to use predefined methods


# This function generates a random number between 1-100 and returns it.
def random_number_generator():
    return random.randint(1, 100)


# Thins function is used to start the game
def start_game():
    # Generated random number is assigned to a variable by calling function
    systemRandom = random_number_generator()

    # To count Player guess a variable is initialised
    userGuessCounter = 0

    # loop until the user guesses the correct number or decides to quit
    while True:
        # get User's guess and assigning it to a variable
        userGuess = input("Guess a number between 1 and 100 [or type '0' to quit]: ")

        if userGuess == '0':
            print("You have exited the game.")
            break  # to exit the loop break is used

        # convert the user's guess to an integer
        guess = int(userGuess)

        # increment the number of guesses
        userGuessCounter += 1

        # check if the user's guess is correct
        if guess == systemRandom:
            print("Congratulations! You have guessed the correct number in " ,userGuessCounter ," guesses")
            break

        # Feed back to user,based on the number they have guessed
        if guess < systemRandom:
            print("The number you guessed is Too low.")
        else:
            print("The number you guessed is Too high.")


# call the start_game() function to start the game
start_game()
