# Import random.py library
import random as rd

# Welcoming text 
print("Welcome to Coin Toss!\n")

coin_side = ["Heads", "Tails"]

# Function for user to choose heads or tails
def user_guess():
    try:
        choice = int(input("Please choose: [1] for Heads or [2] for Tails: "))
        if choice > len(coin_side):
            print("Invalid choice. Please try again.")
            choice = user_guess()
        return choice
    except(ValueError, NameError, SyntaxError):
        print("Sorry, invalid selection. Please try again.")
        choice = user_guess()
        return choice

user_guess()


# print(rd.choice(coin_side))

# print(rd.randint(1,6))