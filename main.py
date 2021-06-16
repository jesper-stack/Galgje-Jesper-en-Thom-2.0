import random
# name = input("Wat is je naam? ")
# print("Welkom " + name)
Woorden = ["Boom", "Roos", "Vis"]
for woord in Woorden :
  print(woord)
gekozenWoord = random.choice(Woorden)
for letter in gekozenWoord :
  print("_ ", end = "")