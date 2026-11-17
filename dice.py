import random

def roll(sides=6):
  return random.randint(1, sides)
print("You rolled a", roll())
