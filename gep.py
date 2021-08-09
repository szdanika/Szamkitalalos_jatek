import math;
import random;
import os;

class Variebels:
    Guessnumber = 0
    Right_guess = False
    Guessednumber = 50

def NumberCreator():
    Variebels.Guessnumber = random.randrange(0,100)
    print (Variebels.Guessnumber)

def NumberGuess():
    if(Variebels.Guessednumber < Variebels.Guessnumber):
        Variebels.Guessednumber = Variebels.Guessednumber + 1
        print(Variebels.Guessednumber)
 
    if(Variebels.Guessednumber > Variebels.Guessnumber):
        Variebels.Guessednumber = Variebels.Guessednumber - 1
        print(Variebels.Guessednumber)

    if(Variebels.Guessednumber == Variebels.Guessnumber):
        print("Your number is equal with my number !")
        Variebels.Right_guess = True

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    NumberCreator()
    while(Variebels.Right_guess == False):
        NumberGuess()

    print("My number was :", Variebels.Guessnumber)
    print("Do you want to player another game? (Y = yes , N = no")
    if(input() == 'Y'):
        print("alright")
        Variebels.Guessednumber = 50
        Variebels.Right_guess = False
        main()
    
    print("Alright then see you soon !")
    input()
main()