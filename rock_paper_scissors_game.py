#this is a rock paper scissor game
import random
# generate computer choice
def computer_choice():
    choices = ["r", "p", "s"]
    return choices[random.randint(0,2)]
# get user input / catch exceptions 
def user_choice():
    while True:
        try: 
            choice = input("what do you choose? \n rock (r), paper (p) or scissors (s)").strip().lower()    #handle uppercase and spaces
            if choice == "r" or choice == "p" or choice == "s":
                return choice
            else:
                print("please use the designatet letter 'r', 'p', 's', to indicate your choice")
        except ValueError:
            print("please use the designatet letter 'r', 'p', 's', to indicate your choice")
# ask user how many rounds they want to play
def rounds():
    while True:
        try:
            round_number = int(input("how many rounds do you want to play?"))
            if round_number > 100:                     # make sure round_number not to high
                print("the maximum rounds are 100")
            elif round_number == 0:                 # handle 0 imput
                while True:
                    try:
                        answ = input("do you want to quit? y/n\n").strip().lower()
                        if answ == "y":
                            print("c u next time")
                            exit()
                        else:
                            break
                    except ValueError:
                        print("please answer 'y' or 'n'")
            else:
                return round_number
        except ValueError:
            print("please choose a whole number")

# dictionary for weapon choices
weapon ={
    "r": "Rock",
    "p": "Paper",
    "s": "Scissors"
}
# this part actually plays the game
def game(round_number):
    uCount = 0
    comCount = 0
     # get number of rounds to play from round_number function
    for i in range(round_number):
        uChoice = user_choice()
        comChoice = computer_choice()
        if uChoice == "r" and comChoice == "s" or uChoice == "s" and comChoice == "p" or uChoice == "p" and comChoice == "r":
            print(f"your enemy chose {weapon[comChoice]}")
            print(f"{weapon[uChoice]} beats {weapon[comChoice]}")
            print("you win!!")
            uCount += 1
        elif uChoice == comChoice:
            print(f"your enemy chose {weapon[comChoice]}")
            print("it's a draw")
        else:
            print(f"your enemy chose {weapon[comChoice]}")
            print(f"{weapon[comChoice]} beats {weapon[uChoice]}")
            print("you loose")
            comCount += 1
    return uCount, comCount        
   

def main():
    print("Hello, this is a rock paper scissors game")
    # loop to ensure valid input
    while True:
        play = input("do you want to play? y/n\n").strip().lower()
        if play == "y":
            
            while True:
                round_number = rounds()
                uCount, comCount = game(round_number)
                if uCount > comCount:
                    print(f"YOU WON!! with {uCount} to {comCount}")
                    play = input("want to go again? y/n\n").strip().lower()
                    if play != "y":
                        print("c u next time")
                        exit() # Exit the loop after the user decides not to play again
                elif uCount == comCount:
                    print(f"its a draw with {uCount} to {comCount}\n")
                    play = input("want to go again? y/n\n").strip().lower()
                    if play != "y":
                        print("c u next time")
                        exit() # Exit the loop after the user decides not to play again
                else:
                    print(f"YOUR LOOSE!!! with {uCount} to {comCount} \n")
                    play = input("want to go again? y/n\n") 
                    if play != "y":
                        print("c u next time")
                        exit() # Exit the loop after the user decides not to play again
        elif play == "n":
            print("c u next time")
            exit()  # Exit the loop if the user does not want to play
        else:
            print("Please enter a valid response ('y' or 'n')")


if __name__ == "__main__":
    main()