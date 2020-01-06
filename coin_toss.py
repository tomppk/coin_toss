# Import random.py library
import random as rd

# User can play two different games of chance. [1] Coin flip: guess whether the result is heads or tails. [2] Dice throw: guess the number from 1 to 6. 

# Function for user to guess heads or tails for coin flip
def user_guess():
    try:
        choice = int(input("Please choose: [1] for Heads or [2] for Tails: "))
        if choice == 1:
            print("You guessed Heads.")
            dot = "."
            for i in range(3):
                print(dot)
                dot += "."
        elif choice == 2:
            print("You guessed Tails.")
            dot = "."
            for i in range(3):
                print(dot)
                dot += "."
        elif 1 < choice > 2:
            print("Invalid choice. Please try again.")
            choice = user_guess()
        return choice
    except(ValueError, NameError, SyntaxError):
        print("Sorry, invalid selection. Please try again.")
        choice = user_guess()
        return choice

# Counters for total tries and correct guesses 
counter_total = []
counter_correct = []

# Random coin flip
def coin_flip():
    result = rd.randint(1, 2)
    if result == 1:
        print("And the result is Heads.")
    elif result == 2:
        print("And the result is Tails.")
    return result


# Compare result of coin flip and user's guess
def result_coin_flip():
    guess = user_guess()
    coin = coin_flip()
    if guess == coin:
        print("You guessed right!")
        counter_total.append(1)
        counter_correct.append(1)
        print("You have guessed right {} / {} times.".format(len(counter_correct), len(counter_total)))
        accuracy = len(counter_correct) / len(counter_total) * 100
        print("With an accuracy of " + str(round(accuracy, 2)) + "%")
        try1 = str(input("Do you want to continue playing? Y/N\n"))
        if try1.lower() == "y":
            return main_sequence()
        else:
            print("\nGoodbye!")
    else:
        print("No luck this time. Nice try.")
        counter_total.append(1)
        print("You have guessed right {} / {} times.".format(len(counter_correct), len(counter_total)))
        accuracy = len(counter_correct) / len(counter_total) * 100
        print("With an accuracy of " + str(round(accuracy, 2)) + "%")
        try2 = str(input("Do you want to continue playing? Y/N\n"))
        if try2.lower() == "y":
            return main_sequence()
        else:
            print("\nGoodbye!")
        
# Counters for total tries and correct guesses for dice throw
counter_dice_total = []
counter_dice_correct = []

# User guess for dice throw for numbers 1-6
def dice_user_guess():
    try:
        choice = int(input("Please choose a number between 1 - 6.\n"))
        if choice > 6 or choice < 1:
            print("Sorry, invalid choice. Please try again.")
            return dice_user_guess() 
        dot = "."
        for i in range(3):
            print(dot)
            dot += "."
        else:
            print("You guessed " + str(choice))
            return choice
    except(ValueError, NameError, SyntaxError):
        print("Sorry, invalid selection. Please try again.")
        choice = dice_user_guess()
        return choice

# Random dice throw
def dice_throw():
    result = rd.randint(1, 6)
    print("And the result is " + str(result))
    return result

# Compare result of dice throw and user's guess
def result_dice_throw():
    guess = dice_user_guess()
    dice = dice_throw()
    if guess == dice:
        print("You guessed right!")
        counter_dice_total.append(1)
        counter_dice_correct.append(1)
        print("You have guessed right {} / {} times.".format(len(counter_dice_correct), len(counter_dice_total)))
        accuracy = len(counter_dice_correct) / len(counter_dice_total) * 100
        print("With an accuracy of " + str(round(accuracy, 2)) + "%")
        try1 = str(input("Do you want to continue playing? Y/N\n"))
        if try1.lower() == "y":
            return main_sequence()
        else:
            print("\nGoodbye!")
    elif guess != dice:
        print("No luck this time. Nice try.")
        counter_dice_total.append(1)
        print("You have guessed right {} / {} times.".format(len(counter_dice_correct), len(counter_dice_total)))
        accuracy = len(counter_dice_correct) / len(counter_dice_total) * 100
        print("With an accuracy of " + str(round(accuracy, 2)) + "%")
        try2 = str(input("Do you want to continue playing? Y/N\n"))
        if try2.lower() == "y":
            return main_sequence()
        else:
            print("\nGoodbye!")


# Main sequence for games
def main_sequence():
    print("""
    Welcome to Games of Chance!\n
    Do you want to play Coin Flip or Dice Throw?\n
    """)
    choice = int(input("Please choose: [1] Coin Flip or [2] Dice Throw.: "))
    try:
        if choice == 1:
            return result_coin_flip()
        elif choice == 2:
            return result_dice_throw()
        elif 1 < choice > 2:
            print("\nInvalid choice. Please try again.\n")
            return main_sequence()
    except(ValueError, NameError, SyntaxError):
        print("\nSorry, invalid selection. Please try again.\n")
        return main_sequence()
    
    
main_sequence()



