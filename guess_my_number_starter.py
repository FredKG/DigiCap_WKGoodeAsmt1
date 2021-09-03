"""
File: guessmynumber.py
----------------------
This program checks if a user's guess of a number matches that guessed by the computer
"""

import random
# use code below  to generate a random integer between 30 and 50 for example
#print(random.randint(30, 50))

# ********************************** YOUR CODE GOES BELOW HERE *********************************************************

"""
Variables used are:
    randomNum -->Stores the system generated random number for comparison
    userGuess -->Stores the user's attempted guess for comparison
"""


#Use the random library to generate a random integer between 1 and 99 and store in randomNum
randomNum = random.randint(1, 99)                           

#Display request for user guess on the number. Store it as an integer in the userGuess variable
print("I am thinking of a number between 1 and 99")         
userGuess = int(input("Enter a guess: "))

while (userGuess!=randomNum):
    #Loop the following part of the code until user guesses right
    """If user's guess is outside the range of (1 to 99),give feedback(invalid) and request a new guess
            If user's guess is greater than expected, give feedback(too high) and request a new guess
            or if the guess is lesser that expected, give feedback(too low) and request a new guess"""
    if (userGuess <1 or userGuess>99):
        print("Invalid Input")
        userGuess = int(input("Enter a new guess:"))
    elif (userGuess > randomNum):
        print("Your guess is too high")
        userGuess = int(input("Enter a new guess:"))
    else:
        print("Your guess is too low")
        userGuess = int(input("Enter a new guess:"))

#After user guesses right, give congratulatory remarks and end program
print("Congratulations! The number was:", randomNum)
