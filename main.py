import random

player = input("                  READY?\n\n\n                    Enter 'r' for rock, 'p' for paper, or 's' for scissors: ")
r = ["s", "s", "r"]
p = ["r", "r", "p"]
s = ["p", "p", "s"]
rules = [r,s,p]

computer = random.randint(0,2)

