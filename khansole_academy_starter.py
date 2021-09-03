"""
File: khansole_academy.py
-------------------------
Khansole Academy is a program that teaches users how to add by asking users to input answers for the addition of two
randomly generating integers between 10 and 99 inclusive. The program returns feedback based on the User's answers.

"""

import random
# use code below  to generate a random integer between 30 and 50 for example
#print(random.randint(30, 50))

# ********************************** YOUR CODE GOES BELOW HERE *********************************************************

"""
Variables used are:
    counter   -->Consecutively increased until 3 successes. Else initialised to 0
                 3 successes means user has mastered and should exit the program
    randomX   -->Stores the first random number for summation
    randomY   -->Stores the second random number for summation
    sumResult -->Stores the value of summation for comparison
    userInput -->Stores the user's attempted answer for comparion
"""


#Initialisation level
counter = 0

while (counter<3):                   #Ensures program runs till 3 consecutive successes
    
    #Use the random library to generate 2 2-digit positve integers and store in randomX and randomY
    randomX = random.randint(10,99)                                      
    randomY = random.randint(10,99)                                      
    sumResult = randomX + randomY                #Compute total and store in sumResult
    print("What is", randomX, "+", randomY, "?")
    userInput = int(input("Your answer: "))      #Store user's attempt as an integer in userInput
    
    #If user's response matches 'sumResult', Give appropriate feedback(correct) and increment counter by 1
    #At any point where user is wrong, give feedback(incorrect) and reset the counter to zero
    if (userInput==sumResult):
        counter+=1
        print("Correct! You've gotten", counter, "correct in a row.")    
    else:                                                                #I
        counter=0
        print("Incorrect! The expected answer is", sumResult)

#Here program has exited the while loop because user has had the 3 successive corrects
#Feedback is given and program terminated
print("Congratulations! You mastered addition")
