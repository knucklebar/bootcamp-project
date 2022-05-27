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
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
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


first_choice = input("You are on a valley where do you choose to go.'up' or 'down'? ")

if first_choice == "down":
  print("You get eaten by Hyenas! Game Over")
else:
  second_choice = input("You reached the end of the valley and find a river do you 'swim' or 'search' for another way? ")
  if second_choice == 'swim':
    print("You get caught in the current and drown")
  else:
    third_choice = input("You search for sometime and find a bridge, you cross it and reacha clearing having 3 caves with symbols '#', '&' and '%' on it which do you choose? ")
    if third_choice == '&':
      print("You enter the cave there and you light a lamp to see things clearly but as the cave is filled with sulphur you get caught in it! Game Over")
    elif third_choice == '%':
      print("You enter the came and a big bolder falls on you. Game Over!")
    elif third_choice == '#':
      print("You are scared by noises and run to the end of the cave and you come across a clearing with a man and a treasure chest. Congratulations you won the game!")
    else:
      print("You failed to choose the right cave and get eaten by wild animals. Game Over!")
  