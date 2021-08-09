import math;
import random;
import os;

class Variebels:
    Guessnumber = 0
    Right_guess = False

def NumberCreator():
    Variebels.Guessnumber = random.randrange(0,100)

def NumberGuess():
    Guessednumber = int(input())
    if(Guessednumber < Variebels.Guessnumber):
        print("Your number is lower than my number")
 
    if(Guessednumber > Variebels.Guessnumber):
        print("Your number is higher then my number")

    if(Guessednumber == Variebels.Guessnumber):
        print("Your number is equal with my number !")
        Variebels.Right_guess = True

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    NumberCreator()
    while(Variebels.Right_guess == False):
        NumberGuess()

    print("Do you want to player another game? (Y = yes , N = no")
    if(input() == 'Y'):
        print("alright")
        Variebels.Right_guess = False
        main()
    
    print("Alright then see you soon !")
    input()
main()