import random

print("Welcome to Guess the Number!")
print("The rules are simple. I will think of a number, and you will try to guess it.")

#statement generates a random number between 1 and 10
number = random.randint(1, 10)

#track if user guessed your number using vthis variable
isGuessRight = False

#handle game logic
while isGuessRight != True:
    guess = input("Guess a number between 1 and 10: ")
    if int(guess) == number:
        print("You guessed {}. That is correct! You win!".format(guess))
        isGuessRight = True
    else:
        print("You guessed {}. Sorry, that isn't it. Try again.".format(guess))
#game pseudocode
#If user has not guessed the correct answer,enter the loop
#Ask the user for a guess
#Is the guess the correct number?
#If the correct guess, tell the user it was the correct guess and exit loop
#If the wrong guess, tell the user it was the wrong guess and continue the loop