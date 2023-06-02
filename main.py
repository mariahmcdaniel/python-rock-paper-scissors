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

score = 0

player = input("                  READY?\n\n\n                    Enter 'r' for rock, 'p' for paper, or 's' for scissors: ")
r = ["s", "s", "r"]
p = ["r", "r", "p"]
s = ["p", "p", "s"]
rules = [r,s,p]

if player.lower() == "r":
    print(f"                       YOU CHOSE:            ROCK\n\n                                 {rock}")
elif player.lower() == "p":
    print(f"                       YOU CHOSE:            PAPER\n\n                                 {paper}")
elif player.lower() == "s":
    print(f"                       YOU CHOSE:            SCISSORS\n\n                                 {scissors}")        

computer = random.randint(0,2)


comp_move = s 

if computer == 0:
    comp_move  = r
    print(f"    COMPUTER CHOSE:              ROCK\n\n                                 {rock}")

elif computer == 1:
    comp_move = p
    print(f"    COMPUTER CHOSE:              PAPER\n\n                                 {paper}")

else:
    print(f"    COMPUTER CHOSE:              SCISSORS\n\n                                 {scissors}")



result = comp_move.count(player)


if result == 0:
   print(f"You lost... Your Score Is: {score}")
   score -= 1
elif result == 1:
    print(f"You tied -- Your Score Is: {score}")
else:
    print(f"You won!! Congrats. Your Score Is: {score}")
    score += 1      

