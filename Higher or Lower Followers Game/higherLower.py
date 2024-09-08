#importing modules
from art import logo
from art import vs
from game_data import data
import random
#printing logo
print(logo)
#function to call if the answer is wrong
def wrong(score):
    print("Sorry That's Wrong.")
    print(score)
#declaring count and i variable and initializing it to True and 0 respectively
count = True
i = 0
#while loop to continue the program as long as the answer is correct
while count:
    #choosing 2 random data as a and b
    a = random.choice(data)
    b = random.choice(data)
    #in case both are equal, b is regenerated
    while a == b:
        b = random.choice(data)
    #printing the comparisons
    print(f"Compare A: {a['name']}, {a['description']}, from {a['country']}")
    print(vs)
    print(f"Compare B: {b['name']}, a {b['description']}, from {b['country']}")
    #taking input from the user as a or b
    user_answer = input("Who has more Instagram followers?(A or B): ").lower()
    #conditional statements to compare the answer
    if user_answer == 'a':
        if a['follower_count'] > b['follower_count']:
            #increasing score for correct answer
            i += 1
            print(f"You are right! Current Score: {i}")
            print("\n" *20)
            print(logo)
        else:
            #stopping the loop when wrong answer
            count = False
            print("\n" * 20)
            print(logo)
            wrong(i)
    elif  user_answer == 'b':
        if b['follower_count'] > a['follower_count']:
            # increasing score for correct answer
            i += 1
            print(f"You are right! Current Score: {i}")
            print("\n" * 20)
            print(logo)
        else:
            # stopping the loop when wrong answer
            count = False
            print("\n" * 20)
            print(logo)
            wrong(i)
    else:
        #statement in case of invalid input from the user
        print("Invalid input, restarting game.")
        print("\n" * 20)
