from time import perf_counter
import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors.\n"))
fig = [rock, paper, scissors]
options = [0,1,2]
pc_choice = options[random.randint(0,2)]
print(pc_choice)
if user_choice == pc_choice:
    print("Computer Choice:\n", fig[pc_choice])
    print("User Choice:\n", fig[user_choice])
    print("TIE!")
elif user_choice == 0:
    if pc_choice == 1:
        print("Computer Choice:\n", fig[pc_choice])
        print("User Choice:\n", fig[user_choice])
        print("COMPUTER WINS!")
    elif pc_choice == 2:
        print("Computer Choice:\n", fig[pc_choice])
        print("User Choice:\n", fig[user_choice])
        print("USER WINS!")
    else:
        print("INVALID INPUT!")
elif user_choice == 1:
    if pc_choice == 0:
        print("Computer Choice:\n", fig[pc_choice])
        print("User Choice:\n", fig[user_choice])
        print("USER WINS!")
    elif pc_choice == 2:
        print("Computer Choice:\n", fig[pc_choice])
        print("User Choice:\n", fig[user_choice])
        print("COMPUTER WINS!")
    else:
        print("INVALID INPUT!")
elif user_choice == 2:
    if pc_choice == 0:
        print("Computer Choice:\n", fig[pc_choice])
        print("User Choice:\n", fig[user_choice])
        print("COMPUTER WINS!")
    elif pc_choice == 1:
        print("Computer Choice:\n", fig[pc_choice])
        print("User Choice:\n", fig[user_choice])
        print("USER WINS!")
    else:
        print("INVALID INPUT!")
