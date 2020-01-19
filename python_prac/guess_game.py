#generate 3 random numbers, ask user to guess 3 nmbers. print the correct guess and wrong guess

import random

def convert(s=[]):
    i = ""
    for x in s:
        i += str(x)
    return i

def guess_game():
    n=[]
    for count in range(0,3):
        n.append(random.randint(0,9))

    z=convert(n)
    print("Random Numbers: ",z)

    for i in range(0,3):
        a=input("enter the number you guess: ")
        if a in z:
            print("Your Guess is Right...")
        else:
            print("Wrong Guess!")


guess_game()


