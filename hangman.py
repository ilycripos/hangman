#Importing modules
import time
from random_word import RandomWords

#Asking for the player's name
name=input("What is your name?")

#Greet the player
print("Hello, " + name + " Time to play!")

#Wait 1 second
time.sleep(1)

#Begin the guessing process
print("Start guessing!")
time.sleep(0.5)

#Defining ask_again variable
ask_again = "yes"

#Defining isdigit() and isalnum() to detect if the user's guess contains digits or alnums
def isdigit(str):
    for char in str:
        if not char.isalnum() or char.isdigit():
            return True
    return False

#Game continues until user states an input other than "yes" or "y"
while ask_again == "yes" or ask_again == "y":

    #Defining random word generation variable
    word = RandomWords().get_random_word()

    #Defining guesses variable 
    guesses = ''

    #Defining turns variable 
    turns = 10

    #Detecting if number of turns goes below 0, meaning failure
    while turns > 0: 
        failed = 0

        #Loop through all the characters in word and check if the character is valid or not
        for char in word:
            if char in guesses:
                print(char,end="")

            #If guess is wrong, prints '-' and adds failed
            else:
                print("-",end="")
                failed += 1

        #If there are no fails before guess run out, you win
        if failed == 0:
            print(" You won!")
            break
        
        #Detecting user input for character guessing
        guess = input(" guess a character: ")
        
        #If the guess is/contains a digit (0,9) it will come out as an invalid guess, keeping guess count the same
        if isdigit(guess):
            print("Invalid  Character")
            continue

        #Add user guess to array of guesses        
        guesses += guess[0]

        #If the alphabetical guess is not in the word, will remove one guess from the count and say that it is wrong
        if guess not in word: 
            turns -= 1
            print("Wrong")
            print(f"You have {str (turns)} guesses left")

            #Once your turn count equals 0, the program will recognise you have lost and tell you what the word was
            if turns == 0:
                print("You lose!")
                print(f"The correct word was {word}.")

    #Ask the user would like the play again
    ask_again = input("Play again? ")

#Say goodbye to the player if they do not wish to play again
print("Thank you for playing, goodbye!")