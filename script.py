import random 

# generate random letter between A-Z
#random_letter =random.randbytes(A,Z)
random_letter = str(random_letter)
# Ask the user to supply one guess (i.e. letter) per round
guess_count = 1
# Let the user choose a level of difficulty at the beginning of the program.
user_input = input("Pick a level")
game_level = ("Easy", "Normal", "Hard")

if game_level = "Easy"
    print ("Only 4-6 characters")

if game_level = "Normal"
    print ("Only 6-8 characters")

if game_level = "Hard"
    print ("8 or more characters")


# the game asking the user if the user wants to quit or not
while user_input != 'No' and game_ends == False
# if the player uses all of the 8 tries incorrectly, they will lose.*Game Over*
    if guess_count == 8;
        print ("You Lost")
        user_input = input('Would you like to try agian? Yes or No')
        game_ends = True
# if the player want to start over, they will get 8 more tries
        if user_input == ("Yes")
            guess_count = 8
            game_ends = False


# Let the user choose a level of difficulty at the beginning of the program.
#  let the user know how many letters the computer's word contains. 

# f a user enters more than one letter, tell them the input is invalid and let them try again