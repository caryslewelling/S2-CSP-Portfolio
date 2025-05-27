#Carys Lewelling
#Magic 8 Ball

#Initial
magic = ["Yes", "No", "Definitely", "Without a doubt", "Never", "Absolutely not", "Ask again later", "Perhaps", "Maybe", "Only time will tell", "Not ever", "For sure", "Absolutely", "Definitely not", "Don't count on it", "Signs point to yes", "Signs point to no", "Most likely",]
import random
import time

#Function
def game():
    a = random.choice(magic)
    q = input("Enter a yes or no question: ")
    if q.endswith("?"):
        print("Now shake the Magic 8 Ball")
        time.sleep(3)
        print(a)
    else:
        print("Enter a yes or no question with a question mark! Try again.")

def ball():
    print("Welcome to the Magic 8 ball game!")
    while True:
        g = input("Do you want to play the game?")
        if g == "yes" or g == "y":
            game()
        elif g == "no" or g == "n":
            print("ok goodbye")
            break
        else:
            print("Enter 'yes' or 'no'")

#Main
ball()
