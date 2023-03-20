"""
Hello! What is your name?
name

Well, name, I am thinking of a number between 1 and 20.
Tak a guess.
yourNumber

output: 
Your guess it too high.
Take a guess.
"""

print("What is your name?")
yourName = input()

print("Well " + yourName + ", I am thnking of a number between 1 and 20.  Take a guess:")
yourNumber = input()

yourNumber = int(yourNumber)

if(yourNumber == 6):
    print("You Guessed right!")
elif (yourNumber > 6):
    print("Your Guess is too high")
else:
    print("Your Guess is too low")


