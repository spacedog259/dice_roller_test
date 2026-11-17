import random

def roll(sides=6):
  return random.randint(1, sides)
a,b=roll(),roll()
print(f"You rolled {a} and {b}, total {a+b}")
