# Import random.py library
import random as rd

# Welcoming text 
print("Welcome to Coin Toss!\n")

# 1 for heads and 2 for tails
coin_side = ["Heads", "Tails"]

# Function for user to choose heads or tails
def user_guess():
    try:
        choice = int(input("Please choose: [1] for Heads or [2] for Tails: "))
        if choice == 1:
            print("Your choice is Heads.")
            dot = "."
            for i in range(3):
                print(dot)
                dot += "."
        elif choice == 2:
            print("Your choice is Tails.")
            dot = "."
            for i in range(3):
                print(dot)
                dot += "."
        elif choice > len(coin_side):
            print("Invalid choice. Please try again.")
            choice = user_guess()
        return choice
    except(ValueError, NameError, SyntaxError):
        print("Sorry, invalid selection. Please try again.")
        choice = user_guess()
        return choice


# Compare random result of coin flip and user guess
def result_coin_flip():
    result = rd.choice(coin_side)
    # print("The result of the coin toss is:", result)
    guess = user_guess()
    if guess == 1:
        guess = "Heads"
        if guess == result:
            print("AND the result is Heads.")
            print("You guessed correctly!")
        elif guess != result:
            print("AND the result is Tails.")
            print("Nope. Better luck next time!")
    elif guess == 2:
        guess = "Tails"
        if guess == result:
            print("Result is Tails.")
            print("You guessed correctly!")
        elif guess != result:
            print("Result is Heads.")
            print("Nope. Better luck next time!")


result_coin_flip()
    
# print(rd.choice(coin_side))


# print(rd.randint(1,6))
