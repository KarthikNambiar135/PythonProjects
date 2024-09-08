# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary
bid = {}
more_bidders = True
def compare(bids):
    amt = 0
    winner = ""
    for key in bids:
        if bid[key] > amt:
            amt = bid[key]
            winner = key
    print(f"The winner is {winner}.")
while more_bidders:

    name = input("What's your name?")
    price = float(input("What's your bid?"))
    bid[name] = price
    choice = input("Is there anyone else ready to bid?(yes or no)").lower()
    if choice == "no":
        more_bidders = False
        compare(bid)
    else:
        print("\n" * 100)
