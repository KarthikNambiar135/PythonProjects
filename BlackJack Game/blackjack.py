import random
from art import logo
print(logo)
cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
user_cards = []
pc_cards = []
def ask():
    blackjack = input("Do you want to play a game of BlackJack🥺? Type 'y' or 'n': ")
    if blackjack == 'y':
        user_cards.clear()
        pc_cards.clear()
        user_cards.append(random.choice(cards))
        user_cards.append(random.choice(cards))
        pc_cards.append(random.choice(cards))
        pc_cards.append(random.choice(cards))
        play()
    else:
        print("GOODBYE! DO PLAY AGAIN SOMETIME :)")
def dealer(user_cards, pc_cards, cards):
    while sum(pc_cards) < 17:
        pc_cards.append(random.choice(cards))
    if sum(pc_cards) > 21:
        print(f"Your Final Hand: {user_cards}, Final Score: {sum(user_cards)}")
        print(f"Computer's Final Hand: {pc_cards}, Final Score: {sum(pc_cards)}")
        print("Computer went over. You Won!🥳")
        ask()
    else:
        compare(sum(user_cards), sum(pc_cards))
def compare(user, pc):
    if user > pc:
        print(f"Your Final Hand: {user_cards}, Final Score: {sum(user_cards)}")
        print(f"Computer's Final Hand: {pc_cards}, Final Score: {sum(pc_cards)}")
        print("You Won!🥳")
        ask()
    elif user < pc:
        print(f"Your Final Hand: {user_cards}, Final Score: {sum(user_cards)}")
        print(f"Computer's Final Hand: {pc_cards}, Final Score: {sum(pc_cards)}")
        print("You Lose!☹️")
        ask()
    else:
        print(f"Your Final Hand: {user_cards}, Final Score: {sum(user_cards)}")
        print(f"Computer's Final Hand: {pc_cards}, Final Score: {sum(pc_cards)}")
        print("Draw!🙃")
        ask()
def play():
    print(f"Your Cards: {user_cards}, Current Score: {sum(user_cards)}")
    print(f"Computer's First Card: {pc_cards[0]}")

    if 11 in user_cards and 10 in user_cards:
        print(f"Your Final Hand: {user_cards}, Final Score: {sum(user_cards)}")
        print(f"Computer's Final Hand: {pc_cards}, Final Score: {sum(pc_cards)}")
        print("You Have BlackJack! You Won!🤩")
        ask()
    elif 11 in pc_cards and 10 in pc_cards:
        print(f"Your Final Hand: {user_cards}, Final Score: {sum(user_cards)}")
        print(f"Computer's Final Hand: {pc_cards}, Final Score: {sum(pc_cards)}")
        print("Computer has BlackJack! You Lose!😭")
        ask()
    else:
        if sum(user_cards) > 21:
            if 11 in user_cards:
                if (sum(user_cards)-1) > 21:
                    print(f"Your Final Hand: {user_cards}, Final Score: {sum(user_cards)}")
                    print(f"Computer's Final Hand: {pc_cards}, Final Score: {sum(pc_cards)}")
                    print("You went over. You Lose!😭")
                    ask()
            else:
                print(f"Your Final Hand: {user_cards}, Final Score: {sum(user_cards)}")
                print(f"Computer's Final Hand: {pc_cards}, Final Score: {sum(pc_cards)}")
                print("You went over. You Lose!😭")
                ask()

    card_choice = input("Type 'y' to get another card, type 'n' to pass: ")
    if card_choice == 'y':
        user_cards.append(random.choice(cards))
        if sum(user_cards) > 21:
            print(f"Your Final Hand: {user_cards}, Final Score: {sum(user_cards)}")
            print(f"Computer's Final Hand: {pc_cards}, Final Score: {sum(pc_cards)}")
            print("You went over. You Lose!😭")
            ask()
        else:
            play()
    if card_choice == 'n':
        dealer(pc_cards=pc_cards, cards=cards, user_cards=user_cards)
ask()
