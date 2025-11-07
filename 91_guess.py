import random

def guess_the_number():
    print("Welcome to the Guess the Number Game!")
    print("I have selected a number between 1 and 100. Can you guess it?\n")

    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    attempts = 0
    guessed_correctly = False

    while not guessed_correctly:
        try:
            # Get the player's guess
            player_guess = int(input("Enter your guess: "))
            attempts += 1

            # Provide feedback to the player
            if player_guess < number_to_guess:
                print("Too low! Try again.")
            elif player_guess > number_to_guess:
                print("Too high! Try again.")
            else:
                guessed_correctly = True
                print(f"Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts.")
        except ValueError:
            print("Please enter a valid number.")

# Run the game
guess_the_number()
