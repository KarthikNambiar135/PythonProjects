print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
a = input("You are at a cross-road. Where do you want to go?(left or right)\n")
if a.lower() == "left":
    b = input("There's a river ahead. Do you want to swim or wait for a boat.\n")
    if b.lower() == 'wait':
        c = input("You find a boat and cross the river. There are three coloured doors ahead. "
                  "Which one are you choosing to enter?(red, yellow or blue)\n")
        if c.lower() == 'yellow':
            print("You have found the treasure!YOU WIN!VICTORYYY!!!")
        elif c.lower() == 'red':
            print("You got burnt by fire. Game over!")
        elif c.lower() == 'blue':
            print("You were eaten by a group of beasts. Game over!")
        else:
            print("Did nothing? Game over!")
    elif b.lower() == 'swim':
        print("You were attacked by a trout...and DIED. Game over!")
    else:
        print("Did nothing? Game over!")
elif a.lower() == 'right':
    print("You fell into a hole. Game over!")
else:
    print("Did nothing? Game over!")
