import random

player = input("                  READY?\n\n\n                    Enter 'r' for rock, 'p' for paper, or 's' for scissors: ")
r = ["s", "s", "r"]
p = ["r", "r", "p"]
s = ["p", "p", "s"]
rules = [r,s,p]

computer = random.randint(0,2)

print(computer)

comp_move = s 

if computer == 0:
    comp_move  = r

elif computer == 1:
    comp_move = p

print(computer)


result = comp_move.count(player)


if result == 0:
   print("You lost")
elif result == 1:
    print("You tied")
else:
    print("You won!!")      

