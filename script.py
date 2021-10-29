import random 

# generate random letter between A-Z
#random_letter =random.randbytes(A,Z)
random_letter = str(random_letter)

guess_count = 1
# Let the user choose a level of difficulty at the beginning of the program.
user_input = input("Pick a level")
game_level = ("Easy", "Normal", "Hard")

# At the start of the game, let the user know how many letters the computer's word contains.

if game_level = "Easy"
    print ("This game only contains 4-6 characters")
    user_input = input("Continue" or "Go Back")
    
    if user_input = ("Continue")
    print ("Start Game")
    
    if user_input = ("Go Back")
    print ("Pick a level")
    game_level = input("Easy", "Normal", "Hard")


if game_level = "Normal"
    print ("This game only contains 6-8 characters")
    user_input = input("Continue" or "Go Back")
    
    if user_input = ("Continue")
    print ("Start Game")

    if user_input = ("Go Back")
    print ("Pick a level")
    game_level = input("Easy", "Normal", "Hard")


if game_level = "Hard"
    print ("This game contains 8 or more characters")
    user_input = input("Continue" or "Go Back")
    
    if user_input = ("Continue")
    print ("Start Game")

    if user_input = ("Go Back")
    print ("Pick a level")
    game_level = input("Easy", "Normal", "Hard")



# # Ask the user to supply one guess (i.e. letter) per roundThis letter can be upper or lower case and it should not matter. If a user enters more than one letter, tell them the input is invalid and let them try again.


# the game asking the user if the user wants to quit or not //!CONDITIONS (YOU WON, YOU LOST, YOU QUIT, START OVER!//
while user_input != 'No' and game_ends == False
# (YOU LOST) if the player uses all of the 8 tries incorrectly, they will lose. *Game Over*
    if guess_count == 8;
        print ("You Lost")
        user_input = input('Would you like to start over? Yes or No')
        game_ends = True
# (START OVER) if the player want to play again, game will start over and user gains 8 more tries
        if user_input == ("Yes")
            guess_count = 8
            game_ends = False


# Let the user choose a level of difficulty at the beginning of the program.
#  let the user know how many letters the computer's word contains. 

# f a user enters more than one letter, tell them the input is invalid and let them try again