import random
from art import logo2
print(logo2)
print("Welcome to the NUMBER GUESSING GAME!")
print("The Computer is thinking of a number between 1 and 100.")

def playing(count):
    chosen_number = random.randint(1, 101)
    i = 0
    guessing = True
    j = count
    while i < count and guessing:
        print(f"You have {j} attempts remaining to guess the number")
        j -= 1
        i += 1
        guess = int(input("Make a Guess: "))
        if guess < chosen_number:
            print("Too Low")
            print("Guess Again.")
        elif guess > chosen_number:
            print("Too High")
            print("Guess Again")
        else:
            print(f"GOOD JOB, You got it! The answer was {chosen_number}.")
            guessing = False
    if j <= 0:
        print(f"OOPS! It seems you have run out of guesses, YOU LOSE! The correct answer was {chosen_number}.")
    choice = input("Wanna Play Again? Type 'y' or 'n': ")
    if choice == 'y':
        play()
    else:
        print("GOODBYE!")
def play():
    count = 0
    difficulty = input("Choose a difficulty. Easy or Hard?: ").lower()
    if difficulty == 'easy':
        count = 10
    elif difficulty == 'hard':
        count = 5
    playing(count)
play()
