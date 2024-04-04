import random

username = input("Guess the number! What's your name? ")
print("Okay " + username + ", let's begin!")
number = random.randint(1, 10)
pick = input("Pick a number from 1 to 10: ")
pick = int(pick)
attempts = 1
while pick != number:
    pick = input("Oops, try again: ")
    pick = int(pick)
    attempts += 1
else:
    print("Congratulations " + username + "! You've won in " + str(attempts) + " attempts.")