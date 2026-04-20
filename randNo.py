import random
Cnumber=random.randrange(1,100)
userInput=int(input("Guess a number between 1 and 100: "))
if userInput==Cnumber:
    print("Congratulations! You guessed the number.")
else:
    print("Sorry, you didn't guess the number.")