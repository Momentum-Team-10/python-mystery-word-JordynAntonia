import random 

# convert to lists
words = []
underscores = []
guesses = []

# BEFORE THE GAME STARTS
user_input = input("Pick a level: Easy, Normal or Hard?")
game_input = ("Easy", "Normal", "Hard")

#USER PICKS CHALLENGE: EASY, NORMAL OR HARD

# Easy
if user_input == ("Easy"):
        print("This game only contains 4-6 characters, would you like to continue? ")
        game_input = input("Yes or No?")
if game_input == ("Yes"):
        game_input = input("Start Game by pressing enter")
        print("Guess a Letter")

    
if game_input == ("No"):
        user_input = input("Pick a level: Easy, Normal or Hard?")
        game_input = input("Start Game by pressing enter")
        print("Guess a Letter")

# Normal
if user_input == ("Normal"):
        print("This game only contains 6-8 characters, would you like to continue?")
        game_input = input("Yes or No?")
if game_input == ("Yes"):
        game_input = input("Start Game by pressing enter")
        print("Guess a Letter")

    
if game_input == ("No"):
        user_input = input("Pick a level: Easy, Normal or Hard?")
        game_input = input("Start Game by pressing enter")
        print("Guess a Letter")

# Hard 
if user_input == ("Hard"):
        print("This game contains 8 or more characters, would you like to continue?")
        game_input = input("Yes or No?")
if game_input == ("Yes"):
        game_input = input("Start Game by pressing enter")
        print("Guess a Letter")

    
if game_input == ("No"):
        user_input = input("Pick a level: Easy, Normal or Hard?")
        game_input = input("Start Game by pressing enter")
        print("Guess a Letter")

# GAME PULLS WORDS FROM WORD LIST 
with open ("words.txt") as file:
    strings = file.readlines()
    words.append(str)
    random_word = words [7].lower()
# # # adds an underscore to each letter of the word and asks user to "guess a letter"
#     word_length = range(len(random_word))
#     for num in word_length:
#         underscores.append('_')
#     underscores = "".join(underscores)
    
#     print(underscores)
#     user_input = input('Guess A Letter').lower()
# # # list comprehensions
#     for index in range(len(random_word)):
#         if random_word[index] == user_input:
#             underscores = underscores[0:index] + user_input + underscores[index+1:]
#     print('underscores', underscores)
        
#         random_word_list = [index+1:]
    
# # generate random letter between A-Z
# #random_letter =random.randbytes(A,Z)
# # random_letter = str(random_letter)

# # guess_count = 1
# # user_input = input("Pick a level")
# # game_level = ("Easy", "Normal", "Hard")

# # # At the start of the game, let the user know how many letters the computer's word contains.

# # # # Ask the user to supply one guess (i.e. letter) per roundThis letter can be upper or lower case and it should not matter. If a user enters more than one letter, tell them the input is invalid and let them try again.


# # # the game asking the user if the user wants to quit or not //!CONDITIONS (YOU WON, YOU LOST, YOU QUIT, START OVER!//
# # while user_input != 'No' and game_ends == False
# # (YOU LOST) if the player uses all of the 8 tries incorrectly, they will lose. *Game Over*
#     if guess_count == 8;
#         print ("You Lost")
#         user_input = input('Would you like to start over? Yes or No')
#         game_ends = True
# # (START OVER) if the player want to play again, game will start over and user gains 8 more tries
#         if user_input == ("Yes")
#             guess_count = 8
#             game_ends = False


# # # Let the user choose a level of difficulty at the beginning of the program.
# # #  let the user know how many letters the computer's word contains. 

# # # f a user enters more than one letter, tell them the input is invalid and let them try again