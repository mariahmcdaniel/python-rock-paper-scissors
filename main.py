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


player = input("                  READY?\n\n\n                    Enter 'r' for rock, 'p' for paper, or 's' for scissors: ")
r = ["s", "s", "r"]
p = ["r", "r", "p"]
s = ["p", "p", "s"]
rules = [r,s,p]

if player.lower() == "r":
    print(rock)
elif player.lower() == "p":
    print(paper)
elif player.lower() == "s":
    print(scissors)        

computer = random.randint(0,2)

print(computer)

comp_move = s 

if computer == 0:
    comp_move  = r
    print(f"    COMPUTER CHOSE:\n                                 {rock}")

elif computer == 1:
    comp_move = p
    print(f"    COMPUTER CHOSE:\n                                 {paper}")

else:
    print(f"    COMPUTER CHOSE:\n                                 {scissors}")

print(computer)
print(comp_move)


result = comp_move.count(player)


if result == 0:
   print("You lost")
elif result == 1:
    print("You tied")
else:
    print("You won!!")      

