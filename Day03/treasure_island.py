import time

print(r'''
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
time.sleep(1)
print("Your mission is to find the treasure.")
time.sleep(2)
path_1 = input("There are 2 paths before you chose left or right. (left or right): ")
if path_1 == "left":
    time.sleep(1)
    path_2 = input("You come across a river will you swim or wait for a boat? (swim or wait): ")
    if path_2 == "wait":
        time.sleep(1)
        path_3 = input("You reach the treasure room but there are 3 doors which will you choose? (yellow, blue, red): ")
        if path_3 == "yellow":
            time.sleep(1)
            print("You win!")
        elif path_3 == "blue":
            time.sleep(1)
            print("You got eaten by a beast!")
            print("You lose!")
        elif path_3 == "red":
            time.sleep(1)
            print("You were burned by a fire!")
            print("You lose!")
        else:
            time.sleep(1)
            print("Bad choice!")
            print("Game Over!")
    else:
        time.sleep(1)
        print("You were eaten by a fish!")
        print("Game Over!")
else:
    time.sleep(1)
    print("You fell into a hole!")
    print("Game Over!")
